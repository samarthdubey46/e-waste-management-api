# Generated by Django 3.2.6 on 2021-08-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='Awareness', max_length=100),
        ),
    ]
