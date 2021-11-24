# Galharufa2021 - RESTful API

## Setup and installation

### Requirements

Python 3.7.12 or higher installed.

### Setup instructions

On the folder `/galharufa2021_restful_api`, run the following command:

- `pip install -r requirements.txt` (Windows)
- `pip3 install -r requirements.txt` (Linux/macOS)

Include `DJANGO_SECRET_KEY` on your `PATH` as an environment variable.

- MacOs uses the file .zshrc to `PATH` locate the environment variables.

### Running the server

On the folder `/galharufa2021_restful_api`, run the following command:

- `python manage.py runserver` (Windows)
- `python3 manage.py runserver` (Linux/macOS)

The server will be running on `localhost` (`127.0.0.1`) on port 8000.

## Usage

### Token generation routes

- `/api/users/token`
- `/api/users/token/refresh`

### API admin GET routes (TOKEN needed)

- `/api/pessoas-admin/`
- `/api/atores-admin/`
- `/api/figuracoes-admin/`
- `/api/modelos-admin/`
- `/api/criancas-admin/`
- `/api/pessoa-admin/slug`
- `/api/ator-admin/slug`
- `/api/figuracao-admin/slug`
- `/api/modelo-admin/slug`
- `/api/crianca-admin/slug`

Example: `http://127.0.0.1:8000/api/pessoas-admin/` returns a JSON response with all casting database entries.

When sending an `admin` request, it is necessary to append the following headers to the request:

```
headers = {"Authorization": Bearer TOKEN",
          "Content-type": "application/json"}
```

The `TOKEN` can be generated on the `http://localhost:8000/api/users/token/` URL and expires after 30 minutes.

### API GET routes (TOKEN not needed)

- `/api/atores/`
- `/api/figuracoes/`
- `/api/modelos/`
- `/api/criancas/`
- `/api/ator/slug`
- `/api/figuracao/slug`
- `/api/modelo/slug`
- `/api/crianca/slug`

Example of single entry: `http://127.0.0.1:8000/api/ator/joao/`

This should return a JSON response with:

```
{'DRT': '1234/SP',
 'altura': 1.75,
 'ano': 1900,
 'foto3x4': '/static/images/3x4/f2b0dfd92af85ce8a8fe866751fdd205.jpg',
 'foto_com_sorriso': '/static/images/com_sorriso/shutterstock_439389151-1024x679.jpg',
 'foto_corpo_inteiro': '/static/images/corpo_inteiro/portrait-handsome-smiling-stylish-young-man-model-wearing-je_ono3VCB.jpg',
 'manequim': 99,
 'nome_artistico': 'João',
 'sapato': 99}
```

## To-do list

### Implement POST/PUT requests for admin

### Implement DELETE requests for admin
