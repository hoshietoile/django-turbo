import uuid

from django.db import models

# Create your models here.

class Book(models.Model):
  class Meta:
    db_table = 'book'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(verbose_name='Title', max_length=20)
  price = models.IntegerField(verbose_name='Price', null=True, blank=True)
  created_at = models.DateTimeField(verbose_name='CreatedAt', auto_now_add=True)

  def __str__(self):
    return self.title