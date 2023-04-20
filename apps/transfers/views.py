from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserDetailSerializer, RegisterSerializer
from apps.users.permissions import UserPermission


# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.object.all()
    serializer_class = UserSerializer  
    permission_classes = (UserPermission, )
