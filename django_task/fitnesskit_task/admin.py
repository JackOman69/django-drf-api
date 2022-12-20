from django.contrib import admin
from fitnesskit_task.models import Sources, BasicAuth, RequestBody, ParametersRequestBody

@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    pass

@admin.register(BasicAuth)
class SourcesAdmin(admin.ModelAdmin):
    pass

@admin.register(RequestBody)
class SourcesAdmin(admin.ModelAdmin):
    pass

@admin.register(ParametersRequestBody)
class SourcesAdmin(admin.ModelAdmin):
    pass