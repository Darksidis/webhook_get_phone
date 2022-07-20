from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from getphone.views import TutorialBotView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/jackpot/', csrf_exempt(TutorialBotView.as_view())),
]