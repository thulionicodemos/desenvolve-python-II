import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Interface para formatação de texto com rich usando módulos do pacote personalizador.")
    parser.add_argument("texto", help="Texto ou nome do arquivo que deseja imprimir formatado.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Ativa quando o argumento é o caminho para um arquivo.")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True,
                        help="Escolhe o módulo que a pessoa quer acessar (por nome ou por id).")
    parser.add_argument("-f", "--funcao", required=True,
                        help="Escolhe a função do módulo que quer acessar (por nome ou por id).")
    
    args = parser.parse_args()
    
    is_arquivo = args.arquivo
    
    if args.modulo == "layout":
        if args.funcao == "formata_layout":
            layout.formata_layout(args.texto, is_arquivo)
        elif args.funcao == "layout_simples":
            layout.layout_simples(args.texto, is_arquivo)
        else:
            print("Função inválida para o módulo layout.")
    elif args.modulo == "painel":
        if args.funcao == "formata_painel":
            painel.formata_painel(args.texto, is_arquivo)
        elif args.funcao == "painel_expandido":
            painel.painel_expandido(args.texto, is_arquivo)
        else:
            print("Função inválida para o módulo painel.")
    elif args.modulo == "progresso":
        if args.funcao == "formata_progresso":
            progresso.formata_progresso(args.texto, is_arquivo)
        elif args.funcao == "progresso_detalhado":
            progresso.progresso_detalhado(args.texto, is_arquivo)
        else:
            print("Função inválida para o módulo progresso.")
    elif args.modulo == "estilo":
        if args.funcao == "formata_estilo":
            estilo.formata_estilo(args.texto, is_arquivo)
        elif args.funcao == "estilo_avancado":
            estilo.estilo_avancado(args.texto, is_arquivo)
        else:
            print("Função inválida para o módulo estilo.")

if __name__ == "__main__":
    main()