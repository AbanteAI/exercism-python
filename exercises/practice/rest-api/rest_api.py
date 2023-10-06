class RestAPI:
    def __init__(self, database=None):
        self.database = database if database else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload = json.loads(payload)
                users = [user for user in self.database["users"] if user["name"] in payload["users"]]
            else:
                users = self.database["users"]
            return {"users": sorted(users, key=lambda x: x["name"])}
            if payload:
                users = [user for user in self.database["users"] if user["name"] in payload["users"]]
            else:
                users = self.database["users"]
            return {"users": sorted(users, key=lambda x: x["name"])}

    def post(self, url, payload=None):
        if url == "/add":
            payload = json.loads(payload)
            user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(user)
            return user
        elif url == "/iou":
            lender = next(user for user in self.database["users"] if user["name"] == payload["lender"])
            borrower = next(user for user in self.database["users"] if user["name"] == payload["borrower"])
            amount = payload["amount"]

            if borrower["name"] in lender["owed_by"]:
                lender["owed_by"][borrower["name"]] += amount
            else:
                lender["owed_by"][borrower["name"]] = amount

            if lender["name"] in borrower["owes"]:
                borrower["owes"][lender["name"]] += amount
            else:
                borrower["owes"][lender["name"]] = amount

            lender["balance"] += amount
            borrower["balance"] -= amount

            return {"users": sorted([lender, borrower], key=lambda x: x["name"])}
