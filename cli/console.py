
from rich.console import Console

console = Console()


def success(message: str) -> None:
    console.print(f"[bold green]✓ {message}[/bold green]")


def info(message: str) -> None:
    console.print(f"[cyan]ℹ {message}[/cyan]")


def warning(message: str) -> None:
    console.print(f"[yellow]⚠ {message}[/yellow]")


def error(message: str) -> None:
    console.print(f"[bold red]✗ {message}[/bold red]")


def title(message: str) -> None:
    console.rule(f"[bold blue]{message}[/bold blue]")