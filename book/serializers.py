from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()