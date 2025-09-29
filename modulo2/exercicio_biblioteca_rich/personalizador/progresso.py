import time
from rich.console import Console
from rich.progress import track

console = Console()

def formata_progresso(texto: str, isArquivo: bool = False) -> None:
    """
    Simula progresso enquanto processa o texto.
    
    :param texto: String com o texto ou caminho do arquivo (ignorado no progresso, mas impresso no final).
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    for _ in track(range(10), description="Processando texto..."):
        time.sleep(0.5)  # Simula processamento
    console.print(f"[green]Processo concluído:[/green] {texto}")

def progresso_detalhado(texto: str, isArquivo: bool = False) -> None:
    """
    Progresso detalhado com mais passos.
    
    :param texto: String com o texto ou caminho do arquivo.
    :param isArquivo: Se True, 'texto' é tratado como caminho de arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    
    for _ in track(range(20), description="Processamento detalhado..."):
        time.sleep(0.3)
    console.print(f"[bold green]Detalhes processados:[/bold green] {texto}")