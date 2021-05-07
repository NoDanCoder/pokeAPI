import pokebase as pb
from . import build

pb.common.ENDPOINTS.append('local/evolution-chain')


def get_data(endpoint, resource_id=None, subresource=None, **kwargs):

    if not kwargs.get('force_lookup', False):
        try:
            data = pb.cache.load(f'local/{endpoint}', resource_id, subresource)
            return data
        except KeyError:
            pass

    data = build.chain_start(resource_id)
    pb.cache.save(data, f'local/{endpoint}', resource_id, subresource)

    return data


class APILocalResource(pb.APIResource):

    def __init__(self, endpoint, name_or_id, lazy_load=False, force_lookup=False):
        self.data_fetch = ''
        super().__init__(endpoint, name_or_id, lazy_load, force_lookup)
        

    def _load(self):
        """Function to collect reference data and connect it to the instance as
         attributes.
         Internal function, does not usually need to be called by the user, as
         it is called automatically when an attribute is requested.

        Returns:
            [none]: [add data directly to data_fetch instance property]
        """


        data = get_data(self.endpoint, self.id_, force_lookup=self._APIResource__force_lookup)

        self.data_fetch = data

        return None