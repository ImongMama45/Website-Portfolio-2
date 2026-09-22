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

class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            # Enforce Singleton
            return
        super().save(*args, **kwargs)

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True, null=True)
    field_of_study = models.CharField(max_length=200, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.school_name} - {self.degree}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"

class Contact(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True) # Optional so forms don't need to know the profile ID
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"Message from {self.sender_name} - {self.sender_email}"

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.platform

class Award(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=200, blank=True, null=True)
    award_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.award_name

class Testimonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=200)
    person_position = models.CharField(max_length=200, blank=True, null=True)
    testimonial_text = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"Testimonial from {self.person_name}"

class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.certification_name
