from django.urls import path
from . import views


urlpatterns=[
    path('',views.home, name='home'),
    path('hello/',views.hello),
    path('details/<int:request_id>/',views.detail, name='details'),
    path('delete/<int:request_id>/',views.delete, name='delete'),
    path('update/<int:request_id>/',views.update, name='update'),
    path('create/', views.create, name='create'),
]