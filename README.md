# Desafio de projeto -- Otimizar o Sistema Bancário

## Objetivo geral
Neste desafio, pude otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo era aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Pude refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.

Este projeto é parte do bootcamp da DIO **Potência Tech powered by iFood | Ciência de Dados** e me possibilitou aplicar os conceitos avançados de programação e demonstrar alguma habilidade de criar soluções mais elegantes e eficientes utilizando Python.


[Repo da V1 do projeto](https://github.com/Rafa-Ol-Dev/sistema_bancario)

---
## Desafio
- Deixar o código mais modularizadoutilizando funções para as operações já existentes: sacar, depositar e visualizar histórico;
- Além disso, para a versão 2 do sistema, criei duas novas funções: *Novo Cliente* e *Nova Conta* (esta última vinculada com o cliente).

## Separação em funções
- Criar funções para todas as operações do sistema;
- Respeitar uma regra na passagem de argumentos para cada função;
- O retorno e nome foram definidos a meu gosto.

## Saque
- A função saque recebeu os argumentos apenas por nome (*keyword only*);
- Argumentos: **saldo, valor, extrato, limite, numero_saques, limite_saque**;
- Retorno: *saldo e extrato*.

## Depósito
- A função depósito recebeu os argumentos apenas por posição;
- Argumentos: **saldo, valor, extrato**;
- Retorno: *saldo e extrato*.

## Extrato
- A função extrato recebeu os argumentos por posição e nome (*positional only e keyword only*);
- Argumentos posicionais: **saldo**;
- Argumentos nomeados: *extrato*.

## Novas funções
- Foram implementadas duas novas funções: *Novo Cliente* e *Nova Conta*;
- Nesse primeiro momento, não há vínculo entre o cliente e as movimentações feitas na conta, elas independem da criação de um cliente e/ou conta.

  ### Novo Cliente
  - O programa armazena os clientes em uma lista;
  - Um cliente é composto por: *nome, data de nascimento, CPF e endereço*;
  - O endereço é uma string com o seguinte formato: *logradouro, num - bairro - cidade/sigla estado*;
  - Apenas os números do CPF são armazenados. Não é possível cadastrar dois clientes com o mesmo CPF.

  ### Criar conta corrente
  - O programa armazena as contas em uma lista;
  - Uma conta é composta por: *agência, número da conta e cliente*;
  - O número da conta é sequencial, iniciando em 1;
  - O número da agência é fixo, *string* "0001";
  - Um cliente pode ter mais de uma conta, mas uma conta pertence a apenas um único cliente.


---
##### 💻 Feito por Rafael Oliveira, 2023.