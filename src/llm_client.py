from openai import OpenAI
import os

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        self.client = OpenAI(api_key=self.api_key)

    def generate_answer(self, query: str, context: list[dict]) -> str:
        """
        Generates an answer based on the provided context (papers).
        """
        
        system_prompt = """You are a helpful research assistant. 
        You answer questions based on the provided academic papers.
        Always cite your sources using [1], [2], etc., corresponding to the paper numbers in the context.
        If the answer is not in the context, say so.
        """
        
        context_str = ""
        for i, paper in enumerate(context, 1):
            context_str += f"[{i}] Title: {paper['title']}\nAbstract: {paper['summary']}\n\n"

        user_prompt = f"Question: {query}\n\nContext:\n{context_str}\n\nAnswer:"

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        return response.choices[0].message.content
