from django.db import models
from django.db.models import JSONField


class GetPhone(models.Model):

    attributes = JSONField(null=True)


