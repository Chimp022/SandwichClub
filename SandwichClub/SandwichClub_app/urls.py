from django.conf.urls import url
from SandwichClub_app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^categories/', views.categories, name='categories'),
	url(r'^about/', views.about, name='about'),
]