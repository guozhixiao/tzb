# from .sensitivePersonnelModel import SensitivePersonnelModel
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tzb.settings")# project_name 项目名称
django.setup()

from .model.sensitivePersonnelModel import SensitivePersonnelModel

import face_recognition
import time
import cv2


# 视频流截取图片
def face(path):
    # 获取当前时间戳做图像保存文件名
    current_time = time.time()
    print(path)
    # md5加密
    # input_name = hashlib.md5()

    # image_name = input_name.update(current_time.encode("utf-8"))

    # print(image_name)

    # 打开视频流或者视频文件
    vidcap = cv2.VideoCapture(path)

    # 按帧读取视频流  image就是每一帧的图像
    success, image = vidcap.read()

    # 读取成功success 为True
    while success:
        # 将读取成功image帧图像保存
        cv2.imwrite("/Users/guozhixiao/Downloads/%d.jpg" % int(current_time), image)
        break

    # 通过load_image_file方法加载待识别图片
    face_image = face_recognition.load_image_file("/Users/guozhixiao/Downloads/%d.jpg" % int(current_time))

    # 提取人脸编码 人脸的信息
    face_encodings = face_recognition.face_encodings(face_image)

    # 提取 image 人脸坐标信息
    face_locations = face_recognition.face_locations(face_image)
    print(face_locations)

    try:
        # where = {'id': 1}
        res = SensitivePersonnelModel.getAll()
    except Exception as e:
        print(e)
    print(res, "--------------------")
    # print(data)
    # 如果未识别人脸信息，直接pass
    if face_recognition == []:

        pass

    # 查询数据库

    # 不为空查询数据库做人脸识别
    elif face_recognition !=  []:
        # 多个人脸

        for i in range(len(face_encodings)):
            # 取人脸编码 做对比
            face_encoding = face_encodings[i]

            # 取人脸位置信息
            face_location = face_locations[i]

            # 上 右 下 左 解包操作，得到每张人脸的四个位置信息
            x, y, w, h = face_location

            # 给人脸画框
            cv2.rectangle(face_image, (h, x), (y, w), (0, 255, 0), 2)

            # 写字
            # cv2.putText(face_image, "", (left-10, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

            res = "/Users/guozhixiao/Downloads/%d.jpg" % int(time.time())

            # cv2.imwrite(res, roiImg)
            # 人脸框颜色
            face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

            # 存储文件
            cv2.imwrite(res, face_image_rgb)  # 存储为图像

            # 从image原图根据location坐标扣图
            face_image = image[x:w, h:y]

            # 保存文件
            cv2.imwrite(res, face_image)


    return "111"
