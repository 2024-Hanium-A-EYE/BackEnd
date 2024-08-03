from django.db import models

# Define Data Format recevied from Front-END
class Front_Data_Model (models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Initiate_AI_Model (models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Control_AI_Model (models.Model):
    method = models.CharField(max_length=10)

    def __str_(self):
        return self.name
    

class Develop_Data_Model (models.Model):
    name = models.CharField(max_length=10)
    data = models.DateField()
    image = models.ImageField(upload_to='devevloping/images')

    def __str__(self):
        return self.name