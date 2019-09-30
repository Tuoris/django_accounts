import base64
import re
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image
from rest_framework import serializers

from api.models import Account

MAX_IMAGE_SIZE = 256  # in pixels

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'avatar',
            'first_name',
            'last_name',
            'creation_date',
        ]


class JSONCreateAccountSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'avatar',
            'first_name',
            'last_name',
            'creation_date',
        ]

    def create(self, validated_data):
        image_data = validated_data.pop('avatar')
        if image_data:
            image_data = re.sub('^data:image/.+;base64,', '', image_data)
            image = Image.open(BytesIO(base64.b64decode(image_data)))
            im_width, im_height = image.size
            if im_width > im_height:
                scale_coeficient = MAX_IMAGE_SIZE / im_width
            else:
                scale_coeficient = MAX_IMAGE_SIZE / im_height
            image = image.resize((int(im_width * scale_coeficient), int(im_height * scale_coeficient)))
            image = image.convert('RGB')

            buffer = BytesIO()
            image.save(buffer, 'JPEG')
            image_file = ContentFile(buffer.getvalue(), 'upload.jpg')

            validated_data['avatar'] = image_file
        return Account.objects.create(**validated_data)
