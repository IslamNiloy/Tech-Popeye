
from django.contrib import admin
from django.urls import path
from tech_dash import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('home/',views.home_page,name='home'),

    path('base/',views.base_page,name='base'),

    path('about/',views.about_page,name='about'),
    path('service/',views.service_page,name='service'),
    path('management/',views.management_page,name='management'),
    path('blog/',views.blog_page,name='blog'),
    path('contact/',views.contact_page,name='contact'),
    path('contactform/',views.contact_form,name='contactform'),
    path('career/',views.career_page,name='career'),
    


]
