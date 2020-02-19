from rest_framework import generics, permissions

from .serializers import UploadSerializer, UploadListSerializer
from .models import Upload
from .permissions import IsAuthor


class UploadCreateView(generics.CreateAPIView):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class UploadEditView(generics.RetrieveUpdateAPIView):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthor)


class UploadListView(generics.ListAPIView):
    queryset = Upload.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UploadListSerializer