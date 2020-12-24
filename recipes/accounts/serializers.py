from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

# refactoring user model
UserModel = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    # Validate Email
    email = serializers.EmailField(validators=[UniqueValidator(
        UserModel.objects.all()
    )])
    password = serializers.CharField(min_length=4, write_only=True)

    def create(self, validated_data):
        fields = 'username password email'.split()
        data = {f: validated_data.get(f) for f in fields}
        return UserModel.objects.create_user(**data)

    class Meta:
        model = UserModel
        fields = 'username password email first_name last_name'.split()
