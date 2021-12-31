from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
	path('login/', LoginView.as_view(template_name='polls/login.html')),
	path('logout/', LogoutView.as_view(next_page='/polls')),
    path('add/', views.addQuestion, name='addQuestion'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]