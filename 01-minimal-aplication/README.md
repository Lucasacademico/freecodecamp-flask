# Exemplo Básico de Aplicação Web com Flask

Este repositório contém um exemplo básico de uma aplicação web utilizando o **Flask**, um micro-framework popular para o desenvolvimento de aplicações web em **Python**. Vamos detalhar cada parte do código e como ele contribui para a criação dessa aplicação simples.

## Descrição

O Flask é um framework leve e flexível para a criação de aplicações web. Ele permite que você desenvolva aplicações de forma rápida e eficiente, com o mínimo de configuração. Neste exemplo, criaremos uma aplicação básica que responde com "Hello, World" quando acessada.

---

## Estrutura do Código

### 1. Importando a Classe Flask

A primeira linha do código importa a classe `Flask` do módulo `flask`. A classe `Flask` é a base para criar uma aplicação web com Flask.

```python
from flask import Flask
```

### 2. Criando uma Instância da Aplicação

Aqui, criamos uma instância da aplicação Flask, atribuindo-a à variável `app`. O argumento `__name__` é passado para o Flask para informar o nome do módulo atual, o que ajuda o Flask a localizar recursos relacionados, como templates e arquivos estáticos.

```python
app = Flask(__name__)
```

### 3. Definindo uma Rota (Endpoint)

Em Flask, usamos **decorators** para mapear URLs para funções Python. No caso da nossa aplicação, o decorator `@app.route('/')` define que a função `hello_world()` será chamada quando alguém acessar a rota raiz (`/`) do site.

- **Explicação**: O `@app.route('/')` mapeia a URL raiz (`/`) para a função `hello_world`, que retorna a string `"Hello, World"` como resposta.

```python
@app.route('/')
def hello_world():
    return "Hello, World"
```

### 4. Função de Visualização (View Function)

A função associada a uma rota em Flask é chamada de **view function**. No nosso caso, a função `hello_world()` gera a resposta que será exibida ao usuário quando ele acessar a URL especificada (`/`).

- **Explicação**: A linha `return "Hello, World"` envia a string `"Hello, World"` de volta ao navegador como resposta da página.

### 5. Rodando a Aplicação

Por fim, para rodar a aplicação, é necessário verificar se o script está sendo executado diretamente e chamar o método `run()` da instância `app`.

- **Explicação**: A verificação `if __name__ == '__main__'` garante que a aplicação será executada apenas quando o script for rodado diretamente (não quando importado). O parâmetro `debug=True` ativa o modo de depuração, permitindo que o servidor recarregue automaticamente quando houver mudanças no código.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

---

## Resumo do Código Completo

No final, você terá uma aplicação simples que mapeia uma rota para exibir "Hello, World" ao ser acessada.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Conclusão

Esse exemplo básico demonstra como é simples criar uma aplicação web com Flask. Ele apresenta os conceitos fundamentais, como criar rotas, associá-las a funções e rodar a aplicação com o servidor embutido do Flask.

Se você deseja expandir esta aplicação, pode adicionar novas rotas, templates HTML, manipulação de formulários e muito mais. O Flask é uma excelente escolha para aplicações web leves e escaláveis.
