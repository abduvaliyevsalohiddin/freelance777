from django.contrib import admin
from django.urls import path
from main.views import *
from user.views import *
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Freelance API",
        default_version='v1',
        description="Test Freelance API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    # Simple JWT
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),

    # Profile
    path('register/', RegisterAPIView.as_view()),
    path('profile/', ProfileRetrieveUpdateDestroyView.as_view()),

    # Skill
    path('skills/', SkillListCreateAPIView.as_view()),
    path('skills/<int:pk>/', SkillDetailAPIView.as_view()),

    # FreelancerSkill
    path('freelancerSkill/', FreelancerSkillListCreateAPIView.as_view()),
    path('freelancerSkill/<int:pk>/', FreelancerSkillDetailAPIView.as_view()),


    # Category
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    # Job
    path('jobs/', JobListCreateAPIView.as_view()),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view()),

    # Proposal
    path('proposals/', ProposalListCreateAPIView.as_view()),
    path('proposals/<int:pk>/', ProposalDetailAPIView.as_view()),

    # Contract
    path('contracts/', ContractListCreateAPIView.as_view()),
    path('contracts/<int:pk>/', ContractDetailAPIView.as_view()),

    # Review
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),

    # Resume
    path('resumes/', ResumeListCreateAPIView.as_view()),
    path('resumes/<int:pk>/', ResumeDetailAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
