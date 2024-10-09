from django.shortcuts import redirect, render

from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from womenapp.models import AdvocateRegistration,Petition
from django.contrib import messages


class index(TemplateView):
    template_name='adv/adv_index.html'
class Profile(TemplateView):
    template_name='adv/profile.html'
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = AdvocateRegistration.objects.get(user_id=id1)
        context['profile'] = pro
        return context
class UpdateProfile(TemplateView):
    template_name='adv/upd_pro.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = AdvocateRegistration.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        exp = request.POST['exp']
        location = request.POST['location']
        phone = request.POST['phone'] 
        image = request.FILES['image']

        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        reg = AdvocateRegistration.objects.get(id=id3)# call the model
        reg.exp=exp
        reg.location=location
        reg.phone=phone
        reg.image = obj
        reg.save()
        # return redirect('/therapist')

        return render(request, 'adv/adv_index.html',{'message':"Successfully Updated"})
class ViewComplaints(TemplateView):
    template_name='adv/view_complaints.html'
    def get_context_data(self, **kwargs):
        context = super(ViewComplaints, self).get_context_data(**kwargs)
        usid = self.request.user.id
        compl = AdvocateRegistration.objects.get(user_id=usid)
        lawyer=compl.id
        com = Petition.objects.filter(status='Complaint Submitted',lawyer_id=lawyer)
        context['com'] = com
        return context
class acceptcomplaints(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        rqs = Petition.objects.get(pk=id)
        rqs.status = 'Complaint Accepted'
        rqs.save()
        return redirect('adv:AcceptedComplaints')
class Rejectcomplaints(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        rqs = Petition.objects.get(pk=id)
        rqs.status = 'Rejected'
        rqs.save()
        return redirect('/adv')
class AcceptedComplaints(TemplateView):
    template_name='adv/acceptedcomp.html'
    def get_context_data(self, **kwargs):
        context = super(AcceptedComplaints, self).get_context_data(**kwargs)
        usid = self.request.user.id
        compl = AdvocateRegistration.objects.get(user_id=usid)
        lawyer=compl.id
        com = Petition.objects.filter(lawyer_id=lawyer,status='Complaint Accepted')
        context['com'] = com
        return context
    def post(self, request, *args, **kwargs):
        obj=AdvocateRegistration.objects.get(user_id=self.request.user.id)
        id=request.POST['id']
        id2=request.POST['id2']
        var=Petition.objects.get(id=id2)
        reply=request.POST['reply']
        # abc=Problems.objects.get(id=id2)
        var.status='replied'
        var.reply=reply
        var.save()
        return render(request, 'adv/adv_index.html',{'message':"Replied"})
# class reply(TemplateView):
#     template_name='adv/reply.html'