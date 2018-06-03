from rest_framework.generics import  ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from django.db.models import Q
from posts.models import Post
from . import serializers
from . import permissions
from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly
)
from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination,
)


from rest_framework.filters import (
SearchFilter,
OrderingFilter
)

class PostCreteApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(is_active = False)

class PostListApiView(ListCreateAPIView):

    serializer_class = serializers.PostListSerializer
    filter_backends = [SearchFilter]
    Search_fields = ["post","comment"]
    pagination_class = LimitOffsetPagination
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(post__icontains=query) |
                Q(comment__icontains=query)

            ).distinct()
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    
    serializer_class = serializers.PostDetaiSerializer

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetaiSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetaiSerializer
