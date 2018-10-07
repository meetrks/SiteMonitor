from django.db import models

from base.models import BaseModel


class MemberDirectory(BaseModel):
    member_name = models.CharField(max_length=255)
    # user_role = models.ManyToManyField(Role, related_name='user_role')
    mobile = models.CharField(max_length=15, default=0)
    country_code = models.CharField(max_length=5, default='+91')
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.member_name
