from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import MondaySyncService
from .models import FranchiseDevelopment



class MondaySyncView(APIView):


    def get(self, request):
        data = FranchiseDevelopment.objects.values(
            "monday_item_id",
            "franchise_name",
            "market",
            "stage",
            "loi_date",
            "under_contract_date",
            "under_development_date",
            "open_date",
            "approved_date",
            "hold_date",
        )

        return Response(list(data))


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