from import_export import resources
from .models import godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel

class godryModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=godryModel
class outofstockModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=outofstockModel
class romobileModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=romobileModel
class rolistModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=rolistModel
class yv26ModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=yv26Model
class yv208ModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=yv208Model
class yv209dModelResource(resources.ModelResource):
    class meta:
        skip_unchanged=True
        model=yv209dModel