from django.urls import path
from . import views
from .views import JobCreateView
urlpatterns = [
    path('jobs/create/', JobCreateView.as_view(), name='job_create'),
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_edit'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/apply/', views.job_apply, name='job_apply'),
]