from rest_framework import generics
from .models import ChatModel
from .serializers import ChatSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view #function based view
@api_view(['GET','POST']) # add any function you should support
def home(request):
    #return render(request, 'index.html')
    return Response({"server running"},status=status.HTTP_200_OK)

class ChatView(generics.ListCreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer

class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        user_input = request.data.get('user_input')
        # Here you can use your chatbot logic to generate a response
        chatbot_response = "This is a sample response from the chatbot."
        data = {'user_input': user_input, 'chatbot_response': chatbot_response}
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
