from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('animecreate/', views.animcreate, name='create_anime'),
    path('anime/edit/<int:pk>/', views.AnimeUpdateView.as_view(template_name='anime/bases/anime_update_form.html'), name='anime_edit'),
]