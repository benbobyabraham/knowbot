import os
from dotenv import load_dotenv
load_dotenv()

# CRITICAL: Unset the Friendli base URL to prevent SDK from using it
if "OPENAI_API_BASE" in os.environ:
    del os.environ["OPENAI_API_BASE"]

from llama_index.core import VectorStoreIndex, Document
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings

# 1. Set up the LLM and embedding models
Settings.llm = LlamaOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY_EMBED"),  # Use the working OpenAI key
    base_url="https://api.openai.com/v1",
    temperature=0.1
)

Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY_EMBED"),
    api_base="https://api.openai.com/v1",
)

# 2. Create some fake documents for testing
docs = [
    Document(text="Employees receive 15 days of paid time off (PTO) per year."),
    Document(text="Parental leave includes 12 weeks of paid leave."),
    Document(text="Laptop refresh cycles occur every 3 years for full-time employees."),
]

# 3. Build an in-memory index
index = VectorStoreIndex.from_documents(docs)

# 4. Create a retriever from the index
retriever = index.as_retriever(similarity_top_k=2)

# 5. Build the RetrieverQueryEngine
engine = RetrieverQueryEngine.from_args(retriever)

# 6. Run a test query
query = "How many weeks of parental leave do employees get?"
response = engine.query(query)

# 7. Print results
print("Query:", query)
print("Answer:", response.response)

print("\nSources:")
for i, node in enumerate(response.source_nodes, start=1):
    print(f"[{i}] {node.text.strip()}")
