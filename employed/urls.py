from django.urls import path
from .views import employedViews , employedbyemployed

urlpatterns = [
    path('', employedViews.as_view()),
    path('<int:id>', employedViews.as_view()),
    path('employed/<int:org_id>/', employedbyemployed.as_view()),
    
]
