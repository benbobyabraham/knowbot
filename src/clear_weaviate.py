import os
from dotenv import load_dotenv
load_dotenv()

import weaviate
from weaviate.classes.init import Auth

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

def main():
    print("🗑️  Connecting to Weaviate Cloud...")
    
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
    )
    
    try:
        # Get all collections
        collections = client.collections.list_all()
        
        if not collections:
            print("✅ No collections found. Cluster is already empty.")
            return
        
        print(f"📋 Found {len(collections)} collection(s):")
        for collection_name in collections:
            print(f"   - {collection_name}")
        
        # Delete each collection
        for collection_name in collections:
            print(f"🗑️  Deleting collection: {collection_name}...")
            client.collections.delete(collection_name)
            print(f"   ✅ Deleted {collection_name}")
        
        print("\n✅ All data cleared from Weaviate cluster!")
        
    finally:
        client.close()

if __name__ == "__main__":
    main()
