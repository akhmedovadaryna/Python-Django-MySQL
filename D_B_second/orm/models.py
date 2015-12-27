__author__ = 'darina'

from django.db import models

# Create your models here.


class FileForm(models.Model):
    name_f = models.CharField()
    size = models.IntegerField(min_value=1)
    type = models.CharField()
    user_name_u = models.CharField()
    Cloud_storage_idstorage = models.IntegerField()


    def __unicode__(self):
        return self.name_f


class userForm(models.Model):
    name_u = models.CharField()
    B_day= models.DateField()
    year= models.IntegerField(max_value=98, min_value=4)


    def __unicode__(self):
        return self.name_u



class CloudForm(models.Model):
    name  = models.CharField()
    date_s_add = models.DateTimeField()
    date_s_change = models.DateTimeField()


    def __unicode__(self):
        return self.name



class userForm_Edit(models.Model):
    name_u = models.CharField(required=False)
    B_day= models.DateField(required=False)
    year= models.IntegerField(required=False, min_value=4, max_value=98)


    def __unicode__(self):
        return self.name_u



class user_id_edit(models.Model):
     Name_key = models.CharField()


     def __unicode__(self):
        return self.Name_key



class FileForm_Edit(models.Model):
    name_f  = models.CharField(required=False)
    size= models.IntegerField(required=False)
    type = models.CharField(required=False)
    user_name_u = models.CharField(required=False)
    Cloud_storage_idstorage = models.IntegerField(required=False)


    def __unicode__(self):
        return self.name_f



class File_id_edit(models.Model):
     Name_key_f = models.IntegerField()


     def __unicode__(self):
        return self.Name_key_f



class File_del(models.Model):
     idFile = models.IntegerField()


     def __unicode__(self):
        return self.idFile



class Diapason(models.Model):
    first = models.IntegerField(min_value=1)
    last = models.IntegerField(min_value=1)


    def __unicode__(self):
        return self.first



class Diapason_1(models.Model):
    first = models.IntegerField(min_value=1)
    last = models.IntegerField(min_value=1)


    def __unicode__(self):
        return self.first



class Search(models.Model):
    search = models.CharField()
    search_1= models.CharField()


    def __unicode__(self):
        return self.search


