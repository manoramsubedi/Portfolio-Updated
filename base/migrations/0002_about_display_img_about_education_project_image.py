# Generated by Django 5.0.7 on 2024-08-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='display_img',
            field=models.ImageField(null=True, upload_to='images/user'),
        ),
        migrations.AddField(
            model_name='about',
            name='education',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
