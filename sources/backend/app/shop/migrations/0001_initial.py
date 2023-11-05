# Generated by Django 4.2.7 on 2023-11-03 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
