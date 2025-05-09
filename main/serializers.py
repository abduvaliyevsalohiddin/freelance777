from rest_framework import serializers
from .models import Category, Job, Proposal, Contract, Review, Resume
from user.models import Skill, Profile


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description']


class JobSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)
    skills_required = SkillSerializer(many=True, read_only=True)
    skills_required_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True, write_only=True, source='skills_required'
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )

    class Meta:
        model = Job
        fields = [
            'id', 'client', 'title', 'description', 'budget',
            'deadline', 'skills_required', 'skills_required_ids',
            'category', 'category_id', 'is_open', 'created_date'
        ]


class ProposalSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(), write_only=True, source='job'
    )
    freelancer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Proposal
        fields = [
            'id', 'job', 'job_id', 'freelancer', 'cover_letter',
            'proposed_price', 'submitted_at', 'status'
        ]
        read_only_fields = ['submitted_at', 'status']


class ContractSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(), write_only=True, source='job'
    )
    freelancer = serializers.StringRelatedField(read_only=True)
    freelancer_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.filter(is_freelancer=True), write_only=True, source='freelancer'
    )
    client = serializers.StringRelatedField(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.filter(is_client=True), write_only=True, source='client'
    )

    class Meta:
        model = Contract
        fields = [
            'id', 'job', 'job_id', 'freelancer', 'freelancer_id',
            'client', 'client_id', 'end_date', 'is_completed', 'created_date'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    contract = serializers.StringRelatedField(read_only=True)
    contract_id = serializers.PrimaryKeyRelatedField(
        queryset=Contract.objects.all(), write_only=True, source='contract'
    )
    reviewer = serializers.StringRelatedField(read_only=True)
    reviewee = serializers.StringRelatedField(read_only=True)
    reviewee_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), write_only=True, source='reviewee'
    )

    class Meta:
        model = Review
        fields = [
            'id', 'contract', 'contract_id',
            'reviewer', 'reviewee', 'reviewee_id',
            'rating', 'comment', 'created_date'
        ]


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'user', 'title', 'summary', 'resume_file', 'created_date']
