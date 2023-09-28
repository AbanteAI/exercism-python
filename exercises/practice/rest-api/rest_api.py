class RestAPI:
    def __init__(self, database=None):
        self.database = database if database else {"users": []}

    def get(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
        if url == "/users":
            if payload:
                users = [user for user in self.database["users"] if user["name"] in payload["users"]]
            else:
                users = self.database["users"]
            return {"users": sorted(users, key=lambda x: x["name"])}
        return {}

    def post(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
        if url == "/add":
            new_user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(new_user)
            return new_user

        if url == "/iou":
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

        return {}
        return {}

        return {}
            new_user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(new_user)
            return new_user

        if url == "/iou":
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

        return {}
