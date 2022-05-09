import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = [
    ('P', "Planning"),
    ('A', "Active"),
    ('C', "Control"),
    ('D', "Done"),
]


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='author'
    )
    status = models.CharField(
        verbose_name=_('Status'),
        max_length=3,
        choices=STATUS_CHOICES,
        default='P'
    )

    start_date = models.DateTimeField(
        verbose_name=_('Start date'),
        default=timezone.now
    )
    end_date = models.DateTimeField(
        verbose_name=_('End date'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.name
