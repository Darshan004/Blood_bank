from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('requ',views.requ,name='requ'),
    path('request',views.request,name='request'),

    path('contact',views.contact,name='contact'),
    path('message',views.message,name='message'),

    path('about',views.about,name='about'),

    path('terms',views.terms,name='terms'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)