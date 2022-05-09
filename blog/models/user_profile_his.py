from django.db import models
from django.utils.translation import gettext_lazy as _


class User_profile_his(models.Model):
    log_id = models.AutoField(
        verbose_name=_('Log id'),
        editable=False,
        primary_key=True,
        null=False,
    )

    log_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Log date'),
    )

    user_id = models.IntegerField(
        null=False,
        verbose_name=_('User ID'),
        blank=True,
    )

    old_password = models.CharField(
        verbose_name=_('Old password'),
        max_length=128,

    )
    new_password = models.CharField(
        verbose_name=_('New password'),
        max_length=128,

    )

    first_name = models.CharField(
        max_length=128,
        verbose_name=_("First name"),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=128,
        verbose_name=_("Last name"),
        blank=True,
        null=True,
    )

    old_email = models.EmailField(
        verbose_name=_('Old email address'),
        blank=True,
        null=True
    )
    new_email = models.EmailField(
        verbose_name=_('New email address'),
        blank=True,
        null=True
    )

    username = models.CharField(
        max_length=128,
        verbose_name=_("Username"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('User profile history')
        verbose_name_plural = _('Users profile histories')

