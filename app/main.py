# app/main.py

from conta import ContaBancaria
import textwrap

def menu() -> str:
    """
    Exibe o menu de opções e captura a escolha do usuário.

    :return: A opção escolhida pelo usuário.
    """
    menu_texto = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    # Usa textwrap.dedent para remover a indentação do texto multilinha
    return input(textwrap.dedent(menu_texto))

def main() -> None:
    """
    Função principal que gerencia o fluxo da aplicação bancária.
    """
    # Instancia a conta bancária, o objeto principal da nossa POO.
    conta = ContaBancaria()

    while True:
        opcao = menu()

        if opcao == "d":
            print("\n--- DEPÓSITO ---")
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("\n❌ Valor inválido. Por favor, digite um número.")

        elif opcao == "s":
            print("\n--- SAQUE ---")
            try:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            except ValueError:
                print("\n❌ Valor inválido. Por favor, digite um número.")

        elif opcao == "e":
            conta.mostrar_extrato()

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema! Volte sempre.")
            break

        else:
            print("\n❌ Operação inválida, por favor selecione novamente a opção desejada.")

# Ponto de entrada padrão para a execução do script
if __name__ == "__main__":
    main()
