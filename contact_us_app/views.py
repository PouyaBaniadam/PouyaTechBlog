from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import *


def contact_us(request):
    contact_us_info = ContactUsInfo.objects.all().last()
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            subject = form.cleaned_data.get("subject")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            Message.objects.create(name=name, subject=subject, email=email, message=message)
            status_of_sent_message = "Your message has been sent successfully!✅"
            form = MessageForm()

            return render(request, "contact_us_app/contact.html",
                          context={"status_of_sent_message": status_of_sent_message,
                                   "contact_us_info": contact_us_info, "form": form})
        else:
            status_of_sent_message = "Something went wrong"

    else:
        form = MessageForm()
        status_of_sent_message = ''

    return render(request, "contact_us_app/contact.html",
                  context={"contact_us_info": contact_us_info, "form": form,
                           "status_of_sent_message": status_of_sent_message})
