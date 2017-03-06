from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^soumettre$',TemplateView.as_view(template_name = 'francais/soumettre.html'), name='soumettre'), 
    url(r'^saved$', views.newSubmit, name="saved"),
    url(r'^About$', views.aboutUs, name="about"),
    url(r'^login$',views.formView, name="login"),
    url(r'^loggedin$', views.login, name= "loggedin"),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^journal', TemplateView.as_view(template_name = 'francais/jda.html'), name='JDA'),
    url(r'^payfailed$', TemplateView.as_view(template_name='francais/failed.html'), name='failed'),
#     url(r'^paysuccess$', views.paySuccess, name="paysuccess"),
 

]
