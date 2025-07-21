from rich.console import Console
from datetime import datetime

console = Console()

def log(msg, level="info"):
    ts = datetime.now().strftime("[%H:%M:%S]")
    if level == "error":
        console.print(f"{ts} [bold red]{msg}[/bold red]")
    elif level == "warn":
        console.print(f"{ts} [yellow]{msg}[/yellow]")
    else:
        console.print(f"{ts} {msg}")