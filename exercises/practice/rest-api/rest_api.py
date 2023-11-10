import json
    def __init__(self, database=None):
        self.database = database if database is not None else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                users_info = self._get_users_info(payload)
            else:
                users_info = self._get_all_users_info()
            return users_info
        return {}

    def post(self, url, payload=None):
        if url == "/add" and payload:
            return self._create_user(payload)
        elif url == "/iou" and payload:
            return self._create_iou(payload)
        return {}
    def _get_all_users_info(self):
        return {"users": sorted(self.database["users"], key=lambda x: x["name"])}

    def _get_users_info(self, payload):
        requested_users = payload.get("users", [])
        users_info = {"users": []}
        for user in self.database["users"]:
            if user["name"] in requested_users:
                users_info["users"].append(user)
        users_info["users"] = sorted(users_info["users"], key=lambda x: x["name"])
        return users_info

    def _create_user(self, payload):
        payload = json.loads(payload)
        new_user = {
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }
        self.database["users"].append(new_user)
        return new_user

    def _create_iou(self, payload):
        payload = json.loads(payload)
        lender_name = payload["lender"]
        borrower_name = payload["borrower"]
        amount = payload["amount"]
        lender, borrower = None, None
        # ... rest of the method remains unchanged
        borrower_name = payload["borrower"]
        amount = payload["amount"]
        lender, borrower = None, None

        for user in self.database["users"]:
            if user["name"] == lender_name:
                lender = user
            elif user["name"] == borrower_name:
                borrower = user

        if lender and borrower:
            lender["owed_by"][borrower_name] = lender["owed_by"].get(borrower_name, 0) + amount
            borrower["owes"][lender_name] = borrower["owes"].get(lender_name, 0) + amount
            self._update_balances(lender, borrower)

            return {"users": sorted([lender, borrower], key=lambda x: x["name"])}
        return {}

    def _update_balances(self, lender, borrower):
        lender["balance"] = sum(lender["owed_by"].values()) - sum(lender["owes"].values())
        borrower["balance"] = sum(borrower["owed_by"].values()) - sum(borrower["owes"].values())
        for user in lender["owes"]:
            if user in lender["owed_by"]:
                min_value = min(lender["owes"][user], lender["owed_by"][user])
                lender["owes"][user] -= min_value
                lender["owed_by"][user] -= min_value
                if lender["owes"][user] == 0:
                    del lender["owes"][user]
                if lender["owed_by"][user] == 0:
                    del lender["owed_by"][user]
        for user in borrower["owes"]:
            if user in borrower["owed_by"]:
                min_value = min(borrower["owes"][user], borrower["owed_by"][user])
                borrower["owes"][user] -= min_value
                borrower["owed_by"][user] -= min_value
                if borrower["owes"][user] == 0:
                    del borrower["owes"][user]
                if borrower["owed_by"][user] == 0:
                    del borrower["owed_by"][user]
        lender["balance"] = sum(lender["owed_by"].values()) - sum(lender["owes"].values())
        borrower["balance"] = sum(borrower["owed_by"].values()) - sum(borrower["owes"].values())
