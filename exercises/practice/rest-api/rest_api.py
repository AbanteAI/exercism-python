class RestAPI:
    def __init__(self, database=None):
        self.database = database or {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                return {"users": [user for user in self.database["users"] if user["name"] in payload["users"]]}
            else:
                return {"users": self.database["users"]}
        return {}

    def post(self, url, payload=None):
        if url == "/add":
            new_user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(new_user)
            return new_user
        elif url == "/iou":
            lender = self.find_user(payload["lender"])
            borrower = self.find_user(payload["borrower"])
            amount = float(payload["amount"])

            self.update_owes_and_owed_by(lender, borrower, amount)
            self.update_balance(lender, borrower, amount)

            return {"users": sorted([lender, borrower], key=lambda x: x["name"])}

        return {}

    def find_user(self, name):
        for user in self.database["users"]:
            if user["name"] == name:
                return user
        return None

    def update_owes_and_owed_by(self, lender, borrower, amount):
        if borrower["name"] in lender["owed_by"]:
            lender["owed_by"][borrower["name"]] += amount
        else:
            lender["owed_by"][borrower["name"]] = amount

        if lender["name"] in borrower["owes"]:
            borrower["owes"][lender["name"]] += amount
        else:
            borrower["owes"][lender["name"]] = amount

    def update_balance(self, lender, borrower, amount):
        lender["balance"] += amount
        borrower["balance"] -= amount