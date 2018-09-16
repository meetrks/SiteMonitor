from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().all()


class ActiveObjectsManager(BaseManager):
    def get_queryset(self):
        return super(ActiveObjectsManager, self).get_queryset().filter(is_deleted=False)
