# Generated by Django 5.0.7 on 2024-08-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_social_social_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='education_icon',
            field=models.ImageField(null=True, upload_to='media/icons'),
        ),
        migrations.AddField(
            model_name='experience',
            name='experience_icon',
            field=models.ImageField(null=True, upload_to='media/icons'),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_icon',
            field=models.ImageField(null=True, upload_to='media/icons'),
        ),
    ]
