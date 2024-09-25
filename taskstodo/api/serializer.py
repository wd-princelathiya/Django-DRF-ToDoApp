from rest_framework import serializers
from taskstodo.models import Task
from accounts.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title","comments","completed"]

    def create(self, validated_data):
        """
        create new portfolio and assign it to
        user
        """
        validated_data["user"] = User.objects.get(
            id=self.context.get("request").user.id
        )
        return super().create(validated_data)