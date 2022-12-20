from django.urls import path
from fitnesskit_task.views import SourcesApiView, DetailsViewSet

urlpatterns = [
    path("team/get_employees", SourcesApiView.as_view()),
    path("team/get_employees/<int:id>", DetailsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))
]