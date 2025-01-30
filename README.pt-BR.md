🌍 [Read in English](README.md)

# My Energy

Aplicação web em python com `streamlit` para melhorar a questão da `green energy`, integrado com api desenvolvido em `djando ` and `django-ninja` .

## Technologies Used

- `Streamlit` - Desenvolvimento da interface.
- `requests` - Realizar requisições para a api.
- `Oracle Database` - Banco de Dados.

## API Features

The API offers a number of features for handling and managing data. Some of the main features include:

- Creation of new records in the database.
- Querying existing data through filters and parameters.
- Update of specific records.
- Deletion of data.

## Passos para execução e instalação da api

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Entre no diretório:

```bash
cd my-energy-api
```

3. Crie um Ambiente Virtual:

```bash
python -m venv .venv
```

4. Ative o `Ambiente Virtual` executando o arquivo `.bat` localizado em `.venv/Scripts/Activate.bat`.

5. Instale as dependências :

```bash
pip install - r requirements.txt
```

6. Configure o banco de dados e migrações:

```bash
python ./src/manage.py
```

7. Execute o servidor:

```bash
python ./src/manage.py runserver
```

8; Acesse a API en:

- http://localhost:8000/api

## Steps to run and install the Front-end

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy.git
```

2. Entre no diretório:

```bash
cd my-energy-api
```

3. Crie um Ambiente Virtual:

```bash
python -m venv .venv
```

4. Ative o `Ambiente Virtual` executando o arquivo `.bat` localizado em `.venv/Scripts/Activate.bat`.

5. Instale as dependências :

```bash
pip install - r requirements.txt
```

6. Execute a aplicação:

```bash
streamlit run ./app/app.py
```

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
