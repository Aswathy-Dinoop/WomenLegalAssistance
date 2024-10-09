from django.urls import path
from womenapp.adv_views import index,Profile,UpdateProfile,ViewComplaints,acceptcomplaints,AcceptedComplaints,Rejectcomplaints

urlpatterns = [
    path('', index.as_view()),
    path('view_profile', Profile.as_view()),
    path('update_profile', UpdateProfile.as_view()),
    path('view_complaints', ViewComplaints.as_view()),
    path('Accept', acceptcomplaints.as_view()),
    path('Reject',Rejectcomplaints.as_view()),
    path('AcceptedComplaints',AcceptedComplaints.as_view(),name='AcceptedComplaints'),
    # path('reply',reply.as_view())
]
def urls():
    return urlpatterns, 'adv','adv'