from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number,password = None, **extrafields):
        if not phone_number:
            raise ValueError('Phone number required.')
        user = self.model(phone_number = phone_number, **extrafields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, phone_number, password = None, **extrafields):
        extrafields.setdefault('is_active', True)
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extrafields)