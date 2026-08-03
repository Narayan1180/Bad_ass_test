from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import MondaySyncService


class MondaySyncView(APIView):

    def post(self, request):

        try:
            board_id=request.data["board_id"]
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