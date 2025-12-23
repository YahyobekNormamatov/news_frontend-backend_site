from urllib import request
from blog.models import Blog, Category, Department, Member, Project, Services
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobApplicationForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news_detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'news_detail.html', {'blog': blog})

def about(request):
    blog = Blog.objects.all()
    return render(request, 'about.html', {'blog': blog})

def community(request):
    departments = Department.objects.prefetch_related("members").all()
    return render(request, "community.html", {"departments": departments})

def team_detail(request, pk):
    members = Member.objects.all()
    member = get_object_or_404(Member, pk=pk)
    return render(request, "team_detail.html", {
        "member": member,
        "members": members,
    })

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})


def blog(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')

    blogs = Blog.objects.all().order_by('-create_at')

    if category_id:
        blogs = blogs.filter(category_id=category_id)

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    active_category_name = None
    if category_id:
        try:
            active_category_name = Category.objects.get(id=category_id).name
        except Category.DoesNotExist:
            pass

    return render(request, 'all_blog.html', {
        'blog': page_obj,
        'query': query,
        'categories': categories,
        'active_category': int(category_id) if category_id else None,
        'active_category_name': active_category_name,
    })


def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Arizangiz muvaffaqiyatli yuborildi!")
            return redirect('apply')
    else:
        form = JobApplicationForm()

    return render(request, 'apply.html', {'form': form})


def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})




