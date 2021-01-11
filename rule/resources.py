from import_export import resources
from .models import Qradardb


class PersonResource(resources.ModelResource):
    class meta:
        model = Person
