from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import get_chatbot_advice
import threading
from .pose_detection import start_pose_detection

# This view handles the chatbot responses.
from django.http import JsonResponse
from .chatbot import get_chatbot_advice  # Import the function from your chatbot.py file

def chatbot_response(request):
    if request.method == 'POST':
        user_goal = request.POST.get('user_goal', '')
        message = request.POST.get('message', '')
        advice = get_chatbot_advice(user_goal, message)
        return JsonResponse({'response': advice})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.shortcuts import render

# New view to render the chatbot page
def chatbot_page(request):
    return render(request, 'trainer/chatbot.html')


# This view renders the chatbot page.

# This view renders the home page.
def home(request):
    return render(request, 'trainer/home.html')


# This view renders the posture tracking page.
def start_posture_tracking(request):
    # Start the posture detection process in a separate thread.
    thread = threading.Thread(target=start_pose_detection)
    thread.daemon = True  # Daemon threads close with the main process
    thread.start()
    
    # Inform the user that the tracking has started
    return render(request, 'trainer/start_posture_tracking.html', {'status': 'Tracking started!'})

def AboutUs(request):
     return render(request, 'trainer/aboutus.html')
    

def ContactUs(request):
    return render(request, 'trainer/contactus.html')
    

def WhyUs(request):

    return render(request, 'trainer/whyus.html')