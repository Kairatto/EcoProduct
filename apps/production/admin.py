from django.contrib import admin
from .models import ProductionShort, Production, ProductionPath, ProductionProcess


admin.site.register(Production)
admin.site.register(ProductionPath)
admin.site.register(ProductionShort)
admin.site.register(ProductionProcess)

