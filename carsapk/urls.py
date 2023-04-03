
from django.urls import path,include
from . import views
from .models  import Cars_Dest
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = 'index'),
    path('fleet',views.fleet,name='fleet'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('blog_detail',views.blog_detail,name='blog_detail'),
    path('faq',views.faq,name='faq'),
    path('offers',views.offers,name='offers'),
    path('team',views.team,name='team'),
    path('terms',views.terms,name='terms'),
    path('testimonials',views.testimonials,name='testimonials'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('booknow',views.booknow,name='booknow'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)











   

   
