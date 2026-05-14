![PythonDeveloper001](https://github.com/user-attachments/assets/ef0a2b7d-9a08-4c73-9f7d-60ff1bd0dc1f)

# 🏦 Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![POO](https://img.shields.io/badge/Paradigma-POO-orange)
![Plataforma](https://img.shields.io/badge/Plataforma-CLI-lightgrey)
![Bootcamp](https://img.shields.io/badge/Bootcamp-Suzano_Python_Developer_%232-purple)

> Protótipo funcional de sistema bancário em Python 3, com arquitetura orientada a objetos, regras de negócio encapsuladas e separação clara entre camada de domínio e interface de usuário — padrão replicável em APIs REST e microsserviços financeiros.

---

## 1. Problema de Negócio

Sistemas bancários sem controle programático de transações criam dois riscos operacionais diretos: **fraude por abuso de saques** e **inconsistência de estado financeiro** causada pela mistura de regras de negócio com lógica de apresentação.

O desafio técnico deste projeto é modelar um domínio bancário que:

- **Previna saques abusivos** via limite diário e teto por transação.
- **Garanta consistência de saldo** em todas as operações.
- **Registre rastreabilidade** de todas as movimentações em extrato auditável.
- **Isole regras de negócio** do canal de interação (CLI, futuramente API ou GUI).

---

## 2. Contexto

O projeto foi desenvolvido como desafio prático do **Bootcamp Suzano – Python Developer #2** (DIO), com objetivo de ir além do exercício procedural e implementar a solução com maturidade de código de produção.

O escopo replicou um subconjunto real de operações bancárias:

- Depósito com validação de valor positivo.
- Saque com duplo controle: limite de **3 saques diários** e teto de **R$ 500,00 por operação**.
- Extrato com histórico de transações e saldo atual formatado.

---

## 3. Premissas

- O saldo inicial é zero; não há simulação de contas pré-carregadas.
- O limite diário de saques é reiniciado apenas via nova instância da classe (sem persistência de data real nesta versão).
- Valores inválidos (negativos, zero, não numéricos) são rejeitados com mensagem de erro clara — nunca levantam exceção não tratada.
- O extrato é a fonte única de verdade sobre o histórico de transações.

---

## 4. Estratégia da Solução

A arquitetura foi planejada em duas camadas deliberadamente desacopladas:

**Camada de Domínio → `app/conta.py`**

A classe `ContaBancaria` encapsula todo o estado e comportamento bancário. Atributos são privados (`_saldo`, `_extrato`, `_saques_hoje`) e expostos apenas via `@property`, impedindo mutação externa não autorizada. As constantes de negócio (`LIMITE_SAQUES_DIARIOS`, `LIMITE_VALOR_SAQUE`) foram extraídas do corpo dos métodos para facilitar configuração sem alteração de lógica.

**Camada de Apresentação → `app/main.py`**

A função `main()` orquestra o fluxo do menu e delega toda lógica à camada de domínio. Entradas do usuário são capturadas com `try/except ValueError`, isolando a camada de domínio de erros de tipo.

**Fluxo de decisão por operação:**

```
Entrada do usuário
       │
       ▼
  Validação de tipo (main.py)
       │
       ▼
  Regras de negócio (conta.py)
  ├── Saque: limite diário → limite de valor → saldo suficiente
  └── Depósito: valor positivo
       │
       ▼
  Atualização de estado + registro no extrato
       │
       ▼
  Feedback ao usuário (✅ / ❌)
```

---

## 5. Decisões Técnicas e Trade-offs

**Por que POO e não código procedural?**

A versão procedural (sem classes) funciona para um único usuário. Com POO, cada instância de `ContaBancaria` representa uma conta independente — o mesmo código suporta múltiplas contas sem refatoração. É o pré-requisito arquitetural para evoluir para múltiplas contas, banco de dados e API REST.

**Por que CLI e não interface gráfica?**

Tkinter ou PyQt adicionariam complexidade de apresentação sem acrescentar valor à demonstração do domínio bancário. A interface CLI mantém o foco no que importa: a lógica de negócio. A separação já implementada entre `main.py` e `conta.py` permite substituir a CLI por FastAPI ou GraphQL sem tocar na camada de domínio.

**Por que type hints e docstrings em projeto de bootcamp?**

Porque código de portfólio é código lido por humanos, não só executado por máquinas. Type hints explicitam o contrato de cada método; docstrings documentam o comportamento esperado. São sinais de maturidade profissional, não exagero para o escopo.

**Trade-off aceito:** sem persistência. O estado é perdido ao encerrar o programa. A decisão foi deliberada — adicionar SQLite ou JSON nesta fase desviaria o foco do padrão arquitetural principal.

---

## 6. Estrutura do Projeto

```
sistema-bancario-em-python/
├── app/
│   ├── __init__.py        # Marca app/ como pacote Python
│   ├── conta.py           # Domínio: classe ContaBancaria (estado + regras)
│   └── main.py            # Apresentação: menu CLI e orquestração do fluxo
├── .gitignore
└── README.md
```

---

## 7. Diagrama UML — Classe `ContaBancaria`

```
┌─────────────────────────────────────────────────┐
│                  ContaBancaria                  │
├─────────────────────────────────────────────────┤
│ - _saldo : float                                │
│ - _extrato : List[Dict[str, Union[str, float]]] │
│ - _saques_hoje : int                            │
├─────────────────────────────────────────────────┤
│ + saldo (property) : float                      │
│ + extrato (property) : List                     │
│ + saques_hoje (property) : int                  │
│ + depositar(valor: float) : bool                │
│ + sacar(valor: float) : bool                    │
│ + mostrar_extrato() : None                      │
└─────────────────────────────────────────────────┘
```

Atributos privados com `@property` garantem encapsulamento: o saldo não pode ser alterado externamente sem passar pelas validações do método `depositar()` ou `sacar()`.

---

## 8. Como Executar

**Pré-requisitos:** Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/Santosdevbjj/sistema-bancario-em-python.git

# 2. Acesse a pasta da aplicação
cd sistema-bancario-em-python/app

# 3. Execute
python main.py
```

O sistema exibirá um menu interativo com as opções `[d] Depositar`, `[s] Sacar`, `[e] Extrato` e `[q] Sair`.

---

## 9. Exemplo de Uso

<img width="854" height="582" alt="Exemplo de uso do sistema bancário em Python" src="https://github.com/user-attachments/assets/5e488bc8-c7d9-4433-b035-e31bfcc7da69" />

---

## 10. Resultados e Aprendizados

**O que funcionou bem:**

A separação entre `conta.py` (domínio) e `main.py` (apresentação) se mostrou a decisão mais valiosa do projeto. Quando foi necessário adicionar validação de `ValueError` na entrada do usuário, a camada de domínio não precisou ser tocada — exatamente o comportamento esperado de código bem encapsulado.

**O que foi mais desafiador:**

Definir a responsabilidade exata de cada método. A tentação inicial era colocar o `print()` de erro dentro de `depositar()` e `sacar()` — o que misturaria domínio e apresentação. A decisão final de manter os prints dentro dos métodos de negócio foi um trade-off consciente: simplificou o protótipo, mas seria refatorado para retorno de objetos de resultado em uma versão de API.

**O que faria diferente hoje:**

Retornaria um objeto `OperationResult(success: bool, message: str)` em vez de `bool` com `print()` dentro dos métodos de domínio. Isso desacoplaria completamente a camada de domínio de qualquer canal de saída — pré-requisito para testes unitários limpos.

---

## 11. Próximos Passos

- [ ] Refatorar retorno dos métodos para `OperationResult` (desacopla domínio da apresentação)
- [ ] Adicionar suporte a múltiplas contas com dicionário de titulares
- [ ] Implementar persistência com SQLite ou arquivo JSON
- [ ] Expor operações via API REST com FastAPI
- [ ] Adicionar testes unitários com `pytest` cobrindo todos os fluxos de validação
- [ ] Containerizar com Docker para execução em ambiente isolado

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| POO / Encapsulamento | Padrão arquitetural do domínio |
| Type Hints (`typing`) | Contratos explícitos nos métodos |
| CLI (`textwrap`, `input`) | Interface de interação com o usuário |

---

## Autor

**Sérgio Santos**
Senior Data Engineer & Cloud Architect

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)
[![GitHub](https://img.shields.io/badge/GitHub-Santosdevbjj-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Santosdevbjj)

---

## Licença

Distribuído sob licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
