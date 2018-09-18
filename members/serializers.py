from base.serializers import BaseModelSerializer
from members.models import MemberDirectory


class MemberDirectorySerializer(BaseModelSerializer):
    class Meta:
        model = MemberDirectory
        fields = '__all__'
