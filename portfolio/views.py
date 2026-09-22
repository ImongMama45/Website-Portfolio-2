from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from .models import Skill, Project
from .forms import ContactForm

class IndexView(TemplateView):
    template_name = "portfolio/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send Email
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject=f"Portfolio Contact from {name}",
                message=full_message,
                from_email=None,  # Uses DEFAULT_FROM_EMAIL
                recipient_list=['quertrussellalisan@gmail.com'],
            )
            
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('/#contact')
            
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

