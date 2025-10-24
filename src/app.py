import os
from dotenv import load_dotenv
load_dotenv()

# CRITICAL: Unset the Friendli base URL to prevent SDK from using it
if "OPENAI_API_BASE" in os.environ:
    del os.environ["OPENAI_API_BASE"]

import streamlit as st
from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import weaviate
from weaviate.classes.init import Auth

# --- Config from env ---
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY_EMBED")  # Use OpenAI for both LLM and embeddings
EMBED_API_KEY   = os.getenv("OPENAI_API_KEY_EMBED")
WEAVIATE_URL    = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

# Early validation
assert OPENAI_API_KEY, "OPENAI_API_KEY_EMBED is empty or not set!"
assert EMBED_API_KEY, "OPENAI_API_KEY_EMBED is empty or not set!"
assert WEAVIATE_URL, "WEAVIATE_URL is empty or not set!"
assert WEAVIATE_API_KEY, "WEAVIATE_API_KEY is empty or not set!"

# --- LLM via OpenAI (explicit base_url) ---
Settings.llm = LlamaOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    base_url="https://api.openai.com/v1",  # Explicit to avoid env leakage
    temperature=0.1,
    timeout=60,
)

# --- Embeddings (OpenAI official) ---
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_key=EMBED_API_KEY,
    api_base="https://api.openai.com/v1",
)

# --- Weaviate vector store ---
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
)
vector_store = WeaviateVectorStore(
    weaviate_client=client,
    index_name="PolicyDocs",
    text_key="text",
)

# Rebuild index handle from existing Weaviate data
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
retriever = index.as_retriever(similarity_top_k=4)
engine: RetrieverQueryEngine = RetrieverQueryEngine.from_args(retriever)

# --- UI ---
st.set_page_config(page_title="Policy Q&A Copilot", page_icon="🧭")
st.title("🧭 Policy Q&A Copilot")

prompt = st.chat_input("Ask about PTO, parental leave, devices, travel, etc.")
if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)

if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            resp = engine.query(prompt)
            # Show answer
            st.markdown(resp.response)

            # Show sources
            if resp.source_nodes:
                with st.expander("Sources"):
                    for i, sn in enumerate(resp.source_nodes, start=1):
                        st.markdown(f"**[{i}]** …{sn.text[:300]}…")

        st.session_state.history.append(("assistant", resp.response))
    st.rerun()

