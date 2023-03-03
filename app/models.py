from django.db import models



# Create your models here.

class Employee(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField( unique=True,max_length=254)
    phone= models.CharField( max_length=50)
    position=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    age= models.IntegerField()
    
    
class DataExcel(models.Model):
    excel_file=models.FileField( upload_to="exceldata", max_length=100)
    
    # def delete(self, *args, **kwargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.qr_code.name))
    #     super().delete(*args, **kwargs)

class error(models.Model):
    error_key=models.CharField( max_length=50)
    error=models.CharField( max_length=500)

