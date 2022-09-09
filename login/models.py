from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='')
    phone_no = models.PositiveBigIntegerField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "login"
    
    def __str__(self):
        return self.name

