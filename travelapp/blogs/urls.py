from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.ArticlesListView.as_view()),
    path('<int:pk>', views.ArticlesDetailView.as_view()),
]