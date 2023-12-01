from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=70, null=False, blank=False)
    address=models.CharField(max_length=70, null=False, blank=False)
    phone=models.CharField(max_length=70, null=False, blank=False)
    trn_number=models.CharField(max_length=70, null=False, blank=False)
    letter_header = models.ImageField(null=True,blank=True)
    letter_footer = models.ImageField(null=True,blank=True)
    logo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name