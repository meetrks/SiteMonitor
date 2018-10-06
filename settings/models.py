from django.db import models

from base.models import BaseModel


class MonitorSetting(BaseModel):
    url_ping_interval = models.PositiveIntegerField(default=5)  # check url on every n minutes (min val is 5)

    def __unicode__(self):
        return


class TwilioSetting(BaseModel):
    """
        Twilio SMS Settings
    """
    account_sid = models.CharField(max_length=50)
    auth_token = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)