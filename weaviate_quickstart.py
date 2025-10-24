import os
import weaviate
from weaviate.classes.init import Auth

# Best practice: store your credentials in environment variables
# weaviate_url = os.environ["WEAVIATE_URL"]
# weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

weaviate_url ="lyaqpzqh8ybbcgzblha.c0.us-west3.gcp.weaviate.cloud"
weaviate_api_key ="ZVZLK1hFQ1g0M09VSkZrVl9PcXV1WkNZQWtIOVlLTVlDVStEQXZWaDJYUVRFWXFCSXRGeVpVYURCZUNBPV92MjAw"

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

print(client.is_ready())