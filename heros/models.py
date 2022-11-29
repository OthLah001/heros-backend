from django.db import models

# Create your models here.
class Hero(models.Model):
    user = models.ForeignKey("users.AppUser", related_name="heros", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    powers = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name