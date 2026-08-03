import requests
from django.conf import settings

from .base import BaseConnector


class MondayConnector(BaseConnector):

    def fetch(self,board_id):

        url = "https://api.monday.com/v2"

        headers = {
            "Authorization": settings.MONDAY_API_TOKEN,
            "Content-Type": "application/json",
        }

        query = f"""
        {{
            boards(ids: {board_id}) {{
                items_page {{
                    items {{
                        id
                        name
                        column_values {{
                            text
                            column {{
                                title
                            }}
                        }}
                    }}
                }}
            }}
        }}
        """

        response = requests.post(
            url,
            json={"query": query},
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()
        #print(dir(response))
        data = response.json()

        if "errors" in data:
            raise Exception(data["errors"])

        return data["data"]["boards"][0]["items_page"]["items"]

    def transform(self, item):
        columns = {col["column"]["title"]: col["text"]
                    for col in item["column_values"]
                  }

        data = {
                "monday_item_id": item["id"],
                "franchise_name": item["name"],
                "market": columns.get("Market"),
                "stage": columns.get("Stage"),
                "loi_date": columns.get("LOI") or None,
                "under_contract_date": columns.get("Under Contract") or None,
                "under_development_date": columns.get("Under Development") or None,
                "open_date": columns.get("Open") or None,
                "approved_date": columns.get("Approved") or None,
                "hold_date": columns.get("Hold") or None,
                #"monday_created_at": item["created_at"],
                # "monday_updated_at": item["updated_at"],
              }

        print(data)

        return data
        """
        columns = {
            col["column"]["title"]: col["text"]
            for col in item["column_values"]
        }

        return {
            "monday_item_id": item["id"],
            "name": item["name"],
            "sku": columns.get("SKU"),
            "category": columns.get("Category"),
            "price": columns.get("Price") or 0,
            "stock": columns.get("Stock") or 0,
            "gst": columns.get("GST %") or 0,
            "supplier": columns.get("Supplier"),
            "manufacturing_date": columns.get("Manufacturing Date") or None,
            "expiry_date": columns.get("Expiry Date") or None,
            "status": columns.get("Status"),
        }
        """