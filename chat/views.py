from django.shortcuts import render

# Create your views here.
#chat/views.py
from django.views.generic import TemplateView

from chat.models import Room

from rest_framework.response import Response
from rest_framework.views import APIView

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # 단순히 시작히 룸을 만들기 위한 장치
        Room.objects.get_or_create(name='노티룸', group_name='main')
        return super().get(request, *args, **kwargs)


class Notification(APIView):
    def post(self, request, *args, **kwargs):
        room = Room.objects.get(group_name='main')
        message = room.messages.create(message=request.data.get('message'))

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'main',
            {
                'type': 'chat_message',
                'message': str(message),
                'created': message.created.strftime('%p %I:%M')
            }
        )

        return Response({'status': 200, 'meesage': '{} send success'.format(message)})