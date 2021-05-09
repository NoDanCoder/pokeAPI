# PokeAPI Wrapping service

PokeAPI Wrapping service is a Django project to get a vinculated data from a given pokemon using PokeAPI service.

## Description

This project uses PokeAPI service to feed a database to create relation between them, this gives the oportunity to
lookup information about a lot of topics based on a given pokemon.

## Installation

First clone repo.

```bash
    git clone https://github.com/NoDanCoder/pokeAPI
    cd pokeAPI
```
Then import dependences.
```bash
    pipenv shell
    pipenv
```
Now make DB migrations and run!
```bash
    python manage.py migrate
    python manage.py runserver
```

Enjoy!

## Usage

You can use Django console service to download related pokemon-chain data and store it
```bash
    python manage.py registerchain <int:id>
```
To get more info about pokemon-chain's check [this](https://pokeapi.co/docs/v2#evolution-section) info.

Now you can use related pokemon info
```bash
    http://localhost:8000/api/<str:name>
```
Again, you can find a list of available pokemons [here](https://pokeapi.co/api/v2/pokemon?limit=1118).

Remember local available pokemons depends on previous chain-load, if your pokemon doesn't belong to
the chain then won't load.

## Roadmap

 - Add async fetch system
 - Add graph db suport

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)