from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),        # Main page
    path('add/', views.add, name='add'),                     # Add a todo
    path('<int:todo_id>/delete/', views.delete, name='delete'),  # Delete a todo
    path('<int:todo_id>/update/', views.update, name='update'),  # Update a todo
]
