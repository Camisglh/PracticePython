from todolist.views import todo_list, todo_detail, category_list, category_detail
from django.urls import path

urlpatterns = [
    path('todo/', todo_list, name='todo-list'),
    path('todo/<int:pk>/', todo_detail, name='todo-detail'),
    path('category/', category_list, name='category-list'),
    path('category/<int:pk>/', category_detail, name='category-detail')
]
