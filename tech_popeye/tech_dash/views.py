from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import CarouselItem,Feature,Service,ContactMessage
# Create your views here.


def home_page(request):
    carousel_items = CarouselItem.objects.all()
    features = Feature.objects.all()
    context = {'carousel_items': carousel_items, 'features': features}
    return render(request, 'index.html', context)




def base_page(request):
    return render(request,'base.html')



def about_page(request):
    return render(request,'about.html')



def service_page(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})


def management_page(request):
    return render(request,'management.html')

def blog_page(request):
    return render(request,'blog.html')

def contact_page(request):
    return render(request,'contact.html')
def career_page(request):
    return render(request,'career.html')


# @csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new ContactMessage object
        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()

        messages.success(request, 'Message sent successfully!')

        # Redirect to a success page or do something else
        return render(request, 'contact.html', {'message': 'Your form has been submitted successfully! We will contact with you soon.'}) 
    else:
        return render(request, 'contact.html',{'message': 'There is a problem'})