from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'is_superuser', 'is_freelancer', 'is_client', 'phone', 'gender', 'bio', 'location', 'profile_picture', )

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)

    # def get_freelancer_skills(self, obj):
    #     if obj.is_freelancer:
    #         skills = FreelancerSkill.objects.filter(user=obj)
    #         return FreelancerSkillSerializer(skills, many=True).data
    #     return []
