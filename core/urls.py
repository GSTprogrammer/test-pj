from django.urls import path
from .views import SignupView,CreateProjectView,ProjectListView,CreateProposalView,ProjectProposalsView,UpdateProposalStatusView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/create/', CreateProjectView.as_view(), name='create_project'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('proposals/create/', CreateProposalView.as_view(), name='create_proposal'),
    path('projects/<int:project_id>/proposals/', ProjectProposalsView.as_view(), name='project_proposals'),
    path('proposals/<int:proposal_id>/update-status/', UpdateProposalStatusView.as_view(), name='update_proposal_status'),


]
