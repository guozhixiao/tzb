from django.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import staticfiles
# 匹配径
urlpatterns = [
    # 空URL接口
    # 分发api 也为了controller 引包问题
    path('', include('tongzhan.urls')),
]

urlpatterns += staticfiles_urlpatterns()