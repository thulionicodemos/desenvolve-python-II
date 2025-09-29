from rich.console import Console
from rich.layout import Layout

console = Console()

def formata_layout(texto: str, isArquivo: bool = False) -> None:
    """
    Formata o texto usando layout do rich.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    layout = Layout()
    layout.split_column(Layout(name="upper"), Layout(name="lower"))
    layout["upper"].update(texto)
    layout["lower"].update("Exemplo de layout inferior.")
    console.print(layout)

def layout_simples(texto: str, isArquivo: bool = False) -> None:
    """
    Uma versão simples de formatação de layout.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    console.print(f"[bold]Layout Simples:[/bold] {texto}")