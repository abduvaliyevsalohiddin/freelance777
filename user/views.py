from .serializers import *
from rest_framework import filters
from rest_framework.generics import *
from rest_framework.permissions import *


class RegisterAPIView(CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user


class ProfileRetrieveView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
