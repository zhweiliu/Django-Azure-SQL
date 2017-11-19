# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Popularinfo(models.Model):
    shop = models.TextField(db_column='Shop')  # Field name made lowercase.
    prodname = models.TextField(db_column='ProdName')  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10)  # Field name made lowercase.
    shipfee = models.CharField(db_column='ShipFee', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shorturl = models.CharField(db_column='ShortUrl', max_length=30)  # Field name made lowercase.
    popular = models.IntegerField(db_column='Popular')  # Field name made lowercase.
    inputtime = models.CharField(db_column='InputTime', max_length=6)  # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PopularInfo'


class Searchinfo(models.Model):
    userid = models.CharField(db_column='UserID', max_length=33, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KeyWord', max_length=50, blank=True, null=True)  # Field name made lowercase.
    miniprice = models.DecimalField(db_column='MiniPrice', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exceptword = models.CharField(db_column='ExceptWord', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inputtime = models.CharField(db_column='InputTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    inputdate = models.CharField(db_column='InputDate', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SearchInfo'


class Userinfo(models.Model):
    name = models.CharField(db_column='Name', max_length=10)  # Field name made lowercase.
    channel = models.IntegerField(db_column='Channel')  # Field name made lowercase.
    uid = models.TextField()  # Field name made lowercase.
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserInfo'

    def __str__(self):
        return '{name} : {uid} @ channel : {channel}'.format(name=str(self.name), uid=str(self.uid), channel=str(self.channel))

    def __unicode__(self):
        return '{name} : {uid} @ channel : {channel}'.format(name=str(self.name), uid=str(self.uid), channel=str(self.channel))