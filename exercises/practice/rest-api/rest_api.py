class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                users = json.loads(payload)["users"]
                return json.dumps({"users": [user for user in self.database["users"] if user["name"] in users]})
            else:
                return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == "/add":
            user_data = json.loads(payload)
            new_user = {
                "name": user_data["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            iou_data = json.loads(payload)
            lender_name = iou_data["lender"]
            borrower_name = iou_data["borrower"]
            amount = iou_data["amount"]

            lender = next(user for user in self.database["users"] if user["name"] == lender_name)
            borrower = next(user for user in self.database["users"] if user["name"] == borrower_name)

            if borrower_name in lender["owes"]:
                lender["owes"][borrower_name] -= amount
                if lender["owes"][borrower_name] <= 0:
                    lender["owed_by"][borrower_name] = -lender["owes"][borrower_name]
                    del lender["owes"][borrower_name]
            else:
                lender["owed_by"].setdefault(borrower_name, 0)
                lender["owed_by"][borrower_name] += amount

            if lender_name in borrower["owed_by"]:
                borrower["owed_by"][lender_name] -= amount
                if borrower["owed_by"][lender_name] <= 0:
                    borrower["owes"][lender_name] = -borrower["owed_by"][lender_name]
                    del borrower["owed_by"][lender_name]
            else:
                borrower["owes"].setdefault(lender_name, 0)
                borrower["owes"][lender_name] += amount

            lender["balance"] += amount
            borrower["balance"] -= amount

            return json.dumps({"users": sorted([lender, borrower], key=lambda x: x["name"])})