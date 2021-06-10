from django.shortcuts import render
import django_filters
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Log


class LogSerializer(serializers.ModelSerializer):#入出力の定義。modelでは指定したモデルの出力、入力チェックを定義。
    class Meta:
        model = Log
        fields = '__all__'


class LogFilter(django_filters.FilterSet):#django-filterの設定クラス。検索キーと検索条件を指定する。
#この設定をすると以下のURLで「指定した時間以降に作られたデータ」
#という条件の検索ができる。
    class Meta:
        model = Log
        fields = {'created_at': ['gte', ], }


class LogViewSet(viewsets.ModelViewSet):#django-filterの設定クラス。
    #検索キーと検索条件を指定する。この設定をすると以下のURLで「指定した時間以降に作られたデータ」という条件の検索ができる。
    queryset = Log.objects.all().order_by("created_at")

    serializer_class = LogSerializer
    filter_class = LogFilter

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

# Create your views here.
