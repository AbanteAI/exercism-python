class RestAPI:
    def __init__(self, database=None):
        pass

    def get(self, url, payload=None):
        if url == "/users":
            return self.get_users(payload)
        return {}

    def post(self, url, payload=None):
        if url == "/add":
            return self.add_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)
        return {}

    def get_users(self, payload):
        users = payload.get("users", [])
        return {"users": self.get_user_objects(users)}

    def add_user(self, payload):
        payload = json.loads(payload)
        user = payload.get("user")
        if user:
            return self.create_user(user)
        return {}

    def create_iou(self, payload):
        lender = payload.get("lender")
        borrower = payload.get("borrower")
        amount = payload.get("amount")
        if lender and borrower and amount:
            return self.update_user_balances(lender, borrower, amount)
        return {}

    def get_user_objects(self, users):
        return sorted([self.get_user_object(user) for user in users], key=lambda x: x["name"])

    def get_user_object(self, user):
        return {
            "name": user,
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }

    def create_user(self, user):
        return self.get_user_object(user)

    def update_user_balances(self, lender, borrower, amount):
        lender_obj = self.get_user_object(lender)
        borrower_obj = self.get_user_object(borrower)
        lender_obj["owed_by"][borrower] = lender_obj["owed_by"].get(borrower, 0.0) + amount
        borrower_obj["owes"][lender] = borrower_obj["owes"].get(lender, 0.0) + amount
        lender_obj["balance"] += amount
        borrower_obj["balance"] -= amount
        return {"users": [lender_obj, borrower_obj]}
