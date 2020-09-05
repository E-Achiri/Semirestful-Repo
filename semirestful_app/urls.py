from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.addshow),
    path('shows/create', views.createshow),
    path('shows/<int:x>', views.showpage),
    path('shows/<int:x>/edit', views.editShow),
    path('shows/<int:x>/update', views.updateShow),
    path('shows/<int:x>/destroy', views.destroy)
]