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