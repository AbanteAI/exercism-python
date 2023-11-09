import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database if database is not None else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload = json.loads(payload)
                users = [user for user in self.database["users"] if user["name"] in payload["users"]]
            else:
                users = self.database["users"]
            return json.dumps({"users": sorted(users, key=lambda x: x["name"])})
        return json.dumps({})

    def post(self, url, payload=None):
        if url == "/add":
            payload = json.loads(payload)
            new_user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database["users"].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            payload = json.loads(payload)
            lender = self._find_user(payload["lender"])
            borrower = self._find_user(payload["borrower"])
            amount = payload["amount"]

            # Update owed_by and owes for lender and borrower
            lender_owed_by = lender["owed_by"].get(borrower["name"], 0)
            borrower_owes = borrower["owes"].get(lender["name"], 0)
            new_lender_owed_by = lender_owed_by + amount - borrower_owes
            new_borrower_owes = borrower_owes + amount - lender_owed_by

            if new_lender_owed_by > 0:
                lender["owed_by"][borrower["name"]] = new_lender_owed_by
                borrower["owes"].pop(lender["name"], None)
            else:
                lender["owed_by"].pop(borrower["name"], None)

            if new_borrower_owes > 0:
                borrower["owes"][lender["name"]] = new_borrower_owes
                lender["owed_by"].pop(borrower["name"], None)
            else:
                borrower["owes"].pop(lender["name"], None)

            self._update_balances(lender)
            self._update_balances(borrower)

            updated_users = sorted([lender, borrower], key=lambda x: x["name"])
            return json.dumps({"users": updated_users})
        return json.dumps({})

    def _find_user(self, name):
        for user in self.database["users"]:
            if user["name"] == name:
                return user
        return None

    def _update_balances(self, user):
        # Calculate net owed amounts
        for name, amount in list(user["owes"].items()):
            if name in user["owed_by"]:
                if user["owes"][name] > user["owed_by"][name]:
                    user["owes"][name] -= user["owed_by"][name]
                    user["owed_by"].pop(name)
                elif user["owes"][name] < user["owed_by"][name]:
                    user["owed_by"][name] -= user["owes"][name]
                    user["owes"].pop(name)
                else:
                    user["owes"].pop(name)
                    user["owed_by"].pop(name)

        # Update balance
        user["balance"] = sum(user["owed_by"].values()) - sum(user["owes"].values())
