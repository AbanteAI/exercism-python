class RestAPI:
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
        return None

    def post(self, url, payload=None):
        if url == "/add":
            user = json.loads(payload)["user"]
            new_user = {"name": user, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            data = json.loads(payload)
            lender = data["lender"]
            borrower = data["borrower"]
            amount = data["amount"]

            lender_data = next(user for user in self.database["users"] if user["name"] == lender)
            borrower_data = next(user for user in self.database["users"] if user["name"] == borrower)

            if borrower in lender_data["owes"]:
                lender_data["owes"][borrower] -= amount
                if lender_data["owes"][borrower] <= 0:
                    lender_data["owed_by"][borrower] = -lender_data["owes"][borrower]
                    del lender_data["owes"][borrower]
            else:
                lender_data["owed_by"][borrower] = lender_data["owed_by"].get(borrower, 0) + amount

            if lender in borrower_data["owed_by"]:
                borrower_data["owed_by"][lender] -= amount
                if borrower_data["owed_by"][lender] <= 0:
                    borrower_data["owes"][lender] = -borrower_data["owed_by"][lender]
                    del borrower_data["owed_by"][lender]
            else:
                borrower_data["owes"][lender] = borrower_data["owes"].get(lender, 0) + amount

            lender_data["balance"] = sum(lender_data["owed_by"].values()) - sum(lender_data["owes"].values())
            borrower_data["balance"] = sum(borrower_data["owed_by"].values()) - sum(borrower_data["owes"].values())

            return json.dumps({"users": [lender_data, borrower_data]})

        return None