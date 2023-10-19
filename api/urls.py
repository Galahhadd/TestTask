from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (ApiLinks,
                    EmployeeViewSet,
                    TeamViewSet)

router = SimpleRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'team', TeamViewSet)
print(router.urls)

urlpatterns = [
    path('', ApiLinks),
    path('api/' ,include(router.urls))
]