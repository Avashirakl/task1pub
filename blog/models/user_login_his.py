from django.db import models
from django.utils.translation import gettext_lazy as _


class User_login_his(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log_id'),
        editable=False,
        primary_key=True,
        null=False,
    )

    user_id = models.UUIDField(
        null=False,
        verbose_name=_('User ID'),
        blank=True,
    )

    logged_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Logged at'),
    )

    was_active = models.IntegerField(
        verbose_name=_('Was active'),
        blank=True,
        null=True,

    )
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=50,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('User login history')
        verbose_name_plural = _('Users login histories')
