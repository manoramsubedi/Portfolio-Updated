from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    text = models.TextField(null=True)
    display_img = models.ImageField(upload_to='media/user', null=True)
    img2 = models.ImageField(upload_to='media/user', null=True)

    def __str__(self):
        return self.name

class Social(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    link = models.URLField(null=True)
    social_img = models.ImageField(upload_to='media/social', null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    education_icon = models.ImageField(upload_to='media/icons', null=True)


    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=50)
    experience_icon = models.ImageField(upload_to='media/icons', null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    experience = models.ForeignKey(Experience,related_name='skill' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.name} - {self.experience.title}"
    
class Project(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField()
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    email = models.EmailField()
    link = models.URLField()

    def __str__(self):
        return self.email
    
    