from django.contrib import admin
from .models import Skill, Project, Profile, Education, Experience, Contact, SocialLink, Award, Testimonial, Certification

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order', 'name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order', 'title')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'start_year', 'end_year')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'start_date', 'end_date', 'is_current')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'sent_at')
    readonly_fields = ('sender_name', 'sender_email', 'subject', 'message', 'sent_at')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_order')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('award_name', 'organization', 'award_year')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'is_visible')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('certification_name', 'issuing_organization', 'issue_date')
