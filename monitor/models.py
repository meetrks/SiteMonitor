# -*- coding: utf-8 -*-


from django.db import models

from base.manager import BaseManager
from base.models import BaseModel


class SiteDetail(BaseModel):
    site_name = models.CharField(max_length=100)
    site_slug = models.SlugField(max_length=255, unique=True)
    site_url = models.URLField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    last_down_time = models.PositiveIntegerField(default=0)

    objects = BaseManager()

    def __unicode__(self):
        return self.site_name
