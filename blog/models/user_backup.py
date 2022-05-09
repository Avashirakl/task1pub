from django.db import models
from django.utils.translation import gettext_lazy as _


class User_backup(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log id'),
        editable=False,
        primary_key=True,
        null=False,
    )
    user_id = models.IntegerField(
        null=False,
        verbose_name=_('User ID'),
        blank=True,
    )
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=50,
        blank=True,
        null=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date joined'),
    )

    deleted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('deleted at'),
    )

    class Meta:
        verbose_name = _('User backup')
        verbose_name_plural = _('User backups')

