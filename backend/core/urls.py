"""
URL configuration for the backend project.

This module sets up the URL routing for the Django project, including:
- Admin site URLs.
- API endpoints for bank accounts and their nested credit transactions using Django REST Framework's nested routers.

Routers:
- `router`: Registers the `BankAccountViewSet` at the `/bankaccounts/` endpoint.
- `accounts_router`: Registers the `CreditTransactionViewSet` nested under each bank account at `/bankaccounts/<bankaccount_pk>/credittransactions/`.

Included URL patterns:
- `/admin/`: Django admin interface.
- `/bankaccounts/`: Bank account API endpoints.
- `/bankaccounts/<bankaccount_pk>/credittransactions/`: Credit transaction API endpoints nested under a specific bank account.
URL configuration for backend project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from bankaccounts.views import BankAccountViewSet
from creditTransaction.views import CreditTransactionViewSet

router = routers.DefaultRouter()
router.register(r"bankaccounts", BankAccountViewSet, basename="bankaccount")

accounts_router = routers.NestedDefaultRouter(
    router, r"bankaccounts", lookup="bankaccount"
)
accounts_router.register(
    r"credittransactions",
    CreditTransactionViewSet,
    basename="bankaccount-credittransactions",
)
accounts_router.register(
    r"debittransactions",
    CreditTransactionViewSet,
    basename="bankaccount-debittransactions",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(accounts_router.urls)),
]
