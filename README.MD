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

## API endpoints to Pieces


### GET
- Return all pieces created:</br>
Path `/pieces/`
- Return the piece selected:</br>
Path`/pieces/<id>/`

### POST
- Create a piece:</br>
Path `/pieces/`</br>
Body:
    ```json
    {
        "name": "knight",
        "color": "black"
    }
    ```
- Update a piece:</br>
Path `/pieces/<id>/`</br>
Body:
    ```json
    {
        "name": "knight",
        "color": "black"
    }
    ```
- Get the possible moves in two steps for the passed coordinate, if the piece is a knight:</br>
Path `/pieces/<id>/moves/`</br>
Body:
    ```json
    {
        "coordinate": "a1"
    }
    ```

## API endpoints to Board


### GET
- Return all boards created:</br>
Path `/boards/`
- Return the board selected:</br>
Path`/boards/<id>/`

### POST
- Create a board:</br>
Path `/boards/`</br>
Body:
    ```json
    {
        "rows": 8,
        "columns": 8
    }
    ```
- Update a board:</br>
Path `/boards/<id>/`</br>
Body:
    ```json
    {
        "rows": 8,
        "columns": 8
    }
    ```