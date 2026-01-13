# Arxivia

Arxivia is a Perplexity-style answering engine focused on AI research papers. It queries the Arxiv API for relevant papers and uses OpenAI's GPT-4 to generate synthesized answers with citations.

## Features

- **Smart Search**: Queries Arxiv to find the most relevant papers for your question.
- **RAG Engine**: Retrieves paper abstracts and constructs a context for the LLM.
- **Citations**: Generates answers with strict referencing (e.g., `[1]`, `[2]`).
- **CLI Interface**: Clean and interactive command-line interface built with `rich`.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd arxivia
   ```

2. **Set up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**:
   Copy the example environment file and add your OpenAI API key.
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```env
   OPENAI_API_KEY=sk-your-api-key
   ```

## Usage

Run the main application:

```bash
python main.py
```

Then simply type your question when prompted.

### Example

```text
Ask a question: Explain LoRA adaptation

Searching Arxiv for: Explain LoRA adaptation...
Generating answer from LLM...

Answer
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique... [1]

References
[1] LoRA: Low-Rank Adaptation of Large Language Models
...
```

## Project Structure

- `src/arxiv_client.py`: Handles interaction with Arxiv API.
- `src/llm_client.py`: Handles interaction with OpenAI API.
- `src/engine.py`: Orchestrates the search and generation process.
- `main.py`: Entry point for the CLI.
