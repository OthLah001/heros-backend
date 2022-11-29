from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Hero(models.Model):
    user = models.ForeignKey("users.AppUser", related_name="heros", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    powers = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey("users.AppUser", related_name="ratingHeros", on_delete=models.CASCADE)
    hero = models.ForeignKey("heros.Hero", related_name="ratings", on_delete=models.CASCADE)
    rating = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])

    def __str__(self):
        return f"{self.hero.name} - {self.user.first_name} '{self.rating} star(s)'"