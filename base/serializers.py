from rest_framework import serializers

from authentication.models import User
from base.models import Bookmark


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'link', 'archived_flag', 'deleted_flag', 'new_flag', 'obsoleted_flag', 'creation_at', 'modification_at', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmarks-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bookmarks']
