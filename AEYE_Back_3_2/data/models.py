from django.db import models

# Define Data Format recevied from Front-END
class DataModel (models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name