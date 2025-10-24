import os, sys, json
from dotenv import load_dotenv

def ok(msg):  print(f"✅ {msg}")
def err(msg): print(f"❌ {msg}") or sys.exit(1)

load_dotenv()  # reads .env in project root

# -------- Friendli (LLM Inference) --------
def test_friendli():
    try:
        from openai import OpenAI
        base = os.getenv("OPENAI_API_BASE")
        key  = os.getenv("OPENAI_API_KEY")
        model = os.getenv("FRIENDLI_MODEL", "gpt-4o-mini-compatible")
        if not base or not key:
            err("Friendli: OPENAI_API_BASE / OPENAI_API_KEY missing")

        client = OpenAI(api_key=key, base_url=base)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role":"user","content":"Reply with the word OK only."}],
            temperature=0
        )
        text = resp.choices[0].message.content.strip()
        if text.upper() == "OK":
            ok(f"Friendli inference works (model={model})")
        else:
            err(f"Friendli responded but unexpected text: {text[:60]!r}")
    except Exception as e:
        err(f"Friendli error: {e}")

# -------- OpenAI (Embeddings) --------
def test_openai_embeddings():
    try:
        from openai import OpenAI
        embed_key = os.getenv("OPENAI_API_KEY_EMBED")
        if not embed_key:
            err("OpenAI embeddings: OPENAI_API_KEY_EMBED missing")

        client = OpenAI(api_key=embed_key)  # default OpenAI base
        out = client.embeddings.create(
            model="text-embedding-3-small",
            input="hello world"
        )
        vec = out.data[0].embedding
        if isinstance(vec, list) and len(vec) > 100:
            ok(f"OpenAI embeddings OK (dim={len(vec)})")
        else:
            err("Embeddings returned but vector looks wrong")
    except Exception as e:
        err(f"OpenAI embeddings error: {e}")

# -------- Weaviate (Connectivity) --------
def test_weaviate():
    try:
        import weaviate
        url = os.getenv("WEAVIATE_URL", "http://localhost:8080")
        client = weaviate.Client(url)
        if hasattr(client, "is_ready") and client.is_ready():
            ok(f"Weaviate reachable at {url}")
        else:
            # Fallback meta ping for older/newer clients
            try:
                meta = client.get_meta()
                if meta:
                    ok(f"Weaviate meta OK at {url}")
                else:
                    err("Weaviate responded but meta empty")
            except Exception as e:
                err(f"Weaviate not ready: {e}")
    except Exception as e:
        err(f"Weaviate import/connection error: {e}")

if __name__ == "__main__":
    print("Running smoke tests…")
    test_friendli()
    test_openai_embeddings()
    test_weaviate()
    print("\n🎉 All checks passed.")

