from django.urls import path

from . import views
from .views import Home
app_name = 'chat'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    # path('<int:announcement_id>/', views.announcement_detail, name='announcement_detail'),
    # path('order/<str:username>', views.order, name='order'),
    # path('order_page/', views.order_page, name='order_page'),
    # path('order_history/<str:username>/', views.order_history, name='order_history'),

]
