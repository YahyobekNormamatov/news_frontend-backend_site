from django.contrib import admin
from .models import Blog, BlogImage, Category, Author, Member, Department, Project, JobApplication

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')



@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
