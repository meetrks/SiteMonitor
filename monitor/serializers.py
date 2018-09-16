from rest_framework import serializers

from base.serializers import BaseModelSerializer
from monitor.models import SiteDetail


class SiteDetailSerializer(BaseModelSerializer):

    class Meta:
        model = SiteDetail
        fields = '__all__'
