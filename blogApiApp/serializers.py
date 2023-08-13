from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post  # Use "model" instead of "mod"
        fields = '__all__'