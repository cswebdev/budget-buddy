"""
URL configuration for the backend project.

This module sets up the URL routing for the Django project, including:
- Admin site URLs.
- API endpoints for users, their bank accounts, and nested credit/debit transactions using Django REST Framework's nested routers.

Routers:
- `router`: Registers the `UserViewSet` at the `/user/` endpoint.
- `user_accounts_router`: Registers the `BankAccountViewSet` nested under each user at `/user/<user_pk>/bankaccounts/`.
- `accounts_router`: Registers the `CreditTransactionViewSet` and `DebitTransactionViewSet` nested under each bank account at `/user/<user_pk>/bankaccounts/<bankaccount_pk>/credittransactions/` and `/user/<user_pk>/bankaccounts/<bankaccount_pk>/debittransactions/`.

Included URL patterns:
- `/admin/`: Django admin interface.
- `/user/`: User API endpoints.
- `/user/<user_pk>/bankaccounts/`: Bank account API endpoints for a user.
- `/user/<user_pk>/bankaccounts/<bankaccount_pk>/credittransactions/`: Credit transaction API endpoints for a user's bank account.
- `/user/<user_pk>/bankaccounts/<bankaccount_pk>/debittransactions/`: Debit transaction API endpoints for a user's bank account.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from user.views import UserViewSet
from bankaccounts.views import BankAccountViewSet
from creditTransaction.views import CreditTransactionViewSet
from debitTransaction.views import DebitTransactionViewSet

# Root router for users
router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

# Nested router for bank accounts under users
user_accounts_router = routers.NestedDefaultRouter(router, r"user", lookup="user")
user_accounts_router.register(
    r"bankaccounts", BankAccountViewSet, basename="user-bankaccounts"
)

# Nested router for transactions under bank accounts
accounts_router = routers.NestedDefaultRouter(
    user_accounts_router, r"bankaccounts", lookup="bankaccount"
)
accounts_router.register(
    r"credittransactions",
    CreditTransactionViewSet,
    basename="user-bankaccount-credittransactions",
)
accounts_router.register(
    r"debittransactions",
    DebitTransactionViewSet,
    basename="user-bankaccount-debittransactions",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(user_accounts_router.urls)),
    path("", include(accounts_router.urls)),
]
