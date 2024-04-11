from django.shortcuts import render,redirect

def checkGroup(view_fun):
    def innerFun(request):
        if  request.user.is_superuser == True or request.user.groups.all()[0].name=='student':
            print(request.user.is_superuser)
            return view_fun(request)
        else:
            return redirect('studentloginurl')
    return innerFun


def checkGroup1(view_fun):
    def innerFun(request):
        if request.user.is_superuser == True or request.user.groups.all()[0].name=='owner':
            return view_fun(request)
        else:
            return redirect('pgloginurl')
    return innerFun