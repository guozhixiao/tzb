from django.urls import path
from .controller.index import IndexController
from .controller.upload import UploadController
from .controller.faceController import FaceController
from .views import face
# 匹配径
urlpatterns = [
    # 空URL接口
    path('add/', IndexController.add, name='add'),
    path('upload/', UploadController.upload, name='upload'),
    path('add_face/', FaceController.face_recognition, name='face_recognition'),
    path('', face, name='face'),
]
