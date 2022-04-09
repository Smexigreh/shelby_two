from django.db import models

class Biology(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/biology/')

class Chemistry(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/chemistry/')

class English(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/english/')

class History(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/history/')

class Information(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/information/')

class Literature(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/literature/')

class Math(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/math/')

class OBZ(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/obz/')

class OID(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/oid/')

class Physics(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/physics/')

class Russian_language(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/russian_language/')

class Social_studies(models.Model):
    title = models.CharField(max_length=2, default=None)
    image = models.ImageField(upload_to='all_abs/social_studies/')

