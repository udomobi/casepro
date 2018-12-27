import short_url

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from dash.orgs.models import Org


class Urls(models.Model):
    org = models.ForeignKey(Org, verbose_name=_("Organization"), related_name="short_urls", on_delete=models.PROTECT)
    url = models.TextField(verbose_name=_("URL"))
    short = models.CharField(max_length=50, verbose_name=_("Short URL"))
    created_on = models.DateTimeField(db_index=True, auto_now_add=True)

    @classmethod
    def create(cls, org, url):
        short = cls.objects.create(
            org=org,
            url=url,
        )

        short.short = short_url.encode_url(short.pk)
        short.save()

        return org.make_absolute_url(reverse("short_urls.redirect", args=[short.short]))

    @classmethod
    def get_url(cls, org, short):
        result = cls.objects.get(org=org, short=short)
        return result.url

    def __str__(self):
        return "{} -> {}".format(self.short, self.url)
