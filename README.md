# Knowbot - Policy Q&A Copilot 🧭

An intelligent RAG (Retrieval-Augmented Generation) chatbot that helps users quickly find answers to policy-related questions using natural language. Built with LlamaIndex, Weaviate vector database, and OpenAI's GPT-4o-mini.

## Features

- **Natural Language Q&A**: Ask questions about company policies in plain English
- **Semantic Search**: Uses vector embeddings to find relevant policy information
- **Source Attribution**: Shows the exact policy excerpts used to generate answers
- **Real-time Responses**: Fast query processing with GPT-4o-mini
- **Streamlit UI**: Clean, intuitive chat interface
- **Weaviate Cloud Integration**: Scalable vector storage for policy documents

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector Database**: Weaviate Cloud
- **Framework**: LlamaIndex
- **Language**: Python 3.x

## Project Structure

```
knowbot/
├── src/
│   ├── app.py                          # Main Streamlit application
│   ├── ingestion.py                    # Document ingestion pipeline
│   ├── clear_weaviate.py               # Utility to clear vector store
│   ├── test_llm.py                     # LLM testing script
│   └── test_retriever_query_engine.py  # Retriever testing script
├── data/                                # Policy documents directory
│   ├── faculty_policy_manual.docx
│   ├── laptop_policy.txt
│   ├── parental_leave.md
│   └── pto.md
├── requirements.txt                     # Python dependencies
├── .env                                 # Environment variables (not in git)
└── README.md
```

## Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- Weaviate Cloud instance (or local Weaviate)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd knowbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   # OpenAI API Keys
   OPENAI_API_KEY_EMBED=your_openai_api_key_here
   
   # Weaviate Configuration
   WEAVIATE_URL=your_weaviate_cluster_url
   WEAVIATE_API_KEY=your_weaviate_api_key
   ```

## Usage

### 1. Ingest Policy Documents

First, add your policy documents to the `data/` directory. Supported formats include:
- `.txt` (plain text)
- `.md` (Markdown)
- `.docx` (Word documents)
- `.pdf` (PDF files)

Then run the ingestion script:

```bash
python src/ingestion.py
```

This will:
- Read all documents from the `data/` directory
- Generate embeddings using OpenAI's text-embedding-3-small
- Store vectors in Weaviate Cloud

### 2. Launch the Application

```bash
streamlit run src/app.py
```

The app will open in your browser at `http://localhost:8501`

### 3. Ask Questions

Example queries:
- "What is the PTO policy?"
- "How many days of parental leave do I get?"
- "What are the laptop usage guidelines?"
- "Can I work remotely?"

## Development

### Testing the LLM

```bash
python src/test_llm.py
```

### Testing the Retriever

```bash
python src/test_retriever_query_engine.py
```

### Clearing the Vector Store

To reset the Weaviate database:

```bash
python src/clear_weaviate.py
```

## Configuration

### LLM Settings

The application uses GPT-4o-mini with the following configuration:
- **Temperature**: 0.1 (for consistent, factual responses)
- **Timeout**: 60 seconds
- **Top-k Retrieval**: 4 most relevant chunks

### Embedding Model

- **Model**: text-embedding-3-small
- **Dimensions**: 1536
- **Provider**: OpenAI

## Troubleshooting

### Issue: "OPENAI_API_KEY_EMBED is empty or not set!"

**Solution**: Ensure your `.env` file contains a valid OpenAI API key:
```env
OPENAI_API_KEY_EMBED=sk-...
```

### Issue: Weaviate connection errors

**Solution**: 
1. Verify your Weaviate cluster URL doesn't include `https://`
2. Check that your Weaviate API key is valid
3. Ensure your Weaviate cluster is running

### Issue: No results returned

**Solution**: 
1. Verify documents were ingested successfully by running `python src/ingestion.py`
2. Check that the `PolicyDocs` collection exists in Weaviate
3. Try rephrasing your question

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built with [LlamaIndex](https://www.llamaindex.ai/)
- Powered by [OpenAI](https://openai.com/)
- Vector storage by [Weaviate](https://weaviate.io/)
- UI framework by [Streamlit](https://streamlit.io/)
