from rich.console import Console


console = Console()


def success(message: str) -> None:
    """
    Exibe uma mensagem de sucesso no console.

    Args:
        message: Mensagem que será exibida.
    """

    console.print(f"[bold green]✓ {message}[/bold green]")


def info(message: str) -> None:
    """
    Exibe uma mensagem informativa no console.

    Args:
        message: Mensagem que será exibida.
    """

    console.print(f"[cyan]ℹ {message}[/cyan]")


def warning(message: str) -> None:
    """
    Exibe uma mensagem de aviso no console.

    Args:
        message: Mensagem que será exibida.
    """

    console.print(f"[yellow]⚠ {message}[/yellow]")


def error(message: str) -> None:
    """
    Exibe uma mensagem de erro no console.

    Args:
        message: Mensagem que será exibida.
    """

    console.print(f"[bold red]✗ {message}[/bold red]")


def title(message: str) -> None:
    """
    Exibe um título formatado no console.

    Args:
        message: Título que será exibido.
    """

    console.rule(f"[bold blue]{message}[/bold blue]")