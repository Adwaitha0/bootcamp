import sys
from . import hello

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else None
    msg = hello(name)  # e.g., "hello, Alice"

    console = Console()
    text = Text(msg, style="bold green")
    console.print(Panel.fit(text, title="adwaitha-hello", border_style="cyan"))

if __name__ == "__main__":
    main()
