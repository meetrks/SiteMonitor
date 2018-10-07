from rest_framework.serializers import ValidationError

from base.serializers import BaseModelSerializer
from members.models import MemberDirectory


class MemberDirectorySerializer(BaseModelSerializer):
    class Meta:
        model = MemberDirectory
        fields = '__all__'

    def validate_mobile(self, attrs):
        if not attrs or len(attrs) > 15 or not attrs.isdigit():
            raise ValidationError({'detail': "Invalid mobile number"})
        return attrs

    def validate_country_code(self, attrs):
        if not attrs or len(attrs) > 4 or not attrs.startswith('+') or not attrs[1:].isdigit():
            raise ValidationError({'detail': "Invalid country code"})
        return attrs
