from django.urls import path
from airways import views
# from bhartiya_airway import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('Home', views.home, name='Home'),
    path('career', views.career, name='career'),
    path('contact_us', views.contactus, name='contact_us'),
    path('applynow', views.applynow, name='applynow'),
    path('contactdata', views.contactdata, name='contactdata'),
    path('about', views.about, name='about'),
    path('month',views.datatablemo,name='month'),
    path('today',views.datatableto,name='today'),
    path('week',views.datatablewe,name='week'),
    path('datatable',views.datatable,name='datatable'),
    path('dashboard',views.dashboard,name='dashboard')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)