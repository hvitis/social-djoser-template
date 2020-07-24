from djoser.serializers import UserSerializer as BaseUserSerializer
from accounts.serializers import SocialMediaSerializer
from rest_framework import serializers
from accounts.models import UserProfile

class CustomUserSerializer(BaseUserSerializer):
    user_profile = serializers.SerializerMethodField(read_only=True)
    class Meta(BaseUserSerializer.Meta):
        fields = (
            'is_active',
            'is_subscribed', 
            'email',
            'nickname',
            'first_name',
            'last_name', 
            'avatar',
            'unique_id',
            'user_type',
            'locale',
            'date_joined',
            #Nested serializers:
            'user_profile', 
            )

    def get_user_profile(self, obj):
        qs = UserProfile.objects.filter(user__id=obj.id) 
        return SocialMediaSerializer(qs, many=True).data
