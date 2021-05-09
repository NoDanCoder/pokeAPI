import pokebase as pb
from . import build

pb.common.ENDPOINTS.append('evolution-chain/local')


def get_data_offline(endpoint, resource_id=None):

    data = pb.cache.load(endpoint, resource_id)
    if isinstance(data, dict) and data.get('results', []):
        raise KeyError()
    return data


def get_data(endpoint, resource_id=None, subresource=None, **kwargs):

    if not kwargs.get('force_lookup', False):
        try:
            data = pb.cache.load(f'{endpoint}/local', resource_id, subresource)
            return data
        except KeyError:
            pass

    data = build.chain_start(resource_id)
    pb.cache.save(data, f'{endpoint}/local', resource_id, subresource)

    return data


class APILocalResource(pb.APIResource):

    def __init__(self, endpoint, name_or_id, lazy_load=False, force_lookup=False, offline_mode=False):
        self.data_fetch = ''
        self.offline_mode = offline_mode
        super().__init__(endpoint, name_or_id, lazy_load, force_lookup)
        
        

    def _load(self):
        """Function to collect reference data and connect it to the instance as
         attributes.
         Internal function, does not usually need to be called by the user, as
         it is called automatically when an attribute is requested.

        Returns:
            [none]: [add data directly to data_fetch instance property]
        """

        if not self.offline_mode:
            data = get_data(self.endpoint, self.id_, force_lookup=self._APIResource__force_lookup)
        else:
            self.endpoint += '/local' if self.endpoint == 'evolution-chain' else ''
            data = get_data_offline(self.endpoint, self.id_)

        self.data_fetch = data

        return None