from django.shortcuts import render
from django.http import JsonResponse
from .models import Update
from django.views.generic import View
from resapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
# Create your views here.


def update_model_detail_view(request):
    data = {
    "count":1000,
    "content":"there you go"

    }

    return JsonResponse(data)


class JsonCBV(View):

    def get(self,request,*agrgs,**kwargs):
        data = {
        "count":1000,
        "content":"there you go"

        }

        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin,View):

    def get(self,request,*agrgs,**kwargs):
        data = {
        "count":1000,
        "content":"there you go"

        }

        return self.render_to_json_response(data)


class SerializedDetailView(View):

    def get(self,request,*agrgs,**kwargs):
        obj = Update.objects.get(id=1)
        data = {
        "user":obj.user.username,
        "content":"there you go"

        }

        return JsonResponse(data)


class SerializedListView(View):

    def get(self,request,*agrgs,**kwargs):
        qs = Update.objects.all()
        data = serialize("json",qs,fields=('user','content'))
        print(data)

        return JsonResponse(data,safe=False)
