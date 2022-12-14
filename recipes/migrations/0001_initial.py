# Generated by Django 4.0.2 on 2022-02-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('ingredients', models.TextField(max_length=1600)),
                ('recipe', models.TextField(max_length=2400)),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
