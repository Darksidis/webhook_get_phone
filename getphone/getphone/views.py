import json


import requests
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import GetPhone
from ...credietienals import *

TELEGRAM_URL = url
TUTORIAL_BOT_TOKEN = token


class TutorialBotView(View):

    def post(self, request):
        """Функция для отправки пост-запроса на приёмник."""
        t_data = json.loads(request.body)
        t_message = t_data['message']
        t_chat = t_message['chat']
        try:
            phone_data = t_message['contact']
        except KeyError:
            phone_data = None
        if phone_data:

            headers = {'content_type': 'application/json'}
            data_for_request = {'phone': phone_data['phone_number'], 'login': phone_data['first_name']}

            response = requests.post(
                'https://test.com/app/', #здесь нужно указать url, который будет получать номер
                headers=headers,
                data=json.dumps(data_for_request),
            )
            self.send_message('номер успешно отправлен', t_chat['id'])
            return response
        else:
            msg = 'Unknown command'
            self.send_message(msg, t_chat['id'])

        return JsonResponse({'ok': 'POST request processed'})

    @staticmethod
    def send_message(message, chat_id):
        """Функция для отправки пост-запроса к api телеграма"""
        data_for_api = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown',
        }

        return requests.post(
            f'{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage', data=data_for_api,
        )

