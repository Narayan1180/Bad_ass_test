from .connectors.monday import MondayConnector
#from .models import Haldiram
from .models import FranchiseDevelopment

class MondaySyncService:

    def sync(self,board_id):

        connector = MondayConnector()

        items = connector.fetch(board_id)
        #print(items)
        
        created = 0
        updated = 0

        for item in items:
            data = connector.transform(item)
            monday_item_id = data.pop("monday_item_id")
            #print("-->",data)

            obj, is_created = FranchiseDevelopment.objects.update_or_create(monday_item_id=monday_item_id,defaults=data)

            if is_created:
                created += 1
            else:
                updated += 1


        return {
            "success": True,
            "created": created,
            "updated": updated,
            "total": len(items),
        }