"""minute_taker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^login/$', views.log, name='login'),
    url(r'^home/$', views.account_home, name='home'),
    url(r'^about/$', views.about_us, name='about'),
    url(r'^suggest-topics/$', views.suggest_topics_guest, name='suggest-topics-guest'),
    url(r'^statistics/', views.statistics, name='statistics'),
    url(r'start_meeting/$', views.start_meeting, name='start_meeting'),
    url(r'reschedule_meeting/$', views.reschedule_meeting, name='reschedule_meeting'),
    url(r'approve_topics/$', views.approve_topics, name='approve_topics'),
    url(r'suggest_topics/$', views.suggest_topics, name='suggest_topics'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'attendance/(\d+)/$', views.take_minutes_attendance, name='attendance'),
    url(r'topic_discussion/$', views.take_minutes_topics, name='topics'),
    url(r'upcoming_meeting_details/$', views.take_minutes_upcoming, name='upcoming'),
    url(r'summary/$', views.take_minutes_end_meeting, name='end_meeting'),
    url(r'comment/(\d+)/$', views.comment, name='comment'),
    url(r'tag/(\d+)/$', views.add_tag, name='tag'),
    url(r'vote/(\d+)/$', views.vote, name='vote'),
    url(r'votingOptions/(\d+)/$', views.votingOptions, name='votingOptions'),
    url(r'^join/$', views.join_meeting, name='join'),
    url(r'^change_password/(\d+)/$', views.change_password, name='change_pass'),
    url(r'^addtopic/$', views.addtopic, name='addtopic'),
    url(r'^assign/(\d+)/$', views.assigntask, name='assign')
]
