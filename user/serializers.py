from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    # def get_freelancer_skills(self, obj):
    #     if obj.is_freelancer:
    #         skills = FreelancerSkill.objects.filter(user=obj)
    #         return FreelancerSkillSerializer(skills, many=True).data
    #     return []
