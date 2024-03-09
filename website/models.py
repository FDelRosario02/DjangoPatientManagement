from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Record(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, )
    last_name =  models.CharField(max_length=50, )
    address = models.CharField(max_length=200, blank=False)
    city =models.CharField(max_length=50, blank=False)
    state =models.CharField(max_length=50, blank=False)
    zipcode = models.CharField(max_length=10, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=12,blank=False)

    def __str__(self):
        return(f"{self.first_name}  {self.last_name}")
    
# The Doctor model represents a doctor in the system.
class Doctor(models.Model):
    # The date and time when the doctor was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # The first name of the doctor.
    first_name = models.CharField(max_length=50)
    # The last name of the doctor.
    last_name = models.CharField(max_length=50)
    # The date of birth of the doctor.
    date_of_birth = models.DateField(null=True, blank=True)
    # The gender of the doctor.
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], blank=True)
    # The address of the doctor.
    address = models.CharField(max_length=200, blank=True)
    # The phone number of the doctor.
    phone = models.CharField(max_length=12, blank=True)
    # The email address of the doctor.
    email = models.EmailField(blank=True)
    # The specialization of the doctor.
    specialization = models.CharField(max_length=100)

    # The __str__ method returns a string representation of the doctor.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# The Patient model represents a patient in the system.
# class Patient(models.Model):
#     # The date and time when the patient was created.
#     created_at = models.DateTimeField(auto_now_add=True)
#     # The first name of the patient.
#     first_name = models.CharField(max_length=50)
#     # The last name of the patient.
#     last_name = models.CharField(max_length=50)
#     # The date of birth of the patient.
#     date_of_birth = models.DateField(null=True, blank=True)
#     # The gender of the patient.
#     gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], blank=True)
#     # The address of the patient.
#     address = models.CharField(max_length=200, blank=True)
#     # The phone number of the patient.
#     phone = models.CharField(max_length=12, blank=True)
#     # The email address of the patient.
#     email = models.EmailField(blank=True)
#     # The blood type of the patient.
#     blood_type = models.CharField(max_length=5, blank=True)
#     # Any allergies the patient may have.
#     allergies = models.TextField(blank=True)
#     # Any current medications the patient is taking.
#     current_medications = models.TextField
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
class Symptom(models.Model):
    nombre = models.CharField(max_length = 250)

class Patient(models.Model):
    # The date and time when the patient was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # The first name of the patient.
    first_name = models.CharField(max_length=50)
    # The last name of the patient.
    last_name = models.CharField(max_length=50)
    # The date of birth of the patient.
    date_of_birth = models.DateField(null=True, blank=True)
    # The gender of the patient.
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], blank=True)
    # The address of the patient.
    address = models.CharField(max_length=200, blank=True)
    # The phone number of the patient.
    phone = models.CharField(max_length=12, blank=True)
    # The email address of the patient.
    email = models.EmailField(blank=True)
    # The blood type of the patient.
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_type = models.CharField(max_length=5, choices=BLOOD_TYPE_CHOICES, blank=True)
    # Any allergies the patient may have.
    allergies = models.TextField(blank=True)
    # Any current medications the patient is taking.
    current_medications = models.TextField(blank=True)
    #nombre= models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def assign_symptom(self,  symptom_name):
            symptom, _ = Symptom.objects.get_or_create(nombre=symptom_name)
            self.symptoms.add(symptom)
