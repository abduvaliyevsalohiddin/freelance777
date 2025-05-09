from django.contrib import admin
from .models import Category, Job, Proposal, Contract, Review, Resume
from user.models import Profile


# -------------------------
# Category Admin
# -------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date', 'updated_date')
    search_fields = ('name', 'description')
    list_filter = ('created_date', 'updated_date')


# -------------------------
# Job Admin
# -------------------------

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'budget', 'is_open', 'deadline', 'created_date', 'updated_date')
    search_fields = ('title', 'description', 'client__username', 'category__name')
    list_filter = ('is_open', 'category', 'created_date', 'updated_date')
    list_editable = ('is_open',)

    def client_username(self, obj):
        return obj.client.username


# -------------------------
# Proposal Admin
# -------------------------

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('job', 'freelancer', 'proposed_price', 'status', 'submitted_at', 'created_date', 'updated_date')
    search_fields = ('job__title', 'freelancer__username', 'status')
    list_filter = ('status', 'created_date', 'updated_date')
    list_editable = ('status',)


# -------------------------
# Contract Admin
# -------------------------

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('job', 'freelancer', 'client', 'end_date', 'is_completed', 'created_date', 'updated_date')
    search_fields = ('job__title', 'freelancer__username', 'client__username')
    list_filter = ('is_completed', 'created_date', 'updated_date')
    list_editable = ('is_completed',)


# -------------------------
# Review Admin
# -------------------------

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('contract', 'reviewer', 'reviewee', 'rating', 'created_date', 'updated_date')
    search_fields = ('contract__job__title', 'reviewer__username', 'reviewee__username')
    list_filter = ('rating', 'created_date', 'updated_date')


# -------------------------
# Resume Admin
# -------------------------

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'summary', 'created_date', 'updated_date')
    search_fields = ('user__username', 'title', 'summary')
    list_filter = ('created_date', 'updated_date')
