from django.urls import path
from womenapp.admin_views import index,ViewUsers,ApproveLawyer,RemoveUser,Approve,AddRights,ViewRights,RemoveRights,LawyerList,RemoveLists
urlpatterns = [
    path('', index.as_view(),name='index'),
    path('view_users', ViewUsers.as_view()),
    path('approve_lawyer',ApproveLawyer.as_view()),
    path('RemoveUser',RemoveUser.as_view()),
    path('Approve',Approve.as_view()),
    path('add_rights', AddRights.as_view(),name='add_rights'),
    path('view_rights', ViewRights.as_view()),
    path('remove_rights',RemoveRights.as_view()),
    # path('upd_rights',UpdateRights.as_view()),
    path('LawyerList',LawyerList.as_view()),
    path('RemoveLists',RemoveLists.as_view())
]
def urls():
    return urlpatterns, 'admin','admin'