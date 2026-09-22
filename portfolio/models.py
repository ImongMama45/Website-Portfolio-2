from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Lead Developer, Full-Stack Engineer")
    tech_stack = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. Django, React, PostgreSQL")
    image = models.ImageField(upload_to='projects/')
    url_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
