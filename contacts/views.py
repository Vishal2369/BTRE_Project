from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        newContact = Contact(listing=listing, listing_id=listing_id, name=name,
                             email=email, phone=phone, message=message, user_id=user_id)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry to this listing')
                return redirect('/listings/' + listing_id)
        else:
            messages.error(request, 'You must login to make an inquiry')
            return redirect('/listings/' + listing_id)

        send_mail(
            'Property Listing Inquiry For ' + listing,
            'Client Name     : ' + name + '\n'
            'Client email    : ' + email + '\n'
            'Client Phone.no : ' + phone + '\n'
            'Client Message  : ' + message,

            'vk536197@gmail.com',
            [realtor_email, 'mongohuge@gmail.com'],
            fail_silently=False

        )

        newContact.save()

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/' + listing_id)
