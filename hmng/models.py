from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
import json
from datetime import date

class Patient(models.Model):
    Pid = models.AutoField(primary_key=True, null=False,auto_created=True,unique=True)
    first_name_p = models.CharField(max_length=12, null=False)
    last_name_p = models.CharField(max_length=10)
    dob_p = models.DateField(null=False,verbose_name="Date of Birth")
    gender_p = models.CharField(max_length=1,null=False)
    mob_num_p = models.CharField(
        max_length=10,  # Mobile number length is fixed at 10
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',  # Ensures the first digit is 6-9 and exactly 10 digits
                message="Mobile number must start with 6, 7, 8, or 9 and be exactly 10 digits long."
            )
        ],
        verbose_name="Mobile Number",
    )
    age_p = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(120)])

    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name_p} {self.last_name_p} ({self.Pid})"
    



# Employee Model
class Employee(models.Model):
    E_ID = models.AutoField(primary_key=True)  # Unique identifier for each Employee
    name = models.CharField(max_length=100, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    e_gen = models.CharField(max_length=1, choices=SEX_CHOICES, null=False)
    mobile_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.E_ID})"

# Doctor Model
class Doctor(models.Model):
    E_ID = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)  # Foreign Key referencing Employee
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.E_ID.name} - {self.department}"

# Nurse Model
class Nurse(models.Model):
    E_ID = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)  # Foreign Key referencing Employee

    def __str__(self):
        return f"Nurse {self.E_ID.name}"

# Room Model
class Room(models.Model):
    R_ID = models.AutoField(primary_key=True)  # Unique identifier for each room
    room_type = models.CharField(max_length=50)  # e.g., deluxe, private, general
    capacity = models.IntegerField()
    availability = models.CharField(max_length=100)

    def __str__(self):
        return f"Room {self.R_ID} ({self.room_type})"

# Receptionist Model
class Receptionist(models.Model):
    E_ID = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)  # Foreign Key referencing Employee

    def __str__(self):
        return f"Receptionist {self.E_ID.name}"

# Test Report Model
class TestReport(models.Model):
    R_ID = models.AutoField(primary_key=True)  # Unique identifier for each Test Report
    P_ID = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Foreign Key referencing Patient
    test_type = models.CharField(max_length=100)
    result = models.TextField()

    def __str__(self):
        return f"Test Report {self.R_ID} for Patient {self.P_ID}"

# Bill Model
class Bill(models.Model):
    B_ID = models.AutoField(primary_key=True)  # Unique identifier for each Bill
    P_ID = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Foreign Key referencing Patient
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bill {self.B_ID} for Patient {self.P_ID}"

# Records Model
class Records(models.Model):
    record_no = models.AutoField(primary_key=True)  # Unique identifier for each record
    app_no = models.CharField(max_length=20)  # Application number

    def __str__(self):
        return f"Record {self.record_no}"

 