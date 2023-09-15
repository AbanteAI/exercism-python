class RestAPI:
    def __init__(self, database=None):
        pass

    def get(self, url, payload=None):
        pass

    def post(self, url, payload=None):
        pass
class RestAPI:
    def __init__(self, database=None):
        self.users = {}

    def get(self, url, payload=None):
        if url == "/users":
            return self.get_users(payload)

    def post(self, url, payload=None):
        if url == "/add":
            return self.create_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)

    def get_users(self, payload):
        if payload and "users" in payload:
            users = payload["users"]
            user_objects = [self.users[user] for user in users if user in self.users]
            user_objects.sort(key=lambda x: x["name"])
            return {"users": user_objects}
        else:
            user_objects = list(self.users.values())
            user_objects.sort(key=lambda x: x["name"])
            return {"users": user_objects}

    def create_user(self, payload):
        if payload and "user" in payload:
            user = payload["user"]
            if user not in self.users:
                self.users[user] = {
                    "name": user,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                return self.users[user]

    def create_iou(self, payload):
        if payload and "lender" in payload and "borrower" in payload and "amount" in payload:
            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = payload["amount"]
            if lender in self.users and borrower in self.users:
                lender_obj = self.users[lender]
                borrower_obj = self.users[borrower]
                if lender != borrower:
                    lender_obj["owes"].setdefault(borrower, 0.0)
                    borrower_obj["owed_by"].setdefault(lender, 0.0)
                    lender_obj["owes"][borrower] += amount
                    borrower_obj["owed_by"][lender] += amount
                    lender_obj["balance"] -= amount
                    borrower_obj["balance"] += amount
                    return {"users": [lender_obj, borrower_obj]}