from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS
from .models import *
from .serializers import *
from user.models import Profile
from rest_framework.response import Response
from rest_framework import status


# -------------------------
# CATEGORY VIEWS
# -------------------------

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


# -------------------------
# Skill VIEWS
# -------------------------

class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [AllowAny]


class SkillDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # permission_classes = [AllowAny]


# -------------------------
# FreelancerSkillList VIEWS
# -------------------------


class FreelancerSkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = FreelancerSkill.objects.all()
    serializer_class = FreelancerSkillSerializer
    # permission_classes = [AllowAny]


class FreelancerSkillDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreelancerSkill.objects.all()
    serializer_class = FreelancerSkillSerializer
    # permission_classes = [AllowAny]


# -------------------------
# JOB VIEWS
# -------------------------

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return JobSerializerSafe
        return self.serializer_class

    def perform_create(self, serializer):
        if not self.request.user.is_client:
            raise PermissionDenied("Only clients can post jobs.")
        serializer.save(client=self.request.user)


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return JobSerializerSafe
        return self.serializer_class


# -------------------------
# PROPOSAL VIEWS
# -------------------------

class ProposalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProposalSerializerSafe
        return self.serializer_class

    def perform_create(self, serializer):
        if not self.request.user.is_freelancer:
            raise PermissionDenied("Only freelancers can submit proposals.")
        serializer.save(freelancer=self.request.user)


class ProposalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProposalSerializerSafe
        return self.serializer_class


# -------------------------
# CONTRACT VIEWS
# -------------------------

class ContractListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.AllowAny]


class ContractDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------
# REVIEW VIEWS
# -------------------------

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------
# RESUME VIEWS
# -------------------------

class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ResumeSerializerSafe
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResumeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ResumeSerializerSafe
        return self.serializer_class
