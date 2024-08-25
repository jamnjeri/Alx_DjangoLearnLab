from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
    ## Permissions and Groups Setup

    ### Custom Permissions
    # - The `Book` model has custom permissions:
    #   - `can_view`: Allows viewing books.
    #   - `can_create`: Allows creating new books.
    #   - `can_edit`: Allows editing existing books.
    #   - `can_delete`: Allows deleting books.

    ### User Groups
    # - **Editors**: Can create and edit books.
    # - **Viewers**: Can only view books.
    # - **Admins**: Have full control over books (view, create, edit, delete).

    ### Enforcing Permissions
    # - Permissions are enforced in views using the `@permission_required` decorator.
    # - For example, the `edit_book` view requires `can_edit` permission to access.
    class Meta:
        permissions = [
            ('can_view', 'Can View Book'),
            ('can_create', 'Can Create Book'),
            ('can_edit', 'Can Edit Book'),
            ('can_delete', 'Can Delete Book'),
        ]
    
# Custom User model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username