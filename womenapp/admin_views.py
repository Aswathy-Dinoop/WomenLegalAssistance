from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from womenapp.models import User,UserRegistration,AdvocateRegistration,PeopleRights
from django.contrib import messages


class index(TemplateView):
    template_name='admin/admin_index.html'
class ViewUsers(TemplateView):
    template_name='admin/view_users.html'
    def get_context_data(self, **kwargs):
        view_users = UserRegistration.objects.all()
        context = {
            'view_users':view_users
        }
        return context
class ApproveLawyer(TemplateView):
    template_name='admin/approvelawyer.html'
    def get_context_data(self, **kwargs):
        context = super(ApproveLawyer,self).get_context_data(**kwargs)
        approveAdv = AdvocateRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['approveAdv'] = approveAdv
        return context
class LawyerList(TemplateView):
    template_name='admin/view_approved_adv.html'
    def get_context_data(self, **kwargs):
        context = super(LawyerList,self).get_context_data(**kwargs)
        approveAdv = AdvocateRegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['viewadv'] = approveAdv
        return context
class RemoveLists(View):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        pg=User.objects.get(id=id).delete()
       
        return redirect(request.META['HTTP_REFERER'],{'message':"Account Removed"})
class Approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Account Approved"})
class RemoveUser(View):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        pg=ADD_PG_INFO.objects.get(id=id).delete()
       
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
class AddRights(TemplateView):
    template_name='admin/add_rights.html'
    def post(self, request, *args, **kwargs):
        rights=request.POST['rights']
        image=request.FILES['image']
        desc=request.POST['desc']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        a=PeopleRights()
        a.rights=rights
        a.desc=desc
        a.image=obj
        a.save()
        return redirect('admin:add_rights')
class ViewRights(TemplateView):
    template_name='admin/view_rights.html'
    def get_context_data(self, **kwargs):
        view_rights = PeopleRights.objects.all()
        context = {
            'view_rights':view_rights
        }
        return context
class RemoveRights(View):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        pg=PeopleRights.objects.get(id=id).delete()
       
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})

# class UpdateRights(TemplateView):
#     template_name='admin/updrights.html'
#     def get_context_data(self, **kwargs):
#         context = super(UpdateRights, self).get_context_data(**kwargs)
#         id3 = self.request.GET['id']
#         pro =  PeopleRights.objects.get(id=id3)
#         context['upd'] = pro
#         return context
#     def post(self, request, *args, **kwargs):
#         id3 = self.request.GET['id']
#         rights=request.POST['rights']
#         image=request.FILES['image']
#         desc=request.POST['desc']
#         ob=FileSystemStorage()
#         obj=ob.save(image.name, image)
#         a=PeopleRights.objects.get(id=id3)
#         a.rights=rights
#         a.desc=desc
#         a.image=obj
#         a.save() 
#         return render(request, 'admin/index.html', {'message': "Successfully updated"})