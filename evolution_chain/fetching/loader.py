from .fetching import APILocalResource

def local_evolution_chain(id_, **kwargs):
    """Quick evolution-chain lookup with a deeper info than current pokeAPI.
    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    Args:
        id_ (int): evolution_chain id to lookup

    Returns:
        APILocalResource: instance which handle resquest and caching
    """

    return APILocalResource('evolution-chain', id_, **kwargs)


def offline_pokemon_species(id_, **kwargs):
    """Quick evolution-species lookup. (only on local storage)
    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    Args:
        id_ (int): evolution_chain id to lookup

    Returns:
        APILocalResource: instance which handle resquest and caching
    """

    return APILocalResource('pokemon-species', id_, offline_mode=True)


def offline_pokemon(id_, **kwargs):
    """Quick pokemon lookup. (only on local storage)
    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    Args:
        id_ (int): evolution_chain id to lookup

    Returns:
        APILocalResource: instance which handle resquest and caching
    """

    return APILocalResource('pokemon', id_, offline_mode=True)


def offline_evolution_chain(id_, **kwargs):
    """Quick evolution-chain lookup with a deeper info than current pokeAPI.
        only on local storage
    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    Args:
        id_ (int): evolution_chain id to lookup

    Returns:
        APILocalResource: instance which handle resquest and caching
    """

    return APILocalResource('evolution-chain', id_, offline_mode=True)