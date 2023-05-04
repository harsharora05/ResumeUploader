from django.db import models


class Resume(models.Model):
 name = models.CharField(max_length=100)
 email = models.EmailField()
 mobile = models.PositiveIntegerField()
 profile = models.CharField(max_length=100)
 gender = models.CharField(max_length=100)
 state = models.CharField( max_length=50)
 pin = models.PositiveIntegerField()
 resume = models.FileField(upload_to='resumes/', blank=True)

