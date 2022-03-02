# Chess API

### API that allows the registration of chess pieces and returns all possible moves in two turns to the knight piece.


## Getting Started

1. Clone this repository: 
```bash
git clone git@github.com:ArthurFerrao/chess-api.git
```
2. Go to `chess-api`:
```bash
cd chess-api
```
3. Create and set the [virtualenv](https://docs.python.org/pt-br/3/tutorial/venv.html).
4. Install the `requirements`:
```bash
pip install -r requirements.txt 
```
5. Make the migrations:
```bash
python manage.py migrate
```
6. Run:
```bash
python manage.py runserver
```

> Open http://localhost:8000 with your browser to see the result.
You can [create a admin user](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) and access the `/admin` path to see a friendly interface.
