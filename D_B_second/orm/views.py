from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from db import DB_1
from .forms import *
import MySQLdb as mdb1


def filelist(request):

    db = DB_1()
    File = db.get_file_list()
    Cloud = db.get_Cloud_storage_list()
    User = db.get_user_list()
    form = Diapason()
    form1 = Diapason_1()
    search = Search()
    if request.method == 'POST':

        if request.POST['key'] == 'Diapason':
            form = Diapason(request.POST)
            D = db.diapason(request.POST['first'],request.POST['last'])
            return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'form': form, 'Dia': D,'form1': form1, 'search': search},)

        if request.POST['key'] == 'Diapason_1':
            form1 = Diapason_1(request.POST)
            D_1 = db.diapason_1(request.POST['first'],request.POST['last'])
            return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'Dia_1': D_1,'form1': form1, 'form': form, 'search': search},)

        if request.POST['key'] == 'Reset':
            db.load()
            return HttpResponseRedirect('/student/file/')

        if request.POST['key'] == 'Poisk':
            Poisk_user = db.poisk_1(request.POST['Poisk'])
            print request.POST
            return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'p':Poisk_user,'form1': form1,'form': form, 'search': search })

        if request.POST['key'] == 'Poisk_1':
            Poisk_cloud_name = db.poisk_2(request.POST['Poisk_1'])
            print request.POST
            return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'c':Poisk_cloud_name,'form': form,'form1': form1, 'search': search})

        if request.POST['key'] == 'search':
            search_1 = db.search_1(request.POST['search'],request.POST['search_1'])
            print request.POST
            return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'form': form, 'form1': form1, 'search': search, 'search_1': search_1})




    return render(request, 'filelist.html', {'File': File , 'Cloud_storage': Cloud, 'user':User, 'form': form, 'form1': form1, 'search': search})

def addfile(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            db = DB_1()
            db.save_file(request.POST['name_f'], request.POST['size'], request.POST['type'], request.POST['user_name_u'], request.POST['Cloud_storage_idstorage'])
            return HttpResponseRedirect('/student/file/')
    else:
        form = FileForm()
    return render(request, 'add.html', {'form': form})

def adduser(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            db = DB_1()
            print request.POST
            db.save_user(request.POST['name_u'], request.POST['B_day'], request.POST['year'])
            return HttpResponseRedirect('/student/file/')
    else:
        form = userForm()
    return render(request, 'add.html', {'form': form})

def addCloud_storage(request):
    if request.method == 'POST':
        form = CloudForm(request.POST)
        if form.is_valid():
            db = DB_1()
            print request.POST
            db.save_cloud(request.POST['name'], request.POST['date_s_add'], request.POST['date_s_change'])
            return HttpResponseRedirect('/student/file/')
    else:
        form = CloudForm()
    return render(request, 'add.html', {'form': form})

def change_u(request):
    if request.method == 'POST':
        user = user_id_edit(request.POST)

        if user.is_valid():
              form = userForm_Edit()
              return render(request, 'change.html', {'form': form,'name_u_edit': request.POST['Name_key']})
        form = userForm_Edit(request.POST)
        if form.is_valid():
            db = DB_1()
            db.change_user(request.POST['name_u'], request.POST['B_day'], request.POST['year'], request.POST['key'])
            return HttpResponseRedirect('/student/file/')
    else:
        user = user_id_edit()
    return render(request, 'change.html', {'user': user})


def change_f(request):
    if request.method == 'POST':
        file = File_id_edit(request.POST)

        if file.is_valid():
              form = FileForm_Edit()
              return render(request, 'change_file.html', {'form': form,'name_f_edit': request.POST['Name_key_f']})
        form = FileForm_Edit(request.POST)
        if form.is_valid():
            db = DB_1()
            db.change_file(request.POST['name_f'], request.POST['size'], request.POST['type'], request.POST['user_name_u'], request.POST['Cloud_storage_idstorage'], request.POST['key'])

            return HttpResponseRedirect('/student/file/')
    else:
        file = File_id_edit()
    return render(request, 'change_file.html', {'file': file})

def delet_f(request):
    if request.method == 'POST':
        file = File_del(request.POST)

        if file.is_valid():
            db = DB_1()
            db.delete(request.POST['idFile'])

            return HttpResponseRedirect('/student/file/')
    else:
        file = File_del()
    return render(request, 'delete.html', {'file': file})

