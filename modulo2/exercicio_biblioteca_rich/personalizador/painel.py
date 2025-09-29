from rich.console import Console
from rich.panel import Panel

console = Console()

def formata_painel(texto: str, isArquivo: bool = False) -> None:
    """
    Formata o texto usando painel do rich.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    panel = Panel(texto, title="Painel Personalizado", border_style="bold blue")
    console.print(panel)

def painel_expandido(texto: str, isArquivo: bool = False) -> None:
    """
    Uma versão expandida de painel com mais opções.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    panel = Panel(texto, title="Painel Expandido", expand=True, border_style="green")
    console.print(panel)