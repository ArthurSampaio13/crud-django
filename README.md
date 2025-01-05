# Livraria App 📚

Uma aplicação web de gerenciamento de livros desenvolvida com Django. Este projeto oferece funcionalidades completas de autenticação, cadastro e gerenciamento de livros, incluindo criação, leitura, atualização e exclusão (CRUD).

## 🛠️ Funcionalidades

- **Autenticação de Usuário**:
  - Login, Logout e Registro.
  - Mensagens de feedback para ações bem-sucedidas ou erros.
  
- **Gerenciamento de Livros**:
  - Adicionar, visualizar, editar e excluir livros.
  - Visualizar lista completa de livros com detalhes.
  
- **Interface Responsiva**:
  - Design moderno utilizando Bootstrap.

---

## 💂️ Estrutura do Projeto

```
ArthurSampaio13-crud-django/
├── manage.py
├── pyproject.toml
├── crudDjango/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── livraria/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        ├── base.html
        ├── home.html
        ├── add_book.html
        ├── update_book.html
        └── book.html
```

---

## ⚙️ Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/ArthurSampaio13/crud-django.git
   cd crud-django
   ```

2. **Instale o Poetry** (se ainda não estiver instalado):
   ```bash
   pip install poetry
   ```

3. **Instale as dependências do projeto**:
   ```bash
   poetry install
   ```

4. **Ative o ambiente virtual do Poetry**:
   ```bash
   poetry shell
   ```

5. **Execute a aplicação** utilizando o Taskipy:
   ```bash
   task dev
   ```

---

## 🖥️ Uso

- **Página Inicial**: Exibe a lista de livros (requer autenticação).
- **Cadastro de Usuário**: Registre-se para acessar o sistema.
- **Adicionar Livro**: Crie novos registros de livros.
- **Editar Livro**: Atualize informações de livros existentes.
- **Excluir Livro**: Remova livros da lista.

---

## 📄 Estrutura das Tabelas

**Modelo Book**:
- `id`: Identificador único.
- `title`: Título do livro.
- `description`: Descrição do livro.
- `year`: Ano de publicação.
- `genre`: Gênero do livro.
- `value`: Preço do livro.

---

## 📊 Tecnologias Utilizadas

- **Back-end**: Django 5.1.4
- **Banco de Dados**: SQLite (padrão, pode ser alterado).
- **Front-end**: Bootstrap 5
- **Gerenciamento**: Poetry para dependências e Taskipy para automação de tarefas.

