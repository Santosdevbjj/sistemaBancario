# app/conta.py

from typing import List, Dict, Union
import textwrap

# Constantes de Negócio
LIMITE_SAQUES_DIARIOS = 3
LIMITE_VALOR_SAQUE = 500.00
FORMATO_MOEDA = "R$ {:.2f}" # Formato para exibição de valores monetários

class ContaBancaria:
    """
    Representa uma conta bancária simples com operações de depósito, saque e extrato.

    A conta implementa as regras de negócio:
    - Depósitos devem ser valores positivos.
    - Saques têm limite diário (3) e de valor (R$ 500,00 por saque).
    - Todas as transações são registradas no extrato.
    """
    def __init__(self, saldo_inicial: float = 0.0) -> None:
        """
        Inicializa a conta bancária.

        :param saldo_inicial: O saldo inicial da conta (padrão é 0.0).
        """
        self._saldo = saldo_inicial
        # O extrato armazena uma lista de dicionários, cada um com 'tipo' e 'valor'.
        self._extrato: List[Dict[str, Union[str, float]]] = []
        self._saques_hoje = 0

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual da conta."""
        return self._saldo

    @property
    def extrato(self) -> List[Dict[str, Union[str, float]]]:
        """Retorna a lista de transações registradas."""
        return self._extrato

    @property
    def saques_hoje(self) -> int:
        """Retorna o número de saques realizados hoje."""
        return self._saques_hoje

    def depositar(self, valor: float) -> bool:
        """
        Realiza um depósito na conta.

        :param valor: O valor a ser depositado.
        :return: True se o depósito foi bem-sucedido, False caso contrário.
        """
        if valor > 0:
            self._saldo += valor
            self._extrato.append({"tipo": "DEPÓSITO", "valor": valor})
            print(f"\n✅ Depósito de {FORMATO_MOEDA.format(valor)} realizado com sucesso.")
            return True
        else:
            print("\n❌ Operação falhou! O valor do depósito deve ser positivo.")
            return False

    def sacar(self, valor: float) -> bool:
        """
        Realiza um saque na conta, respeitando os limites diários e de saldo.

        :param valor: O valor a ser sacado.
        :return: True se o saque foi bem-sucedido, False caso contrário.
        """
        if self._saques_hoje >= LIMITE_SAQUES_DIARIOS:
            print(f"\n❌ Operação falhou! Limite de {LIMITE_SAQUES_DIARIOS} saques diários atingido.")
            return False

        if valor > LIMITE_VALOR_SAQUE:
            print(f"\n❌ Operação falhou! O limite máximo por saque é de {FORMATO_MOEDA.format(LIMITE_VALOR_SAQUE)}.")
            return False

        if valor <= 0:
            print("\n❌ Operação falhou! O valor do saque deve ser positivo.")
            return False

        if valor > self._saldo:
            print("\n❌ Operação falhou! Você não tem saldo suficiente.")
            return False

        # Se todas as verificações passarem, realiza o saque
        self._saldo -= valor
        self._extrato.append({"tipo": "SAQUE", "valor": valor})
        self._saques_hoje += 1
        print(f"\n✅ Saque de {FORMATO_MOEDA.format(valor)} realizado com sucesso.")
        return True

    def mostrar_extrato(self) -> None:
        """
        Exibe o extrato de todas as transações (depósitos e saques) e o saldo atual.
        """
        print("\n================ EXTRATO ================")
        if not self._extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self._extrato:
                tipo = transacao["tipo"]
                valor = transacao["valor"]
                # Saques são exibidos como negativos
                valor_formatado = FORMATO_MOEDA.format(-valor) if tipo == "SAQUE" else FORMATO_MOEDA.format(valor)
                print(f"{tipo:<10}: {valor_formatado:>15}")

        print(f"\nSaldo Atual: {FORMATO_MOEDA.format(self._saldo)}")
        print("=========================================")
