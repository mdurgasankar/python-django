from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from posts.models import Post, comments


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'user',
            'post',
            'comment',
            'is_active'
        ]

class PostListSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(
    view_name="postlist-api:detail",
    lookup_field = "pk"
    )

    delete_url = HyperlinkedIdentityField(
    view_name="postlist-api:delete",
    lookup_field = "pk"
    )
    comment = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'detail_url',
            'post',
            'comment',
            'is_active',
             'delete_url'
        ]
    def get_comment(self, obj):
        return "hello fein the method"

class PostDetaiSerializer(ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'post',
            'comment',
            'is_active',
            'comments'
        ]
    def get_comments(self, obj):
        commentModel = comments
        return CommentSerializer(commentModel.objects.filter(post = obj.id),many=True).data



class CommentSerializer(ModelSerializer):
    class Meta:
        model = comments
        fields=[
            'comment'
        ]
