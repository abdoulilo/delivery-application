from django.urls import path
from .views import me, PingView

urlpatterns = [
    path('me/', me),
    path("ping/", PingView.as_view(), name="api-ping"),
]
