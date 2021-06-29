from django.db import models


class BaseModel(models.Model):
    _created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    _updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)

    @property
    def created_at(self):
        return int(self._created_at.timestamp() * 1000)

    @property
    def updated_at(self):
        return int(self._updated_at.timestamp() * 1000)

    class Meta:
        abstract = True
