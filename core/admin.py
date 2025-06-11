from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Project, Proposal

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff']
    list_filter = ['user_type', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ['project', 'freelancer', 'proposed_price', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['message']
