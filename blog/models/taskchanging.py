import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# STATUS_CHOICES = [
#     ('P', "Planning"),
#     ('A', "Active"),
#     ('C', "Control"),
#     ('D', "Done"),
# ]


class TaskChanging(models.Model):
    id = models.AutoField(
        verbose_name=_('Log_id'),
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        editable=False
    )

    task = models.UUIDField(
        null=False,
        verbose_name=_('Task ID'),
        blank=True,
    )
    # author =
    prevstatus = models.CharField(
        verbose_name=_('Previous Status'),
        max_length=32,
    )
    currentstatus = models.CharField(
        verbose_name=_('New Status'),
        max_length=32,
    )

    log_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Last activity'),
    )

    class Meta:
        verbose_name = _('Task change history')
        verbose_name_plural = _('Task change history')

    def __str__(self):
        return self.prevstatus + "-->" + self.currentstatus
