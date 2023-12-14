from django.db import models

# Create your models here.
class reg(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    number=models.CharField(max_length=20)

class log(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    # class Meta:
    #     verbose_name_plural='regs'
    # class Meta:
    #     verbose_name_plural='logs'  
    def __str__(self):
        return self.name