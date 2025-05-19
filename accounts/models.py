import random
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class OneTimeCode(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    code      = models.CharField(max_length=6)
    created   = models.DateTimeField(auto_now_add=True)
    used      = models.BooleanField(default=False)

    def is_valid(self):
        return (
            not self.used and
            timezone.now() <= self.created + datetime.timedelta(minutes=5)
        )

    @classmethod
    def create_for_user(cls, user):
        """Generate a 6-digit code, save and return it."""
        code = f"{random.randint(0, 999999):06d}"
        return cls.objects.create(user=user, code=code)

