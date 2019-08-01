from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'records'),
    path('<int:studentinfo_id>', views.studentinfo, name = 'studentinfo'),
    path('search', views.search, name = 'search')
]