# Generated by Django 3.0.3 on 2020-03-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_upload_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(default='/media/photos/default.jpg', upload_to='photos/'),
        ),
    ]