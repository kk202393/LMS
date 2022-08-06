from django.contrib import admin
from django.urls import path
from LOAN import views
from django.contrib.auth import views as auth_views
from LOAN.forms import LoginForm


urlpatterns = [
    path("change_password/", views.change_password, name="change_password"),
    path("desbord/", views.desbord, name="desbord"),
    path("center_meeting/", views.center_meeting, name="center_meeting"),
    path("addCenterMeeting/", views.addCenterMeeting, name="addCenterMeeting"),
    path("collection_reverse/", views.collection_reverse, name="collection_reverse"),
    path(
        "cross_sell_cash_sell/", views.cross_sell_cash_sell, name="cross_sell_cash_sell"
    ),
    path(
        "add_cross_sell_cash_sell/",
        views.add_cross_sell_cash_sell,
        name="add_cross_sell_cash_sell",
    ),
    path("Credit_Bureau_Check/", views.Credit_Bureau_Check, name="Credit_Bureau_Check"),
    path("branchDayClose/", views.branchDayClose, name="branchDayClose"),
    path("region_view/", views.region_view, name="region_view"),
    path("loan/", views.loan, name="loan"),
    # path('', views.home, name='login'),
    path("region/", views.Region_field, name="region"),
    path("zone_view/", views.zone_view, name="zone_view"),
    path("zone/", views.one, name="zone"),
    path("center/", views.Center, name="center"),
    path("center_ID/", views.center_ID, name="center_ID"),
    path("Agent/", views.Agents, name="Agent"),
    path("Agent_user/", views.Agent_user, name="Agent_user"),
    path("customerKYC/", views.CustomerKYC, name="customerKYC"),
    path("loanCalculator/", views.loanCalculator, name="loanCalculator"),
    path("loanDetailsAmount/", views.loanDetailsAmount),
    path("AgentCustomer/", views.AgentCustomerKYC),
    path(
        "",
        auth_views.LoginView.as_view(
            next_page="desbord",
            template_name="../templates/index.html",
            authentication_form=LoginForm,
        ),
        name="signin",
    ),
]
