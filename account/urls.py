 django.conf.urls import url
from . import views
from django.contrib.auth import views as loginViews



urlpatterns=[
		url(r'^login/$',
			loginViews.login,
			name="login"),

		url(r'^logout/$',
			loginViews.logout,
			name="logout"),
		

]