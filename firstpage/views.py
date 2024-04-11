from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import PGForm,PGdetails,Registrations_pgs
from django.contrib.auth.models import Group,User
from .forms import PGModelForm,PGdetailsModelForm,RegisterUser,RegisterPg,GroupForm
from django.contrib import messages
from .decorators import checkGroup,checkGroup1
# Create your views here.

def studentlogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        validuser = authenticate(request, username=uname,password=pwd)
        if validuser != None:
            login(request,validuser)
            return redirect('pgdetailsurl')
        else:
            return redirect('studentloginurl')
    return render(request,'home/studentlogin.html')

def user_logout(request):
    logout(request)
    return redirect('studentloginurl')

def admin_logout(request):
    logout(request)
    return redirect('pgloginurl')

def studentsignup(request):
    emptyForm=RegisterUser()
    emptyForm1 = Group.objects.all()
    if request.method=='POST':
        dataForm=RegisterUser(request.POST)
        if dataForm.is_valid()==True:
            #dataForm.save()
            user = dataForm.save()
            group_id = request.POST.get('group')
            group = Group.objects.get(pk=group_id)
            user.groups.add(group)
            #messages.success(request,'User created')
            return redirect('studentloginurl')
        else:
            messages.error(request,'user creation failed')
            messages.error(request,dataForm.errors)
            return redirect('studentsignupurl')
    return render(request,'home/studentsignup.html',{'form':emptyForm,'form1':emptyForm1})

def firstpage(request):
    return render(request,'home/firstpage.html')

def pglogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        validuser = authenticate(request, username=uname,password=pwd)
        if validuser != None:
            login(request,validuser)
            request.session['username'] = uname
            return redirect('stdlisturl')
        else:
            return redirect('pgloginurl')
    return render(request,'home/pglogin.html')

def pgsignup(request):
    emptyForm = RegisterPg()
    emptyForm1 = Group.objects.all()
    
    if request.method == 'POST':
        dataForm = RegisterPg(request.POST)
        if dataForm.is_valid():
            user = dataForm.save()
            group_id = request.POST.get('group')
            group = Group.objects.get(pk=group_id)
            user.groups.add(group)
            request.session['username'] = user.username
            print(user.username)
            return redirect('pgmainurl')
        else:
            return render(request, 'home/pgsignup.html', {'form': emptyForm})
    return render(request, 'home/pgsignup.html', {'form': emptyForm, 'form1': emptyForm1})

def pgform(request):
    return render(request,'home/')

def pgmain(request):
    emptyForm=PGModelForm()
    username = request.session.get('username')
    if request.method=="POST":
        dataForm=PGModelForm(request.POST)
        if dataForm.is_valid()==True:
            #dataForm.instance.Name= username
            dataForm.save()
            #return render(request,'home/pgmain.html',{'form':emptyForm})
            return redirect('pgloginurl')
        else:
            return render(request,'home/pgmain.html',{'form':dataForm})
    return render(request,'home/pgmain.html',{'form':emptyForm})

def pgshare(request):
    emptyForm=PGdetailsModelForm()
    if request.method=="POST":
        dataForm=PGdetailsModelForm(request.POST,request.FILES)
        if dataForm.is_valid()==True:
            dataForm.save()
            return render(request,'home/pgshare.html',{'form':emptyForm})
        else:
            return render(request,'home/pgshare.html',{'form':dataForm})
    return render(request,'home/pgshare.html',{'form':emptyForm})

@checkGroup
@login_required(login_url='studentloginurl')
def pgdetails(request):
    s=PGdetails.objects.all()
    if request.method == 'POST':
        search=request.POST['search']
        data=PGForm.objects.filter(Address=search)
        t=[]
        for i in data:
            a=i.PG_Code
            total=(PGdetails.objects.filter(PG_code=a))
            for i in total:
                t.append(i)
        return render(request,'home/pgdetails.html',{'form':t,'myvar':1})
    return render(request,'home/pgdetails.html',{'form2':s,'myvar':0})

@login_required(login_url='studentloginurl')
def complete(request,eno):
    s=PGdetails.objects.get(id=eno)
    return render(request,'home/complete.html',{'data':s})

@login_required(login_url='studentloginurl')
def registerpg(request,eno):
    obj = PGdetails.objects.get(id=eno)
    rvac=obj.vacancies
    if rvac>0:
        if request.method == 'POST':
            rname = request.POST['name']
            if rname:  
                remail = request.POST['email']
                rmobile = request.POST['mobile']
                obj = PGdetails.objects.get(id=eno)
                rid = obj.PG_code.PG_Code
                rshare = obj.Sharing
                rprice = obj.price
                rvcan=rvac-1
                obj.vacancies=rvcan
                obj.save()
                Registrations_pgs.objects.create(Registration_id=rid,Full_name=rname,Email=remail,Mobile_number=rmobile,sharing_person=rshare,price_person=rprice)
            #return render(request,'home/registerpg.html',{'obj':obj})
                return redirect('pgdetailsurl')
            else:
                return redirect('pgdetailsurl')
    else:
        return redirect('pgdetailsurl')
    return render(request,'home/registerpg.html',{'obj':obj})
    
@checkGroup1
def stdlist(request):

    #total_details=Registrations_pgs.objects.all()
    # print(User.username)
    username = request.session.get('username')
    #pg=PGForm.objects.get(Name=username)
    t=PGForm.objects.get(Name=username)
    s=t.PG_Code
    total_details=Registrations_pgs.objects.filter(Registration_id=s)
    if len(total_details)>0:
        return render(request,'home/stdlist.html',{'res':total_details})
    return render(request,'home/stdlist.html',{'res':total_details,'t':t})
def deleteData(request,eno):
    #empObj=Employee.objects.get(empno=eno)
    obj = Registrations_pgs.objects.get(id=eno)
    rcode=obj.Registration_id
    rsha=obj.sharing_person
    #print(rcode,rsha)
    obj.delete()
    data=PGdetails.objects.filter(PG_code=rcode)
    #print(data[0].vacancies)
    print(data)
    for i in data:
        print(i.Sharing)
        if i.Sharing == rsha:
            print(i.vacancies)
            #i.vacancies+=1
            i.vacancies+=1
            print(i.vacancies)
            i.save()
        # a=i.Sharing
        # print(a)
        # #print(data.a)
        # total=(data.objects.filter(Sharing=rsha))
        # print(total)
        # total.vacancies+=1
    #return render(request,'DBApp/selectEmp.html',)
    return redirect('stdlisturl')