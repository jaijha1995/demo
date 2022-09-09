from django.db import models

# Create your models here.
class employed(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    Designation  = models.CharField(max_length=255)
    salary = models.PositiveBigIntegerField()

    class Meta:
        db_table = "employed"
    
    def __str__(self):
        return self.name
