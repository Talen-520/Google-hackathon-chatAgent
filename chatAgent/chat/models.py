from django.db import models

class ChatModel(models.Model):
    user_input = models.TextField()  # Field to store user input
    chatbot_response = models.TextField()  # Field to store chatbot response
    pub_date = models.DateTimeField('date published')
