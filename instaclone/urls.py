from django.urls import path

from .views import UploadCreateView, UploadListView, UploadEditView



urlpatterns = [
    path('upload/', UploadCreateView.as_view(), name='create-upload'),
    path('upload/edit/<int:pk>/', UploadEditView.as_view(), name='edit-upload'),
    path('', UploadListView.as_view(), name='list-uploads'),
]