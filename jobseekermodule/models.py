from django.db import models


# Create your models here.
class Applicant(models.Model):
    first_name = models. CharField(max_length=100)
    last_name = models. CharField(max_length=100)
    phone_number = models. CharField(max_length=10)
    address = models.TextField()
    tenth_marks = models. CharField(max_length=10)
    twelfth_marks = models. CharField (max_length=10)
    cgpa = models.CharField(max_length=5)
    expected_salary = models. CharField(max_length=10)
    position = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from employermodule.models import JobDetails
class JobApplication(models.Model):
    job_details = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.name} {self.job_details}"