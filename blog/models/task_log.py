import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Task_log(models.Model):
    id = models.AutoField(
        verbose_name=_('Log_id'),
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        editable=False
    )
    action = models.CharField(
        verbose_name=_('Action'),
        max_length=300,
    )
    task = models.UUIDField(
        null=False,
        verbose_name=_('Task ID'),
        blank=True,
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Last activity'),
    )

    last_status = models.CharField(
        verbose_name=_('Last status'),
        max_length=32,
    )

    class Meta:
        verbose_name = _('Task log')
        verbose_name_plural = _('Task logs')
