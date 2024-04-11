from django.db import models

# Create your models here.
class PGForm(models.Model):
    PG_Code=models.CharField(primary_key=True,max_length=10)
    Name=models.CharField(max_length=20)
    PG_Name=models.CharField(max_length=30)
    Address=models.CharField(max_length=50)
    Phn_no=models.CharField(max_length=10)
    rating=models.FloatField(null=True)
    description=models.CharField(max_length=1000,null=True)
class PGdetails(models.Model):
    PG_code=models.ForeignKey(PGForm,on_delete=models.CASCADE)
    Sharing=models.CharField(max_length=20)
    price=models.IntegerField()
    total_capacity=models.IntegerField()
    vacancies=models.IntegerField()
    image= models.ImageField(upload_to='images/',null=True)

class Registrations_pgs(models.Model):
    #id=models.CharField(primary_key=True,max_length=10,default='1')
    Registration_id=models.CharField(max_length=20)
    Full_name=models.CharField(max_length=25,null=False)
    Email = models.CharField(max_length=50,null=False)
    Mobile_number=models.CharField(max_length=10,null=False)
    sharing_person=models.CharField(max_length=25,null=True)
    price_person=models.IntegerField(null=True)