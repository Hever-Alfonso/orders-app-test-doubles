class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        # Simula que el servicio de usuarios está caído
        raise ConnectionError("User service unavailable")


class FakeUserRepository:
    def get_user_email(self, user_id):
        # devuelve un email ficticio, sin depender de la API externa
        return f"user{user_id}@fake.local"
