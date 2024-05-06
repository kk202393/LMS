# middleware.py
from django.shortcuts import redirect
from django.utils import timezone
from django.conf import settings
import datetime

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')

            # Convert last_activity from string to datetime object
            if last_activity_str:
                last_activity = datetime.datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S')
                last_activity = last_activity.replace(tzinfo=timezone.utc)  # Make it aware of UTC
            else:
                last_activity = None

            # Check if last activity timestamp exists and if the session has expired
            if last_activity and (timezone.now() - last_activity).total_seconds() > 60:
                # Redirect to the login page
                return redirect("")

            # Update last activity timestamp in the session
            request.session['last_activity'] = str(timezone.now())

        return response
