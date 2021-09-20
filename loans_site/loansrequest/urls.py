from django.urls import path
from django.contrib.auth import views
from . import views as myviews

urlpatterns = [
path('', myviews.loan_application, name='loan_application'),
path('accounts/login/', views.LoginView.as_view(), name='login'),
path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
path('accounts/loans/', myviews.loans_list, name='loans_list'),
path('accounts/loans/<int:pk>/', myviews.loans_edition, name='loans_edition'),
path('accounts/delete/<int:pk>', myviews.delete_item, name='delete_item'),
]