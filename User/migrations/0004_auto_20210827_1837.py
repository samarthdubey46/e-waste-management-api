# Generated by Django 3.2.6 on 2021-08-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ContactNumber',
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='total_blogs',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
