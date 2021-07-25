from eshop_contact.forms import CreateContactForm
from django.shortcuts import render
from .models import ContactUs
from eshop_settings.models import SiteSetting

# Create your views here.

def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)
    setting = SiteSetting.objects.first()

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message 
        contact_form = CreateContactForm()

    context = {
        "contact_form" : contact_form,
        "setting" : setting
    }
    return render(request, 'contact_us/contact_us_page.html', context)
