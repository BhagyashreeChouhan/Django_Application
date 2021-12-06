from django.shortcuts import render, redirect  # For Render and Redireting to Function views
from .models import User
from .forms import UserForm


# Create your views here.
def UserList(request):
    user = User.objects.all();  # Create Object of Wish Class Model
    params = {'users': user}  # Create Parameter to Send To View
    return render(request, 'users.html', params)  # Return Wishes To The Html Page


def CreateUser(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('UserList')
    return render(request, 'userForm.html', {'form': form})

def UpdateUser(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('UserList')
    return render(request, 'userForm.html', {'form': form, 'users': user})


def DeleteUser(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('UserList')
    return render(request, 'DeleteConfirm.html', {'user': user})

def Search(request,text):
    user=User.objects.filter()
