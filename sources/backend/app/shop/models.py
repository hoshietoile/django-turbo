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

class User(models.Model):
  class Meta:
    db_table = 'user'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(verbose_name='Name', max_length=20)
  email = models.CharField(verbose_name='Email', max_length=100)
  password = models.CharField(verbose_name='Password', max_length=20)
  password_confirm = models.CharField(verbose_name='PasswordConfirm', max_length=20)
  created_at = models.DateTimeField(verbose_name="CreatedAt", auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name="UpdatedAt", auto_now_add=True)
  deleted_at = models.DateTimeField(verbose_name="DeletedAt", auto_now_add=True)

class Auth(models.Model):
  class Meta:
    db_table = 'auth'

  id = models.UUIDField(primary_key=True, editable=False)
  name = models.CharField(verbose_name='AuthName', max_length=20)
  parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auths')