class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0.0

    def update_balance(self):
        total_owed_by_other_users = sum(self.owed_by.values())
        total_owed_to_other_users = sum(self.owes.values())
        self.balance = total_owed_by_other_users - total_owed_to_other_users

    def add_iou(self, lender, amount):
        if amount > 0:
            if lender in self.owed_by:
                self.owed_by[lender] += amount
            else:
                self.owed_by[lender] = amount
        elif amount < 0:
            if lender in self.owes:
                self.owes[lender
        self.balance = total_owed_by_other_users - total_owed_to_other_users

    def add_iou(self, lender, amount):
        if amount > 0:
            if lender in self.owed_by:
                self.owed_by[lender] += amount
            else:
                self.owed_by[lender] = amount
        elif amount < 0:
            if lender in self.owes:
                self.owes[lender] += abs(amount)
            else:
                self.owes[lender] = abs(amount)
        self.update_balance()

    def to_dict(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        }


class RestAPI:
    def __init__(self, database=None):
        self.database = database or {}

    def get(self, url, payload=None):
        if url == "/users":
            users = payload["users"]
            user_objects = []
            for user in users:
                if user in self.database:
                    user_objects.append(self.database[user].to_dict())
            return {"users": sorted(user_objects, key=lambda u: u["name"])}
        return {}

    def post(self, url, payload=None):
        if url == "/add":
            user_name = payload["user"]
            if user_name not in self.database:
                new_user = User(user_name)
                self.database[user_name] = new_user
                return new_user.to_dict()
        elif url == "/iou":
            lender_name = payload["lender"]
            borrower_name = payload["borrower"]
            amount = payload["amount"]
            if lender_name in self.database and borrower_name in self.database:
                lender = self.database[lender_name]
                borrower = self.database[borrower_name]
                lender.add_iou(borrower_name, amount)
                borrower.add_iou(lender_name, -amount)
                return {"users": [lender.to_dict(), borrower.to_dict()]}
        return {}