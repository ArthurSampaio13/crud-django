# Projeto CRUD com Django

Este projeto é uma aplicação web desenvolvida com o framework Django, implementando operações CRUD (Create, Read, Update, Delete) para gerenciar [especificar o tipo de dados, por exemplo, "informações de funcionários"].

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Arquitetura do Projeto](#arquitetura-do-projeto)

## Funcionalidades

- **Criar**: Adicionar novos registros ao sistema.
- **Ler**: Visualizar uma lista de registros existentes ou detalhes de um registro específico.
- **Atualizar**: Editar informações de registros existentes.
- **Deletar**: Remover registros do sistema.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework**: Django 3.x
- **Banco de Dados**: SQLite 
- **Front-end**: HTML, CSS, JavaScript 

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/ArthurSampaio13/crud-django.git
   cd crud-django
   ```

2. **Instale as dependências**:

   ```bash
   poetry install
   ```

3. **Configure o banco de dados**:

   - Edite o arquivo `settings.py` para configurar o banco de dados conforme sua preferência.
   - Aplique as migrações:

     ```bash
     python manage.py migrate
     ```

4. **Execute o servidor de desenvolvimento**:

   ```bash
   task dev
   ```

6. **Acesse a aplicação**:

   - Abra o navegador e vá para `http://localhost:8000/`.

## Arquitetura do Projeto

O projeto segue a estrutura padrão do Django, organizada da seguinte forma:

```
└── crud-django/
    ├── manage.py
    ├── pyproject.toml
    ├── crudDjango/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── livraria/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── migrations/
        │   ├── 0001_initial.py
        │   ├── 0002_alter_book_created_at.py
        │   └── __init__.py
        └── templates/
            ├── add_book.html
            ├── base.html
            ├── book.html
            ├── home.html
            ├── navbar.html
            ├── register.html
            └── update_book.html

```


