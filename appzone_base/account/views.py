from django.contrib import auth
from django.shortcuts import render
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "index.html")

def search(request):

    if "q" in request.GET is not None:
        # print(q)
        query = None
        sponsor_name = None

        query = request.GET.get("q")
        sponsor_name = User.objects.all().filter(Q(username=query))
        print("===========")
        print(sponsor_name)
        print("===========")
        print(query)


        return render(request, "sponsor_val.html", {"sp": sponsor_name})

    else:
        return render(request, "sponsor_val.html")

def register(request, **kwargs):
    print("=========uname===========")
    print(kwargs["uname"])
    sp_name = kwargs["uname"]

    print("=========spame===========")
    print(sp_name)
    user =User.objects.get(username=sp_name)

    

    if request.method == "POST":

        sponsor_name = user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        e_mail = request.POST["e_mail"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            user = User.objects.create_user(
                sponsor_name=sponsor_name,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=e_mail,
                password=password,
            )
            user.save()
            print("registration success")
            return render(request, "reg_true.html")
        else:
            print("password mismatch")

    return render(request, "register.html", {"sp": sp_name})


def reg_true(request):

    return render(request, "reg_true.html")


def dashboard(request):
    current_user = request.user
    print(current_user.id)
    
    return render(request, "dashboard.html")

def login(request):
    if request.method == "POST":
        login_username = request.POST["username"]
        login_password = request.POST["password"]
        print(login_username)
        print(login_password)
        user = auth.authenticate(username=login_username, password=login_password,  )
        if user is not None and  user.is_superuser==False and user.is_active==True:
            auth.login(request, user)
            print("login success")
            messages.info(request, "login success------user")
            return render(request, "dashboard.html")
        else:
            print("user not Exists")
            messages.info(request, "user not Exists")
            return render(request, "login.html")

    else:
        print("user not created")
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


def manage_member(request):
      current_user = request.user
      user =  User.objects.filter(sponsor_name = current_user.id)
      member = User.objects.filter(sponsor_name = current_user.id,package__isnull=False)
      freeuser = User.objects.filter(sponsor_name = current_user.id,package__isnull=True)
      print(type(user))
      freeusercount=len(freeuser)
     

      print("===========================before==================")
    #   user.sort()
      usercount=len(member)
      print(user)
      print(len(user))

      return render(request, "manage-member.html", {"us":user , "usercount" : usercount , "freeusercount":freeusercount })


def profile_view(request):
      return render (request,"profile.html")

def profile_edit(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        e_mail = request.POST["e_mail"]
        username = request.POST['username']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        postal_code = request.POST['postal_code']
        about_me = request.POST['about_me']
        about_me = request.POST['about_me']
        image = request.FILES.get("image")

        if User.objects.filter(username=username,).exists():
                 User.objects.filter(username=username).update(first_name=first_name,last_name=last_name,email=e_mail,address=address,city=city,country=country,postal_code=postal_code,about_me=about_me,image=image)
                 return render (request,"profile.html")
    

    return render (request,"profile_edit.html")



def wallet_view(request):
    from bonus.models import bonus
    current_user = request.user
    log_data = transaction_log.objects.filter(username=current_user.id).all()
    bonus_data = bonus.objects.filter(username=current_user).all()
    context = {}
    context['bonus_data'] = bonus_data
    context['log_data'] = log_data
    return render(request, "wallet.html", context)

    
    
       
        
    

