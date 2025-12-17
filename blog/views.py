from blog.models import Blog, Category, Department, Member, Project
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .forms import JobApplicationForm

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

    categories = Category.objects.all()

    return render(request, 'all_blog.html', {
        'blog': blogs,
        'query': query,
        'categories': categories,
        'active_category': int(category_id) if category_id else None
    })



def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = JobApplicationForm()
    else:
        form = JobApplicationForm()

    return render(request, 'apply.html', {'form': form})






