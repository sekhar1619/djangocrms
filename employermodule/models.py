from django.db import models

# Create your models here.
class JobDetails(models.Model):
    work_title = models.CharField(max_length=255)
    salary_offered = models.CharField(max_length=255)
    JOB_TYPES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
    ]
    job_type = models. CharField(max_length=20, choices=JOB_TYPES)
    benefits = models. TextField()
    education = models. CharField(max_length=255)
    work_location= models. CharField(max_length=255)
    required_skills = models.TextField()

    def __str__(self):
        return self.work_title