import shelve
import pokebase as pb


pb.common.ENDPOINTS.append('local/evolution-chain')


def get_data(endpoint, resource_id=None, subresource=None, **kwargs):

    if not kwargs.get('force_lookup', False):
        try:
            data = pb.cache.load(f'local/{endpoint}', resource_id, subresource)
            return data
        except KeyError:
            pass

    data = pb.api._call_api(endpoint, resource_id, subresource)
    pb.cache.save(data, f'local/{endpoint}', resource_id, subresource)

    return data


class APIChainResource(pb.APIResource):

    def __init__(self, endpoint, name_or_id, lazy_load=False, force_lookup=False):
        self.data_fetch = ''
        super().__init__(endpoint, name_or_id, lazy_load, force_lookup)
        

    def _load(self):
        """Function to collect reference data and connect it to the instance as
         attributes.
         Internal function, does not usually need to be called by the user, as
         it is called automatically when an attribute is requested.
        :return None
        """

        data = get_data(self.endpoint, self.id_, force_lookup=self._APIResource__force_lookup)

        self.data_fetch = data

        return None

