from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from womenapp.models import PeopleRights,UserRegistration,AdvocateRegistration,Petition
from django.contrib import messages


class index(TemplateView):
    template_name='user/user_index.html'
class Rights(TemplateView):
    template_name='user/rights.html'
    def get_context_data(self, **kwargs):
        view_rights = PeopleRights.objects.all()
        context = {
            'view_rights':view_rights
        }
        return context
class SingleRights(TemplateView):
    template_name='user/single_rights.html'
    def get_context_data(self, **kwargs):
        context=super(SingleRights, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view = PeopleRights.objects.get(id=id1)
        context = {
            'view':view
        }
        return context
class ViewLawyers(TemplateView):
    template_name='user/view_adv.html'
    def get_context_data(self, **kwargs):
        context=super(ViewLawyers, self).get_context_data(**kwargs)
        id1=self.request.GET['id']
        view = PeopleRights.objects.get(pk=id1)
        lawyer=AdvocateRegistration.objects.filter(rights_id=id1)
        context = {
            'lawyer':lawyer
        }
        return context
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        lawyer = AdvocateRegistration.objects.filter(location__icontains=search)
        # lawyer = AdvocateRegistration.objects.filter(location__icontains=search)

        
        return render(request,'user/view_adv.html',{'lawyer':lawyer})
class Petition_Form(TemplateView):
    template_name='user/petition.html'
    def get_context_data(self, **kwargs):
        id1=self.request.GET['id']
        context=super(Petition_Form, self).get_context_data(**kwargs)
        ps = UserRegistration.objects.get(user_id=self.request.user.id)
        lawyer=AdvocateRegistration.objects.get(id=id1)
        context['ps'] = ps
        context['lawyer']=lawyer
        return context
    def post(self, request, *args, **kwargs):
        id1=self.request.GET['id']
        complaint = request.POST['complaint']
        ps = UserRegistration.objects.get(user_id=self.request.user.id)
        lawyer=AdvocateRegistration.objects.get(id=id1)
        abc=Petition()
        abc.complaint=complaint
        abc.user=ps
        abc.lawyer=lawyer
        abc.status='Complaint Submitted'
        abc.save()
        return redirect('/user')
class ViewCmplaints(TemplateView):
    template_name='user/complaint_status.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCmplaints, self).get_context_data(**kwargs) 
        abc=UserRegistration.objects.get(user_id=self.request.user.id)
        pro = Petition.objects.filter(user_id=abc.id)
        context['compl'] = pro  
        return context

class Payment(TemplateView):
    template_name="user/payment.html"
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)  
        user = Registration.objects.get(user_id=self.request.user.id)      
        cart = AddtoCart.objects.filter(status="Order Approved",user_id=user.id)
        total = 0
        for i in cart:
            total = total + int(i.price)
        context['asz'] = total
        context['cart'] = cart
        return context







        