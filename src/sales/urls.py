from django.urls import path
from .views import (
	home_view, 
	SalesListView,
	)

app_name = 'sales'

urlpatterns = [
	path('',home_view,name='home'),
	path('list/',SalesListView.as_view(),name='list'), # need to add .as_view() for class based view
]