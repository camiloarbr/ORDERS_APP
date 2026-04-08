class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        raise Exception("User service unavailable")


class FakeUserRepository:
    def get_user_email(self, user_id):
        return f"user{user_id}@fake.local"