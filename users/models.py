from django.db import models
import crypt

# Create your models here.
class AppUser(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    creation_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    last_logged_in_date = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_password = self.password
    
    def save(self):
        if self.password != self.__original_password:
            self.password = crypt.crypt(self.password, crypt.METHOD_SHA256)
        super(AppUser, self).save()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
    
    def check_password(self, password):
        return crypt.crypt(password, self.password) == self.password