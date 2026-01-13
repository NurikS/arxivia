from .arxiv_client import ArxivClient
from .llm_client import LLMClient

class ResearchEngine:
    def __init__(self):
        self.arxiv = ArxivClient()
        try:
            self.llm = LLMClient()
        except ValueError as e:
            print(f"Warning: {e}. LLM features will be disabled.")
            self.llm = None

    def research(self, query: str):
        print(f"Searching Arxiv for: {query}...")
        papers = self.arxiv.search_papers(query)
        
        if not papers:
            return "No relevant papers found.", []

        if not self.llm:
             # Fallback if no API key
            return "LLM not initialized (missing API key). Here are the papers found.", papers

        print("Generating answer from LLM...")
        answer = self.llm.generate_answer(query, papers)
        
        return answer, papers
