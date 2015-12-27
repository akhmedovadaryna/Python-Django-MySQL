from django import forms

class FileForm(forms.Form):
    name_f = forms.CharField()
    size = forms.IntegerField(min_value=1)
    type = forms.CharField()
    user_name_u = forms.CharField()
    Cloud_storage_idstorage = forms.IntegerField()

class userForm(forms.Form):
    name_u = forms.CharField()
    B_day= forms.DateField()
    year= forms.IntegerField(max_value=98, min_value=4)

class CloudForm(forms.Form):
    name  = forms.CharField()
    date_s_add = forms.DateTimeField()
    date_s_change = forms.DateTimeField()

class userForm_Edit(forms.Form):
    name_u = forms.CharField(required=False)
    B_day= forms.DateField(required=False)
    year= forms.IntegerField(required=False, min_value=4, max_value=98)

class user_id_edit(forms.Form):
     Name_key = forms.CharField()

class FileForm_Edit(forms.Form):
    name_f  = forms.CharField(required=False)
    size= forms.IntegerField(required=False)
    type = forms.CharField(required=False)
    user_name_u = forms.CharField(required=False)
    Cloud_storage_idstorage = forms.IntegerField(required=False)

class File_id_edit(forms.Form):
     Name_key_f = forms.IntegerField()

class File_del(forms.Form):
     idFile = forms.IntegerField()

class Diapason(forms.Form):
    first = forms.IntegerField(min_value=1)
    last = forms.IntegerField(min_value=1)

class Diapason_1(forms.Form):
    first = forms.IntegerField(min_value=1)
    last = forms.IntegerField(min_value=1)

class Search(forms.Form):
    search = forms.CharField()
    search_1=forms.CharField()

