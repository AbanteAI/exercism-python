import json
class RestAPI:
    def __init__(self, database=None):
        self.database = database or {"users": []}

    def get(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
        if url == "/users":
            return self.get_users(payload)
            return self.get_users(payload)
    def post(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
        if url == "/add":
            return self.create_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)
        if url == "/add":
            return self.create_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)

    def create_user(self, payload):
        new_user = {
            "name": payload["user"],
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }
        self.database["users"].append(new_user)
        return {"users": [new_user]}

    def create_iou(self, payload):
        lender = self.get_user(payload["lender"])
        borrower = self.get_user(payload["borrower"])
        amount = payload["amount"]

        if borrower["name"] in lender["owed_by"]:
            lender["owed_by"][borrower["name"]] -= amount
            borrower["owes"][lender["name"]] -= amount
        else:
            lender["owes"].setdefault(borrower["name"], 0)
            lender["owes"][borrower["name"]] += amount
            borrower["owed_by"].setdefault(lender["name"], 0)
            borrower["owed_by"][lender["name"]] += amount

        lender["balance"] += amount
        borrower["balance"] -= amount

        return {"users": sorted([lender, borrower], key=lambda x: x["name"])}

    def get_users(self, payload):
        if payload:
            users = [self.get_user(name) for name in payload["users"]]
        else:
            users = self.database["users"]
        return {"users": sorted(users, key=lambda x: x["name"])}

    def get_user(self, name):
        return next(user for user in self.database["users"] if user["name"] == name)