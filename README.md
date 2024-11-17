# My Energy

Aplicação web para melhorar a questão dos gastos com energia integrado com api desenvolvida em `django` e `django-ninja`.

## Tecnologias Utilizadas

Streamlit - Desenvolvimento da interface
request - Realizar requisições na api para manipulações no crud.
Oracle Database - Banco de dados padrão (pode ser alterado conforme necessidade)

## Funcionalidades da API

A API oferece uma série de funcionalidades para manipulação e gerenciamento de dados. Algumas das principais funcionalidades incluem:

- Criação de novos registros no banco de dados.
- Consulta de dados existentes por meio de filtros e parâmetros.
- Atualização de registros específicos.
- Exclusão de dados.

## Rode a Api

1. Clone o Repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Instale as Dependências :

```bash
pip install -r requirements.txt
```

3. Configure o Banco de Dados e Migrações:

```bash
python  ./src/manage.py migrate
```

4. Execute o Servidor:

```bash
python ./src/manage.py runserver
```

Acesse a API em http://localhost:8000/api.

## Instalação e Configuração

1. Clone o Repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy.git
```

2. Entre no diretorio:

```bash
cd my-energy
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode a aplicação:

```bash
streamlit run ./app/app.py
```

## Integrantes

- **Felipe** RM: 554547
- **Victor** RM: 555059
- **Jennie** RM: 554661
