import os, glob
from dotenv import load_dotenv
load_dotenv()

from llama_index.core import (
    SimpleDirectoryReader, VectorStoreIndex, StorageContext, Settings
)
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.weaviate import WeaviateVectorStore
import weaviate
from weaviate.classes.init import Auth

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
EMBED_API_KEY = os.getenv("OPENAI_API_KEY_EMBED")

def main():
    # 1) Reader
    docs = SimpleDirectoryReader("data", recursive=True).load_data()
    print("\n\n\n\n",docs,"\n\n\n\n")

    # 2) Embeddings (fast & tiny) - use real OpenAI, not Friendli
    Settings.embed_model = OpenAIEmbedding(
        model="text-embedding-3-small",
        api_key=EMBED_API_KEY,
        api_base="https://api.openai.com/v1",
    )

    # 3) Weaviate client & vector store (Cloud)
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
    )
    
    try:
        # Create vector store with a simple class name
        vector_store = WeaviateVectorStore(
            weaviate_client=client,
            index_name="PolicyDocs",
            text_key="text",
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # 4) Build the index (LLamaIndex handles chunking + upsert)
        index = VectorStoreIndex.from_documents(
            docs, storage_context=storage_context
        )

        print("✅ Ingestion complete. Indexed docs in Weaviate.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
