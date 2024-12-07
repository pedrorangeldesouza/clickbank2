# ClickBank - Sistema Bancário Simples

Este é um sistema bancário simples desenvolvido em Python. Ele permite cadastrar novos usuários, abrir contas bancárias, realizar depósitos, saques e visualizar extratos. O código foi projetado para fornecer uma compreensão básica de como gerenciar contas e transações bancárias.

## Funcionalidades

- **Cadastro de Novo Usuário**: Permite cadastrar um novo usuário fornecendo informações como CPF, nome completo, data de nascimento, telefone e endereço.
- **Abrir Conta**: Ao cadastrar um usuário, é possível abrir uma conta bancária para o mesmo, atribuindo um número de conta e uma agência.
- **Depósito**: Permite realizar um depósito na conta bancária do usuário.
- **Saque**: Realiza o saque de uma conta bancária, respeitando um limite diário de saques.
- **Extrato**: Exibe o saldo atual da conta do usuário.
- **Limite de Saques Diários**: O sistema permite um número limitado de saques diários por conta.

## Como Usar

1. Clone o repositório para o seu computador.
    ```bash
    git clone https://github.com/seu-usuario/clickbank.git
    ```
2. Navegue até o diretório do projeto.
    ```bash
    cd clickbank
    ```
3. Execute o código em seu terminal ou editor Python.
    ```bash
    python clickbank.py
    ```
4. O programa estará em loop contínuo, aguardando que você escolha uma das opções disponíveis.

## Funcionalidades Detalhadas

### 1. **Novo Usuário**
   - O sistema solicita CPF, nome, data de nascimento, telefone e endereço do novo usuário.
   - O CPF é verificado para evitar duplicação de usuários.

### 2. **Abrir Conta**
   - A conta é criada apenas se o CPF informado já estiver cadastrado no sistema.
   - A conta recebe um número de conta único e é associada a uma agência (`0001`).

### 3. **Depósito**
   - Permite realizar um depósito, aumentando o saldo da conta.

### 4. **Saque**
   - Realiza um saque, respeitando:
     - O limite de R$ 500,00 por saque.
     - O limite de 3 saques diários por conta.
     - O saldo disponível na conta.

### 5. **Extrato**
   - Exibe o saldo atual da conta do usuário.

## Como Funciona

O programa gerencia usuários e contas de forma simples. Ele utiliza três listas principais:
- **`usuarios`**: Lista de dicionários contendo as informações de cada usuário.
- **`contas`**: Lista de dicionários contendo as informações das contas bancárias.
- **`enderecos`**: Lista separada para armazenar os endereços dos usuários (não utilizado no código final, pois está armazenado dentro do dicionário de `usuarios`).

### Limitações
- Não há persistência de dados, ou seja, os dados são perdidos quando o programa é encerrado.
- O programa é interativo e não possui uma interface gráfica.

## Melhorias Futuras

- **Persistência de Dados**: Salvar os dados dos usuários e contas em um arquivo ou banco de dados para manter as informações entre as execuções do programa.
- **Controle de Saques por Conta**: Implementar um controle mais detalhado de saques diários, permitindo múltiplas contas para o mesmo usuário.
- **Interface Gráfica**: Criar uma interface gráfica para facilitar a interação com o sistema.
- **Validações Adicionais**: Melhorar as validações de entrada (por exemplo, CPF válido, telefone, etc.).

## Contribuições

Contribuições são bem-vindas! Se você tiver melhorias ou sugestões, sinta-se à vontade para abrir um **issue** ou enviar um **pull request**.
