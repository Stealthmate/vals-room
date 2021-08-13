
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key=True)
