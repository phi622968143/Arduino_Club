from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_staff_member = models.BooleanField(default=False)  # 用于区分幹部

    def __str__(self):
        return self.username