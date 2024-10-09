from django.urls import path
from womenapp.user_views import index,Rights,SingleRights,ViewLawyers,Petition_Form,ViewCmplaints
urlpatterns = [
    path('', index.as_view()),
    path('knowyourrights',Rights.as_view()),
    path('singlerights',SingleRights.as_view()),
    path('petition_form',Petition_Form.as_view()),
    path('view_lawyers',ViewLawyers.as_view()),
    path('ViewComplaints',ViewCmplaints.as_view())
]
def urls():
    return urlpatterns, 'user','user'