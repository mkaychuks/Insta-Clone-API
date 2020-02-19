from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions

from .serializers import UserProfileSerializer, UserProfileUploads
from .models import UserProfile
from .permissions import YourProfile

from instaclone.models import Upload



class UserCreateProfile(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated,)



class UserProfileList(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated, YourProfile,)


    '''Returns the profile of users'''
    def retrieve(self, request: Request, *args, **kwargs):
        ''' if provided 'pk' is 'pk' then return the current user'''
        if kwargs.get('pk') == 'pk':
            return Response(self.get_serializer(request.user).data)
        return super().retrieve(request, args, kwargs)


class UserProfileUploadsView(generics.ListAPIView):
    serializer_class = UserProfileUploads
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        """
        This view should return a list of all the uploads
        for the currently authenticated user.
        """
        user = self.request.user
        return UserProfile.objects.filter(user=user)