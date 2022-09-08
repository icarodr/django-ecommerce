from django.db import models

class Music(models.Model):
    class Meta:
        db_table = 'Music'
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name
