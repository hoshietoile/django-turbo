# Generated by Django 4.2.7 on 2023-11-05 11:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('password_confirm', models.CharField(max_length=20, verbose_name='PasswordConfirm')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='UpdatedAt')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='DeletedAt')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='AuthName')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auths', to='shop.user')),
            ],
            options={
                'db_table': 'auth',
            },
        ),
    ]
