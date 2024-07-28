from django.db import models

# Create your models here.

# Define Data Format recevied from Front-END
class DataModel (models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.name