from django.core.management.base import BaseCommand
from django.utils import timezone
from evolution_chain.fetching.loader import local_evolution_chain

class Command(BaseCommand):
    
    help = 'Fetchs and stores a given chain id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Indicates chain ID to lookup')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        try:
            local_evolution_chain(id)
        except (ConnectionError, OSError):
            self.stderr.write("Error: db unavailable or network issues")
        else:
            self.stdout.write(f"Done! {id} registered")