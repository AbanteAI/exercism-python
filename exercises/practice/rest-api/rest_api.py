class RestAPI:
    def __init__(self, database=None):
        self.database = database if database is not None else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                users = [user for user in self.database['users'] if user['name'] in payload['users']]
            else:
                users = self.database['users']
            return {"users": sorted(users, key=lambda x: x['name'])}
        return {}

import json

def post(self, url, payload=None):
    if payload:
        payload = json.loads(payload)
    if url == "/add":
        user = {
            "name": payload['user'],
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }
        self.database['users'].append(user)
        return user
    elif url == "/iou":
        lender = next(user for user in self.database['users'] if user['name'] == payload['lender'])
        borrower = next(user for user in self.database['users'] if user['name'] == payload['borrower'])
        amount = payload['amount']
        
        lender['owed_by'][borrower['name']] = lender['owed_by'].get(borrower['name'], 0) + amount
        borrower['owes'][lender['name']] = borrower['owes'].get(lender['name'], 0) + amount
        
        lender['balance'] += amount
        borrower['balance'] -= amount
        
        return {"users": sorted([lender, borrower], key=lambda x: x['name'])}
    return {}
