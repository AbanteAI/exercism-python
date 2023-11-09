import json
class RestAPI:
    def __init__(self, database=None):
        self.database = database if database is not None else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                payload = json.loads(payload)
                users_info = [user for user in self.database['users'] if user['name'] in payload['users']]
            else:
                users_info = self.database['users']
            return json.dumps({"users": sorted(users_info, key=lambda x: x['name'])})
        return json.dumps({})

    def post(self, url, payload=None):
        if url == "/add":
            user_data = json.loads(payload)
            new_user = {
                "name": user_data['user'],
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database['users'].append(new_user)
            return json.dumps(new_user)
        elif url == "/iou":
            iou_data = json.loads(payload)
            lender = next(user for user in self.database['users'] if user['name'] == iou_data['lender'])
            borrower = next(user for user in self.database['users'] if user['name'] == iou_data['borrower'])
            amount = iou_data['amount']

            # Update the amount owed and owed_by
            lender['owed_by'][borrower['name']] = lender['owed_by'].get(borrower['name'], 0) + amount
            borrower['owes'][lender['name']] = borrower['owes'].get(lender['name'], 0) + amount

            # Adjust balances
            lender['balance'] += amount
            borrower['balance'] -= amount

            # If the borrower now owes nothing, remove the lender from the borrower's owes
            if borrower['owes'][lender['name']] == 0:
                del borrower['owes'][lender['name']]

            # If the lender is now owed nothing, remove the borrower from the lender's owed_by
            if lender['owed_by'][borrower['name']] == 0:
                del lender['owed_by'][borrower['name']]

            # If the borrower owes less than before, adjust the owes amount
            if borrower['owes'][lender['name']] < 0:
                lender['owed_by'][borrower['name']] += borrower['owes'][lender['name']]
                borrower['owes'][lender['name']] = 0

            # If the lender is owed less than before, adjust the owed_by amount
            if lender['owed_by'][borrower['name']] < 0:
                borrower['owes'][lender['name']] += lender['owed_by'][borrower['name']]
                lender['owed_by'][borrower['name']] = 0

            return json.dumps({"users": sorted([lender, borrower], key=lambda x: x['name'])})
        return json.dumps({})
