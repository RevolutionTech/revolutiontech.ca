"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "home.html"


class CategoryPageView(TemplateView):

    template_name = "category_page.html"


class ItemPageView(TemplateView):

    template_name = "item_page.html"

    def dispatch(self, request, items, slug, *args, **kwargs):
        try:
            self.item = items.objects.get(slug=slug)
        except items.DoesNotExist:
            verbose_name_plural = items._meta.verbose_name_plural.lower()
            items_list = "{items}:{items}_list".format(
                items=verbose_name_plural
            )
            return HttpResponseRedirect(reverse(items_list))
        return super(ItemPageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemPageView, self).get_context_data(**kwargs)
        context['item'] = self.item
        context['absolute_uri'] = self.request.build_absolute_uri()
        return context
