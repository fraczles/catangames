from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(**extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra):
        return self.create_user(phone_number, password=password, is_staff=True,
                                is_active=True, is_superuser=True, **extra)

    # TODO: Implement this
    @staticmethod
    def normalize_phone_number(phone_number):
        return phone_number

