# Generated by Django 5.0.7 on 2024-08-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_skill_skill_icon_alter_skill_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='img2',
            field=models.ImageField(null=True, upload_to='media/user'),
        ),
        migrations.AddField(
            model_name='about',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
