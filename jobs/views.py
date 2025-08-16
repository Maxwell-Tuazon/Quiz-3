from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplicant
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib import messages

def job_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are unauthorized!")
        return redirect('/accounts/login/?next=/jobs/')
    query = request.GET.get('q')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query) |
            Q(location__icontains=query)
        )
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    user = request.user
    applicants = None
    is_admin = getattr(user, 'is_admin', False) if user.is_authenticated else False
    if is_admin:
        applicants = JobApplicant.objects.filter(job=job)
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'applicants': applicants,
        'is_admin': is_admin,
    })

from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Job
    fields = ['job_title', 'job_description', 'min_offer', 'max_offer', 'location']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        return self.request.user.is_admin

class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['job_title', 'job_description', 'min_offer', 'max_offer', 'location']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        return self.request.user.is_admin

class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        return self.request.user.is_admin

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required(login_url='/admin/login/')
def job_apply(request, pk):
    job = get_object_or_404(Job, pk=pk)
    user = request.user

    if user.is_admin:
        return HttpResponseForbidden("Admins cannot apply.")

    if request.method == 'POST' and request.FILES.get('resume'):
        resume = request.FILES['resume']
        # Prevent duplicate applications
        if JobApplicant.objects.filter(user=user, job=job).exists():
            return render(request, 'jobs/job_detail.html', {
                'job': job, 'is_admin': False, 'error': 'Already applied.'
            })
        JobApplicant.objects.create(user=user, job=job, resume=resume)
        return redirect('job_detail', pk=job.pk)

    return redirect('job_detail', pk=job.pk)