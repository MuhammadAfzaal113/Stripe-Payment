from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_eventstream import send_event


class NotificationView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            print(send_event('test', 'message', {'text': 'hello world'}))
            send_event('test', 'notification', {'text': 'hello developer'})
            response = {
                'success': True,
                'message': 'Success'
            }
            return Response(response, status.HTTP_200_OK)

        except Exception as e:
            print(f'throws Exception {e}')
            response = {
                'success': False,
                'message': f'bad request {e}'
            }
            return Response(response, status.HTTP_400_BAD_REQUEST)
