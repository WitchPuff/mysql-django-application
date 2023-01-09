from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('admin/', views.admin, name='admin'),
    path('dealerLogin/', views.dealerLogin, name='dealerLogin'),
    path('market/', views.market, name='market'),
    path('dealer/', views.dealer, name='dealer'),
    path('dealerReg/', views.dealerReg, name='dealerReg'),
    path('search/', views.search, name='search'),
    path('custReg/', views.customerSurvey, name='custReg'),
    
    # path('StaffLogin/', views.staffLogin, name='staffLogin'),
    # path('StaffRegister/', views.insertStaff, name='insertStaff'),
    # path('work/', views.getStaff, name='getStaff'),
    # path('AddStaff/', views.addStaff, name='addStaff'),
    # path('deleteStaff/', views.deleStaff, name='deleStaff'),
    # path('editStaff/', views.editStaff, name='editStaff'),
    # path('clientManage/', views.getClient, name='getClient'),
    # path('RoomManage/', views.getRoom, name='getRoom'),
    # path('OrderManage/', views.getOrder, name='getOrder'),

]