from rest_framework import serializers
from .models import Category, Tag, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


# Краткий — для списка
class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "is_completed", "created_at"]


# Детальный — для просмотра + создания/обновления
class TaskDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        required=False,
        allow_null=True,
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        write_only=True,
        many=True,
        required=False,
    )

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "is_completed", "created_at",
            "category", "tags",
            "category_id", "tag_ids",
        ]
        read_only_fields = ["id", "created_at"]