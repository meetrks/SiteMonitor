# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

from base.utils import generate_short_id


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    short_id = models.CharField(max_length=8, null=True, blank=True, unique=True, db_index=True)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.short_id:
            self.short_id = generate_short_id()
        super(BaseModel, self).save(force_insert=False, force_update=False, using=using)
