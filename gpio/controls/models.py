from django.db import models

# Create your models here.
class control(models.Model):
    pin = models.IntegerField()
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
