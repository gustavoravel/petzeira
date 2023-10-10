from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tente encontrar um usuário com o endereço de e-mail fornecido
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Se o usuário não for encontrado, retorne None
            return None

        # Verifique a senha do usuário
        if user.check_password(password):
            return user
        return None

