from django.urls import path
from . import views

urlpatterns = [
      # This should render the HTML page
     path('chatbot/', views.chatbot_response, name='chatbot_response'),  # This handles the API requests
    path('', views.home, name='home'),
    path('chatbot-page/', views.chatbot_page, name='chatbot_page'),
    path('start_posture_tracking/', views.start_posture_tracking, name='start_posture_tracking'),
    path('aboutus/',views.AboutUs,name='AboutUs'),
    path('contactus/',views.ContactUs,name='ContactUs'),
    path('whyus/',views.WhyUs,name='WhyUs'),
    
]