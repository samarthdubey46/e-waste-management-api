# Generated by Django 3.2 on 2021-04-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ContactNumber',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
    ]