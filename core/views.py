from .models import CustomUser,Project,Proposal
from .serializers import SignupSerializer,ProjectSerializer,ProposalSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions ,status

class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer


class IsClientUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'client'

class CreateProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsClientUser]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
        
        
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]  


class IsFreelancerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'freelancer'

class CreateProposalView(generics.CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [IsFreelancerUser]

    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)
        
        
        
class ProjectProposalsView(generics.ListAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)

        # فقط اگر خود کارفرما باشه اجازه داره
        if project.client != self.request.user:
            raise permissions.PermissionDenied("You don't have access to this project's proposals.")

        return Proposal.objects.filter(project=project).order_by('-created_at')



class UpdateProposalStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, proposal_id):
        try:
            proposal = Proposal.objects.get(id=proposal_id)
        except Proposal.DoesNotExist:
            return Response({"error": "Proposal not found."}, status=status.HTTP_404_NOT_FOUND)

        # فقط client صاحب پروژه اجازه داره
        if proposal.project.client != request.user:
            return Response({"error": "You are not allowed to modify this proposal."}, status=status.HTTP_403_FORBIDDEN)

        new_status = request.data.get("status")
        if new_status not in ['accepted', 'rejected']:
            return Response({"error": "Status must be 'accepted' or 'rejected'."}, status=status.HTTP_400_BAD_REQUEST)

        if new_status == 'accepted':
            # فقط یک Proposal باید accepted باشه
            if Proposal.objects.filter(project=proposal.project, status='accepted').exists():
                return Response({"error": "An accepted proposal already exists for this project."}, status=status.HTTP_400_BAD_REQUEST)

        proposal.status = new_status
        proposal.save()

        return Response({"message": f"Proposal {proposal.id} marked as {new_status}."})