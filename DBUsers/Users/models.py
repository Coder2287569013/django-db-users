from django.db import models

# Create your models here.
class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        USER = "USER", "user"

    name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)

    def __str__(self) -> str:
        return self.name, self.role