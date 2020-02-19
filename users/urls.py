from django.urls import path

from .views import UserProfileList, UserCreateProfile, UserProfileUploadsView


urlpatterns = [
    path('create/profile/', UserCreateProfile.as_view(), name='create-profile'),
    path('profile/<int:pk>/', UserProfileList.as_view(), name='user_profile'),
    path('profile/uploads/', UserProfileUploadsView.as_view(), name='user-uploads'),
]