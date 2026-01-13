import arxiv

class ArxivClient:
    def __init__(self):
        self.client = arxiv.Client()

    def search_papers(self, query: str, max_results: int = 5):
        """
        Searches Arxiv for papers related to the query.
        """
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        
        papers = []
        for result in self.client.results(search):
            papers.append({
                "title": result.title,
                "summary": result.summary,
                "url": result.entry_id,
                "published": result.published,
                "authors": [a.name for a in result.authors]
            })
        return papers
