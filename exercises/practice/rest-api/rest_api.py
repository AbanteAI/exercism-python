class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}

    @property
    def balance(self):
        total_owed = sum(self.owes.values())
        total_owed_to = sum(self.owed_by.values())
        return total_owed - total_owed_to


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload is not None and "users" in payload:
                users = payload["users"]
                user_objects = [User(user) for user in users]
                sorted_user_objects = sorted(user_objects, key=lambda x: x.name)
                return {"users": sorted_user_objects}
            else:
                return {"users": []}
        else:
            return {}

    def post(self, url, payload=None):
        if url == "/add":
            if payload is not None and "user" in payload:
                new_user = User(payload["user"])
                return new_user.__dict__
        elif url == "/iou":
            if payload is not None and "lender" in payload and "borrower" in payload and "amount" in payload:
                lender = payload["lender"]
                borrower = payload["borrower"]
                amount = payload["amount"]
                if lender in self.database and borrower in self.database:
                    self.database[lender].owed_by[borrower] = amount
                    self.database[borrower].owes[lender] = amount
                    sorted_users = sorted([lender, borrower])
                    updated_users = [self.database[user] for user in sorted_users]
                    return {"users": updated_users}
        return {}