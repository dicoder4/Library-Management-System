from models.user_model import users_collection

class UserService:
    def get_all_users(self):
        return list(users_collection.find({}, {"_id": 0}))
