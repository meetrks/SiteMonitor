from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)
        super(BaseModelSerializer, self).__init__(*args, **kwargs)
        existing_fields = set(self.fields.keys())
        if fields is not None:
            allowed = set(fields)
            for field_name in existing_fields - allowed:
                self.fields.pop(field_name)
        existing_fields = set(self.fields.keys())
        if exclude_fields is not None:
            exclude_fields = set(exclude_fields)
            for field_name in existing_fields & exclude_fields:
                self.fields.pop(field_name)
