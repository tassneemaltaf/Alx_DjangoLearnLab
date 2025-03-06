from django.urls import path
from .import views

urlpatterns = [
  path("", views.index, name="index")
  path("relationship_app", include("relationship_app.urls"))
]