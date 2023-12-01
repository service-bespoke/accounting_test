from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

from django_countries.fields import CountryField

from django.urls import reverse

from company.models import Company


DEFAULT_THUMB = 'default.png'
# Create your models here.
STAFF_STATUS = (
    ('Active','Active'),
    ('Suspended','Suspended'),
    ('Resigned','Resign'),
    ('Terminated','Terminate'),
)
class Employee(models.Model):
    LANGUAGE = (('English','ENGLISH'),('Arabic','ARABIC'),('Hindi','HINDI'),('French','FRENCH'),('Other','OTHER'))
    GENDER = (('Male','MALE'), ('Female', 'FEMALE'),('other', 'OTHER'))
    VISATYPE=(('Visit Visa','VISIT VISA'),('Work Visa','WORK VISA'),('Own Visa','OWN VISA'),('Other Visa','OTHER VISA'))
    
    company=models.ForeignKey(Company, on_delete=models.PROTECT)
    emp_id = models.CharField(max_length=70)
    thumb = models.ImageField(blank=True,null=True,upload_to='staffimage',default=DEFAULT_THUMB)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    arabic_name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(max_length=125,blank=True,null=True)
    address1 = models.CharField(max_length=100,blank=True,null=True)
    address2 = models.CharField(max_length=100,default='',null=True,blank=True)
    dob = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    country=CountryField(blank=True,null=True)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='English')
    
    permanent_address1 = models.CharField(max_length=100,null=True,blank=True)
    permanent_address2 = models.CharField(max_length=100,default='',null=True,blank=True)
    emergency = models.CharField(max_length=15,null=True,blank=True)

    designation=models.CharField(max_length=100,blank=True,null=True)
    joined_date = models.DateField(blank=True,null=True)
    joined_as_trainee = models.DateField(null=True,blank=True)
    resign_date = models.DateField(null=True,blank=True)
    staff_status = models.CharField(max_length=20,choices=STAFF_STATUS,default='Active')
    is_staff_left = models.BooleanField(default=False)

    passport_number = models.CharField(max_length=128,null=True,blank=True)
    passport_issue_date = models.DateField(null=True,blank=True)
    passport_expiry_date = models.DateField(null=True,blank=True)
    is_passport_expiry_notif_send = models.BooleanField(default=False)

    visa_type = models.CharField(choices=VISATYPE, max_length=20,default='work visa')
    visa_number = models.CharField(max_length=128,null=True,blank=True)
    visa_issue_date = models.DateField(null=True,blank=True)
    visa_expiry_date = models.DateField(null=True,blank=True)
    is_visa_expiry_notif_send = models.BooleanField(default=False)

    driv_licence_number = models.CharField(max_length=128,null=True,blank=True)
    driv_licence_issue_date = models.DateField(null=True,blank=True)
    driv_licence_expiry_date = models.DateField(null=True,blank=True)
    is_driv_licence_expiry_notif_send = models.BooleanField(default=False)

    medical_insurance_number = models.CharField(max_length=128,null=True,blank=True)
    medical_insurance_issue_date = models.DateField(null=True,blank=True)
    medical_insurance_expiry_date = models.DateField(null=True,blank=True)
    is_medi_insurance_expiry_notif_send = models.BooleanField(default=False)

    basic_salary = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    hra_allowance = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    food_allowance = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    transport_allowance = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    communication_allowance = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    other_allowance = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])

    regular_holiday_rate = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    public_holiday_rate = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    overtime_rate = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    halfday_fine = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
    fullday_fine = models.DecimalField(default=0,decimal_places=2, max_digits=15,validators=[MinValueValidator(Decimal('0.00'))])
 
    suspended=models.BooleanField(default=False)      
    deleted=models.BooleanField(default=False) 

    def __str__(self):
        return self.first_name
        