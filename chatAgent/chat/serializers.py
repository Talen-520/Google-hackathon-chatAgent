from rest_framework import serializers
from .models import ChatModel

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = ['id', 'user_input', 'chatbot_response', 'pub_date']
