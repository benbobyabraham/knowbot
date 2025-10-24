# Contributing to Knowbot

Thank you for your interest in contributing to Knowbot! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/knowbot.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes thoroughly
6. Commit your changes: `git commit -m "Add: description of your changes"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and configure your API keys

3. Run tests before submitting:
   ```bash
   python src/test_llm.py
   python src/test_retriever_query_engine.py
   ```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- Keep the first line under 50 characters
- Reference issues and pull requests when relevant

Examples:
- `Add: support for PDF document ingestion`
- `Fix: Weaviate connection timeout issue`
- `Update: improve error handling in ingestion pipeline`
- `Docs: add troubleshooting section to README`

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure all tests pass
3. Update documentation for any new features
4. Your PR will be reviewed by maintainers
5. Address any feedback from reviewers
6. Once approved, your PR will be merged

## Reporting Bugs

When reporting bugs, please include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

## Suggesting Enhancements

We welcome suggestions! Please include:
- A clear description of the enhancement
- Why this enhancement would be useful
- Possible implementation approach (if you have ideas)

## Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

Thank you for contributing to Knowbot! 🚀
