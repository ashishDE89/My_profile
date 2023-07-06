from django.db import models

# Create your models here.
class resumes(models.Model):
    name = models.CharField(max_length=50)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")