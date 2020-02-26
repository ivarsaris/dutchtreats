from django.contrib.auth.models import User


class EmailAuth:

    """Authenticate a user by matching email and password"""

    def authenticate(self, username=None, password=None):

        """get the user from the email"""

        try:
            user = User.objects.get(email=username)

            """verify the password"""

            if user.check_password(password):
                return user

            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):

        """use Django authentication system to retrieve user"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:

                return user

            return None

        except User.DoesNotExist:
            return None
