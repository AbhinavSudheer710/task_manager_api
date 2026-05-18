from rest_framework import serializers
from.models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_names = serializers.ListField(child=serializers.CharField(max_length=50),write_only=True,required=False)
    class Meta:
        model = Tasks
        read_only_fields = ['created_at']
        fields = ['title', 'description', 'created_at', 'due_date', 'difficulty', 'status','tags','tag_names']

    def _handle_tags(self, obj, tag_names):
        tags = []
        for names in tag_names:
            tag,_ = Tag.objects.get_or_create(name=names)
            tags.append(tag)
        obj.tags.set(tags)

    def create(self, validated_data):
        tags = validated_data.pop('tag_names')
        obj = Tasks.objects.create(**validated_data)
        self._handle_tags(obj, tags)
        return obj

class TaskListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'difficulty', 'status', 'due_date', 'tags']