from django.shortcuts import render

from .forms import JobApplicationForm
from .models import *

def viewjobs(request):
    return render(request, 'jobseekermodule/viewjobs.html')

from employermodule.models import JobDetails
from django.contrib.auth.decorators import login_required
@login_required(login_url='login1')
def job_details_list(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekermodule/viewjobs.html', {'job_details_list': job_details_list})

def addjobseekerprofile(request):
    return render(request, 'jobseekermodule/addjobseekerprofile.html')

def submit_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        tenth_marks = request. POST['10thMarks']
        twelfth_marks = request.POST['12thMarks']
        cgpa = request.POST['cgpa']
        expected_salary = request.POST['expectedSalary']
        position = request.POST['position']

        applicant = Applicant(first_name=first_name,
                              last_name=last_name,
                              phone_number=phone_number,
                              address=address,
                              tenth_marks=tenth_marks,
                              twelfth_marks=twelfth_marks,
                              cgpa=cgpa,
                              expected_salary=expected_salary,
                              position=position)
        applicant.save()
        return render(request, 'jobseekerhomepage.html')
    return render(request, 'jobseekerhomepage.html')

from django.shortcuts import render, redirect, get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail

def apply_to_job(request,job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job_details = job_details
            job_application.save()

            subject = 'Job Application Received'
            message = 'Thank you for applying to the job. Your application is received and will be sent to next process'
            from_email = 'akashm2k5@gmail.com'
            recipient_list = [job_application.email]
            send_mail(subject, message, from_email, recipient_list)
        return redirect('jobseekermodule:job_details_list')
    else:
        form = JobApplicationForm()

    return render(request, 'jobseekermodule/apply_to_job.html', {'job_details': job_details, 'form': form})