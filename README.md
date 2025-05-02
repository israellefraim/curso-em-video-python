# 🐍 Curso Básico Python
Aulas e Exercícios do Mundo I, II e III do Curso em Vídeo Python.

Ótimo ponto! Vamos refazer de forma **completa, mais clara e detalhada**, explicando **não só os formatos (snake_case, etc.)**, mas **também boas práticas de nomes** — como o uso de **verbos em funções**, **nomes significativos**, e estrutura de projeto.

---

<details><summary>
  
  ### **CONVENÇÕES DE NOMEAÇÃO PYTHON (com boas práticas)**
  
  </summary>

Python segue o **PEP 8** como guia oficial de estilo de código. Abaixo, está o padrão para **variáveis, funções, classes, arquivos, pastas e constantes**, incluindo **dicas semânticas (como usar verbos)**.

### 1. 🟩 **Variáveis**
- **Formato**: `snake_case` (letras minúsculas com underscore)
- **Boa prática**: nomes curtos, mas **descritivos**
- **Evitar**: nomes genéricos como `data`, `info`, `temp`, exceto em casos claros

**✅ Exemplos bons**:
```python
user_name = "Alice"
total_price = 49.90
is_logged_in = True
```

**❌ Exemplos ruins**:
```python
x = "Alice"        # genérico demais
price = 49.90      # OK, mas pode ser mais específico
```

---

### 2. 🟦 **Funções**
- **Formato**: `snake_case`
- **Boa prática**:
  - **Usar verbos** no início → a função executa uma ação
  - Nome descritivo do que ela faz
  - Curto, mas claro

**✅ Exemplos bons**:
```python
send_email()
get_user_by_id()
calculate_total_price()
validate_password()
```

**❌ Exemplos ruins**:
```python
email()      # o quê?
calc()       # calcular o quê?
check()      # checar o quê?
```

---

### 3. 🟨 **Classes**
- **Formato**: `PascalCase` (cada palavra começa com maiúscula)
- **Boa prática**: nome de **substantivo**, representando **entidade ou conceito**

**✅ Exemplos bons**:
```python
User
Product
EmailSender
OrderController
```

**❌ Exemplos ruins**:
```python
user_class
getuser
ClassUser
```

---

### 4. 🟥 **Constantes**
- **Formato**: `ALL_UPPER_CASE` com underscores
- **Usadas** para valores fixos, configurações, etc.

**✅ Exemplos**:
```python
PI = 3.14159
MAX_CONNECTIONS = 10
DATABASE_URL = "localhost"
```

---

### 5. 🟪 **Arquivos (.py)**
- **Formato**: `snake_case`
- **Boa prática**: nome claro e descritivo do conteúdo do arquivo

**✅ Exemplos**:
```plaintext
user_model.py
auth_service.py
order_utils.py
```

**❌ Exemplos ruins**:
```plaintext
UserModel.py      # PascalCase errado
modelUser.py      # invertido e confuso
mainFile.py       # muito genérico
```

---

### 6. 🟫 **Pastas (Pacotes Python)**
- **Formato**: `snake_case`
- **Boa prática**: agrupar por domínio de responsabilidade

**✅ Exemplos**:
```plaintext
models/
controllers/
services/
utils/
```

---

### 7. ⚫ **Métodos e Funções Privadas**
- **Formato**: `snake_case`, com prefixo `_`
- **Indicam que são internos, não devem ser usados fora da classe/módulo**

**Exemplo**:
```python
def _connect_to_database():
    pass
```

---

### 8. ⚪ **Métodos Especiais (Dunder Methods)**
- Começam e terminam com **dois underlines (`__`)**
- Usados pelo próprio Python

**Exemplos**:
```python
__init__()     # construtor da classe
__str__()      # representação como string
__len__()      # usado por len(obj)
```

---

## 🧱 Estrutura de Projeto Python Exemplo (Mini App)

```
meu_projeto/
├── main.py
├── config.py
├── models/
│   └── user_model.py
├── services/
│   └── auth_service.py
├── controllers/
│   └── user_controller.py
├── utils/
│   └── email_utils.py
```

---

## ✅ RESUMO FINAL

| Elemento         | Formato         | Boa prática                                                                  |
|------------------|------------------|-----------------------------------------------------------------------------|
| Variável         | `snake_case`     | Nome curto, mas claro (substantivo ou adjetivo)                             |
| Função           | `snake_case`     | Usar verbo no início + descrever a ação                                     |
| Classe           | `PascalCase`     | Substantivo, nome de entidade ou conceito                                   |
| Constante        | `ALL_UPPER_CASE` | Valores fixos e imutáveis                                                   |
| Arquivo .py      | `snake_case`     | Nome simples e descritivo                                                   |
| Pasta            | `snake_case`     | Nome de domínio funcional (ex: services, models)                            |
| Método privado   | `_nome()`        | Prefixo `_` indica uso interno                                              |
| Método especial  | `__nome__()`     | Dunder methods: métodos especiais do Python                                 |
</details>

<details><summary>
  
  ### **COMANDOS (functions, statemants, keywords, data types, etc.)**
  
  </summary>
<br>  

| COMANDO                                | DESCRIÇÃO                                                |
| -------------------------------------- | -------------------------------------------------------- |
| `print()`                              | Exibe valores na saída padrão                            |
| `input()`                              | Lê texto digitado pelo usuário                           |
| `len()`                                | Retorna o tamanho (nº de itens) de sequências e coleções |
| `type()`                               | Informa o tipo de um objeto                              |
| `int()`, `float()`, `str()`            | Convertem valores para inteiro, ponto flutuante e string |
| `list()`, `dict()`, `tuple()`, `set()` | Criam lista, dicionário, tupla e conjunto                |
| `range()`                              | Gera sequências de números                               |
| `open()`                               | Abre arquivo para leitura/escrita                        |
| `import`                               | Importa módulos e pacotes                                |
| `def`                                  | Declara função                                           |
| `class`                                | Declara classe                                           |
| `if` / `elif` / `else`                 | Estruturas de condição                                   |
| `for`                                  | Laço de repetição sobre iteráveis                        |
| `while`                                | Laço de repetição baseado em condição                    |
| `break`                                | Interrompe um laço                                       |
| `continue`                             | Pula para a próxima iteração do laço                     |
| `try` / `except` / `finally`           | Tratamento de exceções                                   |
| `with`                                 | Gerencia contexto (por exemplo, arquivos)                |
| `lambda`                               | Função anônima de expressão única                        |
| `map()`                                | Aplica função a cada item de um iterável                 |
| `filter()`                             | Filtra itens de um iterável por uma função condicional   |
| `enumerate()`                          | Itera e retorna par (índice, valor)                      |
| `zip()`                                | Agrupa iteráveis em tuplas                               |
| `sorted()`                             | Retorna nova lista ordenada                              |
| `reversed()`                           | Retorna iterador invertido                               |
| `sum()`                                | Soma itens de um iterável                                |
| `min()`, `max()`                       | Encontram valor mínimo e máximo                          |
| `abs()`                                | Valor absoluto                                           |
| `isinstance()`                         | Verifica o tipo de objeto                                |
| `help()`                               | Exibe documentação de objetos                            |
| `dir()`                                | Lista atributos e métodos de um objeto                   |

</details>
