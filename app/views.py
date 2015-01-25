from django.shortcuts import render
from app.models import Provider
# For email
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    providers = Provider.objects.order_by("-name")
    return render(request, 'app/index.html', {"providers": Provider})

# About Us page
def about(request):
    return render(request, "about.html")

# Contact Us page
# Using http://code.techandstartup.com/django/contact-form/ as template
def contact(request):
	# Create a blank array of possible errors to present
    errors = []
    if request.method == 'POST':
    	# Error for no subject
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        # Error for no message
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        # Error for no valid email address
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        # If there are no errors
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'info@sheltr.org'),
                ['info@sheltr.org'], #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    # Present the error if there was one
    return render(request, 'contact.html',
        {'errors': errors})

# Thanks for the email page
def thanks(request):
    return render_to_response('thanks.html')



