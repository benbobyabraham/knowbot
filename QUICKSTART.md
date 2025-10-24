# Quick Start Guide

Get Knowbot up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- A Weaviate Cloud account ([Sign up here](https://console.weaviate.cloud/))

## Step 1: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/knowbot.git
cd knowbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
# Add your OpenAI API key and Weaviate credentials
```

Your `.env` should look like:
```env
OPENAI_API_KEY_EMBED=sk-proj-...
WEAVIATE_URL=your-cluster.weaviate.cloud
WEAVIATE_API_KEY=your-weaviate-key
```

## Step 3: Ingest Documents

```bash
# Add your policy documents to the data/ folder
# Then run the ingestion script
python src/ingestion.py
```

## Step 4: Launch the App

```bash
streamlit run src/app.py
```

The app will open at `http://localhost:8501`

## Try It Out!

Ask questions like:
- "What is the PTO policy?"
- "How many days of parental leave do I get?"
- "What are the laptop usage guidelines?"

## Need Help?

- Check the [README](README.md) for detailed documentation
- See [CONTRIBUTING](CONTRIBUTING.md) for development guidelines
- Open an issue if you encounter problems

Happy querying! 🚀
