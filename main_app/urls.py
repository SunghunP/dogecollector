from django.urls import path 
from . import views

urlpatterns= [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),

	################
	## DOGS
	################
	path('dogs/', views.dogs_index, name='dogs_index'),
	path('dogs/<int:dog_id>', views.dogs_detail, name='detail'),
	path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
	path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
	path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),

	################
	## FEEDINGS
	################
	path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),

	################
	## TOYS
	################
	path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
	path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

	################
	## AUTH
	################
	path('accounts/signup/', views.signup, name='signup'),
]