# -*- coding: UTF-8 -*-
'''
Created on 2012-11-5

@author: tianwei
'''

from django.db import models
from users.models import UserProfile

class ActiveKeyInfo(models.Model):
    """
    Active Key base table
    """
    keyValue    = models.CharField(max_length = 40,unique=True)
    totalCount  = models.IntegerField()
    leftCount   = models.IntegerField()
    isAlreadLocated = models.BooleanField(default=True)  
    
    def __unicode__(self):
        return self.keyValue

class LanguageEnum(models.Model):
    """
    Language Enum for Chemistry 
    """    
    languageStr = models.CharField(max_length = 50)
    
    #Pre-loading data
    #TODO : Default create 
    
    def __unicode__(self):
        return self.languageStr    

Chinese_Name_Label = "Chinese"
English_Name_Label = "English"

class ActiveHistory(models.Model):
    """
    Active history (for calculate)
    """
    user        = models.ForeignKey(UserProfile)
    activeIP    = models.URLField()
    activeTime  = models.DateTimeField()
    antActiveIP = models.URLField(blank=True,null=True)
    antActiveTime = models.DateTimeField(blank=True,null=True)
    activekey   = models.ForeignKey(ActiveKeyInfo)
    
    def __unicode__(self):
        return '%s'%(self.user)
    
class ModelInfo(models.Model):
    """
    Chemistry Models Information
    """
    modelName = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.modelName

class CompoundInfo(models.Model):
    """
    Smiles and CAS compound
    """
    smilesInfo = models.CharField(max_length = 200,primary_key=True)
    casInfo    = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return '%s' % (self.smilesInfo)    

class CompoundName(models.Model):
    """
    Smiles and CAS name compound
    """
    simlesInfo = models.ForeignKey(CompoundInfo)
    nameStr = models.CharField(max_length = 500)
    languageID = models.ForeignKey(LanguageEnum)
    isDefault = models.BooleanField()
    
    def __unicode__(self):
        return '%s' %(self.nameStr)
    
class CalculateHistory(models.Model):
    """
    Calculate history
    """   
    user        = models.ForeignKey(UserProfile)
    calculateStartTime = models.DateTimeField()
    calculateEndTime   = models.DateTimeField(blank=True,null=True)
    paramInfo   = models.TextField(blank=True)
    result      = models.TextField(blank=True)
    isFinished  = models.BooleanField(blank=True)
    modelInfo   = models.ForeignKey(ModelInfo)
    smilesInfo  = models.ForeignKey(CompoundInfo)       #Maybe wrong
    
    def __unicode__(self):
        return '%s' %(self.user)    
    

    
    
    
    
    
    