from import_export import resources
from .models import empModel

class empModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=empModel