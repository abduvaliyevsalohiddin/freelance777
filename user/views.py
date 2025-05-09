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


class SkillListCreateAPIView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class SkillDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class FreelancerSkillListCreateAPIView(ListCreateAPIView):
    queryset = FreelancerSkill.objects.all()
    serializer_class = FreelancerSkillSerializer
    permission_classes = [AllowAny]


class FreelancerSkillDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FreelancerSkill.objects.all()
    serializer_class = FreelancerSkillSerializer
    permission_classes = [AllowAny]
