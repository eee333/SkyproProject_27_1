import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from ads.models import Category, Adv


def index(request):

    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = self.object_list
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        json_data = json.loads(request.body)

        category = Category()
        category.name = json_data["name"]

        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdvListView(ListView):
    model = Adv

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        advs = self.object_list
        response = []
        for adv in advs:
            response.append({
                "id": adv.id,
                "name": adv.name,
                "author": adv.author,
                "price": adv.price,
                "description": adv.description,
                "address": adv.address,
                "is_published": adv.is_published,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        json_data = json.loads(request.body)

        adv = Adv()
        adv.name = json_data["name"]
        adv.author = json_data["author"]
        adv.price = json_data["price"]
        adv.description = json_data["description"]
        adv.address = json_data["address"]
        adv.is_published = json_data["is_published"]

        try:
            adv.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        adv.save()
        return JsonResponse({
            "id": adv.id,
            "name": adv.name,
            "author": adv.author,
            "price": adv.price,
            "description": adv.description,
            "address": adv.address,
            "is_published": adv.is_published,
        })


class AdvDetailView(DetailView):
    model = Adv

    def get(self, request, *args, **kwargs):
        adv = self.get_object()

        return JsonResponse({
            "id": adv.id,
            "name": adv.name,
            "author": adv.author,
            "price": adv.price,
            "description": adv.description,
            "address": adv.address,
            "is_published": adv.is_published,
        })
