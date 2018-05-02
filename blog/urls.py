##importing django function url and all of our views from the blog application

from django.conf.urls import url
from.import views

##add the url pattern to be used 
##assigining a view called post_list to the ^$ URL. this Regex will match ^ (a beginning)
##followed by $ (an end). so only an empty string will match
##and name='post_list' is the name of the URL that will be used to identify the new view
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]