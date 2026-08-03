from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import MondaySyncService


class MondaySyncView(APIView):

    def post(self, request):

        try:
            
            if "challenge" in request.data:
                return Response({"challenge": request.data["challenge"]})

        # 2. Monday event
            event = request.data["event"]

            board_id = event["boardId"]
            item_id = event["pulseId"]
            event_type = event["type"]

            print(board_id)
            print(item_id)
            print(event_type)
            #board_id=request.data["board_id"]
            #print(board_id,request.headers)
            result = MondaySyncService().sync(board_id)

            return Response(
                result,
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )