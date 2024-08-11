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
        return f"{self.name}, {self.role}"

class Task(models.Model):
    class Status(models.TextChoices):
        DONE = "DONE", "done"
        PROCESSING = "PROCESSING", "processing"
        NO_WORK = "NO WORK", "no work"

    status = models.CharField(max_length=100, choices=Status.choices, default=Status.NO_WORK)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.title}, {self.status}"