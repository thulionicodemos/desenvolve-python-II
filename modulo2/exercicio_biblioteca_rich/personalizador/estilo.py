from rich.console import Console

console = Console()

def formata_estilo(texto: str, isArquivo: bool = False) -> None:
    """
    Aplica estilos ao texto usando rich.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    console.print(f"[bold red on yellow]{texto}[/bold red on yellow]")

def estilo_avancado(texto: str, isArquivo: bool = False) -> None:
    """
    Estilo avançado com mais formatações.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    console.print(f"[italic underline blue]{texto}[/italic underline blue]", style="on black")