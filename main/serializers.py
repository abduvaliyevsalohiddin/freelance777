from rest_framework import serializers
from .models import *
from user.serializers import ProfileSerializer


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class FreelancerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerSkill
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JobSerializerSafe(serializers.ModelSerializer):
    client = ProfileSerializer(read_only=True, many=False)

    class Meta:
        model = Job
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class ProposalSerializerSafe(serializers.ModelSerializer):
    freelancer = ProfileSerializer(read_only=True, many=False)

    class Meta:
        model = Proposal
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ResumeSerializerSafe(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True, many=False)

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
