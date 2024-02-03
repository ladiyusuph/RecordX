from django.db import models

class Record(models.Model):
    
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    branch = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    
    def __str__(self):
        return self.first_name + "   " + self.last_name
