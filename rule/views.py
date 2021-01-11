from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')

    else:
        return render(request, 'login.html')


@login_required(login_url='/login/')
def home(request):
    request.session.set_expiry(900)
    return render(request, 'index.html')

'''
def upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['Rules']

        imported_data = dataset.load(new_persons.read(), format='xlsx')
    # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8]
            )
            value.save()

    return render(request, 'upload.html')

'''