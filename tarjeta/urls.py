

from re import template
import django
from django.urls import path, include
from .import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from tarjeta.views import DetailCard, CreateCard, UpdateCard, DeleteCard, CreateBeneficery

urlpatterns = [
   
    path('home', views.tarjeta, name="Home"),
    path('register',views.register, name='register'),
    path('',LoginView.as_view(template_name='index.html'),name='login'),
    path('logout',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('detail/<int:pk>',DetailCard.as_view(template_name='detail.html'), name="Detail"),
   # path('create',CreateCard.as_view(template_name = "create.html"), name='Create'),
    path('update/<int:pk>', UpdateCard.as_view(template_name = "update.html"), name='Update'),    
    path('delete/<int:pk>', DeleteCard.as_view(template_name="delete.html"), name='Delete'),    
    path('createBeneficery',CreateBeneficery.as_view(template_name = "createBeneficery.html"), name='CreateBeneficery'),
    path('create',CreateCard.as_view(template_name = "create.html"), name='Create'),
    
  
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
