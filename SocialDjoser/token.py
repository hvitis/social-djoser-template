from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user = User.objects.get(id=user.id)
        # Add custom claims
        token['uuid'] = str(user.unique_id) 
        return token


class CustomJWTToken(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
