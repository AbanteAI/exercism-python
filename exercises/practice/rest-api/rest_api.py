import json

class RestAPI:

class RestAPI:
    def __init__(self, database=None):
        self.database = database if database is not None else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload_dict = json.loads(payload)
                requested_users = payload_dict.get("users", [])
                users_info = [user for user in self.database["users"] if user["name"] in requested_users]
            else:
                users_info = self.database["users"]
            return json.dumps({"users": sorted(users_info, key=lambda x: x["name"])})

    def post(self, url, payload=None):
        payload_dict = json.loads(payload)
        if url == "/add":
            new_user = {
                "name": payload_dict["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            lender_name = payload_dict["lender"]
            borrower_name = payload_dict["borrower"]
            amount = payload_dict["amount"]
            lender = next(user for user in self.database["users"] if user["name"] == lender_name)
            borrower = next(user for user in self.database["users"] if user["name"] == borrower_name)
            lender["owed_by"][borrower_name] = lender["owed_by"].get(borrower_name, 0) + amount
            borrower["owes"][lender_name] = borrower["owes"].get(lender_name, 0) + amount
            lender["balance"] += amount
            borrower["balance"] -= amount
            return json.dumps({"users": sorted([lender, borrower], key=lambda x: x["name"])})
