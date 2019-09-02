"""
:Created: 13 July 2015
:Author: Lucas Connors

"""

import random

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "home.html"


class CategoryPageView(TemplateView):

    template_name = "category-page.html"

    def get_context_data(self, items, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = items._meta.verbose_name_plural.lower()

        item_qs = items.objects.filter(visible=True).order_by("order")
        heroes = item_qs.filter(hero=True)
        regular = item_qs.filter(hero=False)
        context["items"] = {"heroes": heroes, "regular": regular}
        context["random_hero_unit_index"] = (
            random.randint(0, heroes.count() - 1) if heroes.count() > 0 else 0
        )

        return context


class ItemPageView(TemplateView):

    template_name = "item-page.html"

    def dispatch(self, request, items, slug, *args, **kwargs):
        try:
            self.item = items.objects.get(slug=slug)
        except items.DoesNotExist:
            verbose_name_plural = items._meta.verbose_name_plural.lower()
            items_list = "{items}:{items}_list".format(items=verbose_name_plural)
            return HttpResponseRedirect(reverse(items_list))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.item
        context["absolute_uri"] = self.request.build_absolute_uri()
        return context
