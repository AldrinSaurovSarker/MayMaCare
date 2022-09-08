from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    topView = models.TextField(default=None, blank=True, null=True)
    listView = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
