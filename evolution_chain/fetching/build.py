import pokebase as pb


def chain_start(resource_id):
    
    fetch = [pb.evolution_chain(resource_id).chain]

    data_struct = {
        'species': None,
        'evolves_to': []
    }

    construct_chain(fetch, data_struct['evolves_to'])

    return data_struct


def construct_chain(data, current):

    for pokemon in data:
        
        specie = pokemon.species

        insertion = {
            'species': {'name': specie.name, 'types': get_species(specie.name)},
            'evolves_to': []
        }

        current.append(insertion)

        construct_chain(pokemon.evolves_to, insertion['evolves_to'])


def get_species(name):

    varieties = pb.pokemon_species(name).varieties
    return [get_pokemon_info(variety.pokemon.name) for variety in varieties]


def get_pokemon_info(name):

    info = pb.pokemon(name)

    pokemon_data = {
        'id': info.id,
        'name': info.name,
        'height': info.height,
        'weight': info.weight,
        'stats': [fill_stat(stat) for stat in info.stats]
    }

    return pokemon_data


def fill_stat(stat):

    stat_data = {
        'base_stat': stat.base_stat,
        'effort': stat.effort,
        'name': stat.stat.name
    }

    return stat_data