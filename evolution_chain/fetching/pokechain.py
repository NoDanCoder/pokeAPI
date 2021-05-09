from .loader import offline_evolution_chain, offline_pokemon, offline_pokemon_species, APILocalResource

def get_poke_data(name):
    """Search pokemon and his evolution chain locally

    Args:
        name (str): Pokemon name to lookup

    Returns:
        dict: compiled pokemon info
    """
    pokemon = offline_pokemon(name).data_fetch

    if pokemon.get('error', False):
        return pokemon

    pokemon['preevolution'] = []
    pokemon['evolution'] = []

    # funcion de armado 
    pokemon_species = offline_pokemon_species(name).data_fetch

    pokemon_evo_chain = pokemon_species['evolution_chain']['url']
    pokemon_evo_chain = int(pokemon_evo_chain.split('/')[-2])

    pokemon_evo_chain = offline_evolution_chain(pokemon_evo_chain).data_fetch

    construct_chain(pokemon_evo_chain, pokemon)

    return pokemon



def construct_chain(chain, pokemon_data):
    """Assings preevolitions and evolutions of given pokemon
    according on his position on evolution tree

    Args:
        chain (dict): pokemon evolution chain where belongs to
        pokemon_data (dict): pokemon info and place to add his
            preevolutions and evolutions
    """

    for pokemon in chain:
        
        specie = pokemon['species']['name']

        if specie == pokemon_data['name']:
            pokemon_data['evolution'] = pokemon['evolves_to']
            return
        elif len(pokemon['evolves_to']) == 0:
            continue
        else:
            pokemon_data['preevolution'].append(pokemon['species'])
            construct_chain(pokemon['evolves_to'], pokemon_data)