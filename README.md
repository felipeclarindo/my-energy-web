🌍 [Leia em Português](README.pt-BR.md)

# My Energy

Web application in python using `streamlit` to improve the issue of energy spending integrated with api developed in `django` and `django-ninja`.

## Technologies Used

- `Streamlit` - Development of the interface.
- `requests` - Perform requests in api for manipulations in crud.
- `Oracle Database` - Standard database (can be changed as needed).

## API Features

The API offers a number of features for handling and managing data. Some of the main features include:

- Creation of new records in the database.
- Querying existing data through filters and parameters.
- Update of specific records.
- Deletion of data.

## Steps to run and install the api

1. Clone the Repository:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Enter directory:

```bash
cd my-energy-api
```

3. Create Virtual Environment:

```bash
python -m venv .venv
```

4. Activate the `Virtual Environment` running the `.bat` file in `.venv/Scripts/Activate.bat`.

5. Install dependencies :

```bash
pip install - r requirements.txt
```

6. Configure Database and Migrations:

```bash
python ./src/manage.py
```

7. Run Server:

```bash
python ./src/manage.py runserver
```

8. Access API in:

- http://localhost:8000/api

## Steps to run and install the Front-end

1. Clone the Repository:

```bash
git clone https://github.com/felipeclarindo/my-energy.git
```

2. Enter the directory:

```bash
cd my-energy
```

3. Create Virtual Environment:

```bash
python -m venv .venv
```

4. Activate the `Virtual Environment` running the `.bat` file in `.venv/Scripts/Activate.bat`.

5. Install dependencies:

```bash
pip install - r requirements.txt
```

6. Run application:

```bash
streamlit run ./app/app.py
```

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
