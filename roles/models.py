from django.db import models

from base.models import BaseModel


class Role(BaseModel):
    role_name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    alert_diff = models.PositiveIntegerField(default=0)
    last_alert_on = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.role_name
