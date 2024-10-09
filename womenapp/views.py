from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from womenapp.models import UserType,UserRegistration,AdvocateRegistration,PeopleRights
from django.contrib import messages

# Create your views here.
class index(TemplateView):
    template_name='index.html'
class User_Reg(TemplateView):
    template_name='user_reg.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        password = request.POST['password']
        if not email.endswith('.com'):
            return render(request, 'user_reg.html', {'message': "Invalid email"})
        else: 

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'user_reg.html' , {'message': "already added the username or email"})
                
            else:
                
                user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                                is_staff='0', last_name='1')
                user.save()

                reg = UserRegistration()# call the model
                reg.user = user
                reg.name=name
                reg.email=email
                reg.phone = phone
                reg.location = location
                reg.password = password
                
                reg.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "user"
                usertype.save()
                # messages.success(request, 'Successfully Registered')
                # return redirect('/')
                # messages = "Registration Successfull"
                return render(request, 'index.html', {'message': "Successfully Registered"})
class adv_reg(TemplateView):
    template_name='adv_reg.html'
    def get_context_data(self, **kwargs):
        context = super(adv_reg, self).get_context_data(**kwargs)
        dept = PeopleRights.objects.all()
        context['rights'] = dept
        return context
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        lawyertype = request.POST['lawyertype']
        regnum = request.POST['regnum']
        image=request.FILES["image"]
        exp=request.POST['exp']
        qualification=request.POST['edu']
        location = request.POST['location']
        password = request.POST['password']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)

        if User.objects.filter(email=email):
           
            return render(request, 'adv_reg.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()

            reg = AdvocateRegistration()# call the model
            reg.user = user
            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.location = location
            reg.rights_id=lawyertype
            reg.regnum=regnum
            reg.exp=exp
            reg.qualification=qualification
            reg.image=obj
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "adv"
            usertype.save()
            # messages.success(request, 'Successfully Registered')
            return redirect('/')
class loginview(TemplateView):
    template_name='login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "adv":
                    return redirect('/adv')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})
