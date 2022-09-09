from django.urls import path
from .views import loginViews, ListCustomerViews, LoginCustomer, CreateCustomer

urlpatterns = [
    path('', loginViews.as_view()),
    path('<int:id>', loginViews.as_view()),
    path('org_id/''<int:org_id>', ListCustomerViews.as_view()),
    path('login', LoginCustomer.as_view()),
    path('sign-up', CreateCustomer.as_view())
    
]
