from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings ### added for marker
from django.contrib.gis.db import models ###

def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

#marker # HERE CAN BE ADDED MORE FIELDS
class Marker(models.Model):
    """A marker with name and location."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length=255) #local name
    location = models.PointField()

    def __str__(self):
        """Return string representation."""
        return self.name