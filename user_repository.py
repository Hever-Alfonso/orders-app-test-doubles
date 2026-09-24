class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        # Simula que el servicio de usuarios está caído
        raise ConnectionError("User service unavailable")
