from import_export import resources
from .models import yqlabModel,yvrokarModel

class yqlabModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=yqlabModel
class yvrokarModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=yvrokarModel
