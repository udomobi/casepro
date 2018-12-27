from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse

from .models import Urls


class ShortUrlsView(View):
    def get(self, request, *args, **kwargs):
        short = kwargs.get("short")
        org = self.request.org

        if short and org:
            try:
                url_to_redirect = Urls.get_url(org, short)
                return HttpResponseRedirect(url_to_redirect)
            except Urls.DoesNotExist:
                return HttpResponse(status=404)

        return HttpResponse(status=404)
