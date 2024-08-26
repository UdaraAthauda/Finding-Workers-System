from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
#from django.contrib.auth.models import Users, auth
import re

# Create your views here.
def base(request):
    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')
    workerAreas = WorkerArea.objects.all()

    if userConf:
        return render(request, 'basepage.html', {'confirm': userConf, 'userName': user_name, 'areas': workerAreas})

    else:
        return render(request, 'basepage.html', {'areas': workerAreas})


def register(request):
    userConf = request.session.get('confirm')

    if userConf:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST['name']
            contact = request.POST['contact']
            password = request.POST['password']
            cpass = request.POST['confpass']

            regex = '([0]{1}[7]{1}[01245678]{1}[0-9]{7})'

            if len(contact) == 10 and re.search(regex, contact):
                if password == cpass:
                    if Users.objects.filter(contact=contact).exists():
                        messages.error(request, 'This phone number is already registered')
                    else:
                        db_entry = Users(name=name, contact=contact, password=password)
                        db_entry.save()
                        regMsg = True
                        return render(request, 'register.html', {'form': Registration, 'successMsg': regMsg})
                        #return redirect('/login')
                else:
                    messages.error(request, 'Invalid password, Please confirm your password correctly!')
            else:
                messages.error(request, 'Not a valid phone number, Please enter a valid phone number!')

        return render(request, 'register.html', {'form': Registration})


def login(request):
    userConf = request.session.get('confirm')

    if userConf:
        return redirect('/')
    else:
        if request.method == 'POST':
            contact = request.POST['contact']
            password = request.POST['password']

            regex = '([0]{1}[7]{1}[01245678]{1}[0-9]{7})'

            if len(contact) == 10 and re.search(regex, contact):
                user = Users.objects.filter(contact=contact, password=password).exists()

                if user:
                    objects = Users.objects.all()

                    for user in objects:
                        if int(user.contact) == int(contact):
                            request.session['confirm'] = user.id
                            request.session['userDetails'] = user.name
                            userConf = request.session.get('confirm')
                            user_name = request.session.get('userDetails')

                            workerAreas = WorkerArea.objects.all()
                            return render(request, 'basepage.html', {'confirm': userConf, 'userName': user_name, 'areas': workerAreas})
                else:
                    messages.error(request, 'User does not exist, Please check you phone number and password are correct!')
            else:
                messages.error(request, 'Not a valid phone number, Please enter a valid phone number!')

        return render(request, 'login.html', {'form': Login})


def logout(request):
    del request.session['confirm']
    del request.session['userDetails']
    return redirect('/')


def userProfile(request):
    if request.method == 'POST':
        userid = request.session.get('confirm')

        name = request.POST['username']
        contact = request.POST['contact']

        if name:
            Users.objects.filter(id=userid).update(name=name)

        if contact:
            regex = '([0]{1}[7]{1}[01245678]{1}[0-9]{7})'

            if len(contact) == 10 and re.search(regex, contact):
                phoneNumber = int(contact)

                if Users.objects.filter(contact=contact).exists():
                    messages.error(request, 'This phone number is already registered')
                else:
                    Users.objects.filter(id=userid).update(contact=phoneNumber)
                    return redirect('/logout')
            else:
                messages.error(request, 'Not a valid phone number, Please enter a valid phone number!')

    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')
    userDetails = Users.objects.get(id=userConf)
    contact = userDetails.contact

    return render(request, 'userProfile.html', {'confirm': userConf, 'userName': user_name, 'contact': contact})


def deleteMsg(request):
    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')
    userDetails = Users.objects.get(id=userConf)
    contact = userDetails.contact

    errorFlag = True

    return render(request, 'userProfile.html', {'confirm': userConf, 'userName': user_name, 'contact': contact, 'errorFlag': errorFlag})


def deleteUser(request):
    userid = request.session.get('confirm')

    item_to_delete = Users.objects.get(id=userid)
    item_to_delete.delete()
    return redirect('/logout')


def changePassword(request):
    if request.method == 'POST':
        userid = request.session.get('confirm')
        userDetails = Users.objects.get(id=userid)
        oldPass = userDetails.password

        oldPassword = request.POST['oldpass']
        newpass = request.POST['newpass']
        cpass = request.POST['cpass']

        if oldPassword == oldPass:
            if newpass == cpass:
                Users.objects.filter(id=userid).update(password=newpass)
                return redirect('/logout')
            else:
                messages.error(request, 'Invalid password, Please confirm your password correctly!')
        else:
            messages.error(request, 'Entered old password is not matching, Please enter the right password!')


    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')

    return render(request, 'changePass.html', {'confirm': userConf, 'userName': user_name})


def addWorkerDetails(request):
    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')

    if request.method == 'POST':
        contact = request.POST['Contact_number']
        regex = '([0]{1}[7]{1}[01245678]{1}[0-9]{7})'

        if len(contact) == 10 and re.search(regex, contact):
            form = WorkerDetailForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                regMsg = True
                return render(request, 'workerDetail.html', {'confirm': userConf, 'userName': user_name, 'form': WorkerDetailForm, 'successMsg': regMsg})

        else:
            messages.error(request, 'Not a valid phone number, Please enter a valid phone number!')

    return render(request, 'workerDetail.html', {'confirm': userConf, 'userName': user_name, 'form': WorkerDetailForm})


def workerDetailDisplay(request, param):
    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')

    workerDetails = WorkerDetails.objects.filter(Working_areas=param, Accept=True)

    if workerDetails:
        return render(request, 'workerDetailDisplay.html', {'confirm': userConf, 'userName': user_name, 'details': workerDetails})

    else:
        messages.error(request, 'No worker details are available in this worker area')
        return render(request, 'workerDetailDisplay.html', {'confirm': userConf, 'userName': user_name})


def contactUs(request):
    userConf = request.session.get('confirm')
    user_name = request.session.get('userDetails')

    return render(request, 'contactUs.html', {'confirm': userConf, 'userName': user_name})