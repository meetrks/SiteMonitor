from base.serializers import BaseModelSerializer
from roles.models import Role


class RolesSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('last_alert_on', 'short_id')
