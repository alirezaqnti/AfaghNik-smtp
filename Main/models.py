from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailTable(models.Model):
    Email = models.EmailField(_("آدرس ایمیل"), max_length=254)
    Salary = models.CharField(_("حقوق"), max_length=10)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("EmailTable")
        verbose_name_plural = _("EmailTables")

    def __str__(self):
        return self.Email
