from src.engine import ResearchEngine
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    console = Console()
    console.rule("[bold blue]Arxivia Research Engine[/]")
    
    if not os.getenv("OPENAI_API_KEY"):
         console.print("[yellow]Warning: OPENAI_API_KEY not found in environment. LLM generation might fail.[/]")

    engine = ResearchEngine()
    
    while True:
        query = console.input("\n[bold green]Ask a question (or 'exit'):[/] ")
        if query.lower() in ["exit", "quit"]:
            break
            
        try:
            answer, papers = engine.research(query)
            
            console.rule("[bold]Answer[/]")
            console.print(Markdown(answer))
            
            console.rule("[bold]References[/]")
            for i, paper in enumerate(papers, 1):
                console.print(f"[{i}] [link={paper['url']}]{paper['title']}[/link] ({paper['published'].year})")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {e}")

if __name__ == "__main__":
    main()
