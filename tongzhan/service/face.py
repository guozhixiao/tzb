# from .sensitivePersonnelModel import SensitivePersonnelModel
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tzb.settings")# project_name 项目名称
django.setup()

from ..model.sensitivePersonnelModel import FaceRecognitionIndexModel
from ..model.sensitivePersonnelModel import SensitivePersonnelModel
from ..model.sensitivePersonnelModel import TempleFaceModel

import face_recognition
import time
import cv2
import numpy as np
import hashlib
import datetime
import codecs, json

# 定义个空数组
known_face_encodings = []

def test(path):
    # 获取当前时间戳做图像保存文件名
    current_time = time.time()
    url = '/Users/guozhixiao/Downloads/' + '1596770859.jpg'

    # 打开视频流或者视频文件
    vidcap = cv2.VideoCapture(url)

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

    # 如果未识别人脸信息，直接pass
    if face_locations == []:
        return "111"
    else:
        # 根据人脸数循环
        for i, element in enumerate(face_locations):
            currtime = int(time.time())
            print(element)
            # 获取下表s的人脸坐标
            # 获取四个坐标
            x, y, w, h = element

            # 从image原图根据location坐标扣图
            face_image = image[x:w, h:y]

            md5_file = md5(str(currtime))
            print(currtime)

            url = "/Users/guozhixiao/Downloads/%s.jpg" % md5_file

            # 添加人脸
            create = {
                'face_address': "%s.jpg" % md5_file,
                'ipcamera': 1,
                'create_time': datetime.datetime.now()
            }
            TempleFaceModel.create(create)
            time.sleep(1)
            cv2.imwrite(url, face_image)
            return ""

# 视频流截取图片
def face(path):
    # 获取当前时间戳做图像保存文件名
    current_time = time.time()

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
    cv2.imshow('lasd', face_image)
    # 提取人脸编码 人脸的信息
    face_encodings = face_recognition.face_encodings(face_image)

    # 提取 image 人脸坐标信息
    face_locations = face_recognition.face_locations(face_image)

    datas = []
    # 如果未识别人脸信息，直接pass
    if face_locations == []:
        return "未识别到人脸"

    # 不为空查询数据库做人脸识别
    elif face_locations !=  []:
        # 多个人脸
        # 获取数据库人脸数据
        data = FaceRecognitionIndexModel.getAll()
        # 如果数据库无数据 保存人脸图片
        if len(data) == 0:
            # 根据人脸数循环
            for s in range(len(face_encodings)):
                # 获取下表s的人脸坐标
                try:
                    face_location = face_locations[s]
                    # 获取四个坐标
                    x, y, w, h = face_location

                    # 从image原图根据location坐标扣图
                    face_image = image[x:w, h:y]

                    currtime = int(time.time())

                    md5_file = md5(str(currtime))

                    url = "/Users/guozhixiao/Downloads/%s.jpg" % md5_file

                    # 添加人脸
                    create = {
                        'face_address': "%s.jpg" % md5_file,
                        'ipcamera': 1,
                        'create_time': datetime.datetime.now()
                    }
                    TempleFaceModel.create(create)
                    cv2.imwrite(url, face_image)


                    return ""
                except Exception as e:
                    print(e)
        else:
            print("----------有数据进来------------")
            for i in range(len(face_encodings)):
                face_encoding = face_encodings[i]
                face_location = face_locations[i]
                # 获取四个坐标
                x, y, w, h = face_location

                # 从image原图根据location坐标扣图
                face_image = image[x:w, h:y]

                currtime = int(time.time())

                md5_file = md5(str(currtime))

                url = "/Users/guozhixiao/Downloads/%s.jpg" % md5_file

                # 添加人脸
                create = {
                    'face_address': "%s.jpg" % md5_file,
                    'ipcamera': 1,
                    'create_time': datetime.datetime.now()
                }
                TempleFaceModel.create(create)
                cv2.imwrite(url, face_image)

                # 循环数据库人脸
                for a in data:
                    try:
                        face = string_numpy(a['face_recognition'])
                        print(a['face_recognition'],'------------获取face')
                        results = face_recognition.compare_faces(face, face_encoding, tolerance=0.4)

                        print(results)
                        if results[0] == True:
                            where = {
                                'id' : a['sensitive_personnel_id']
                            }
                            user = SensitivePersonnelModel.getOne(where)
                            arr = {
                                'name': user['name'],
                                'id_card': user['id_card'],
                                'face_address': user['face_address'],
                                'url' : '127.0.0.1:8001/static/' + "%s.jpg" % md5_file,
                            }
                            datas.append(arr)
                    except Exception as e:
                        print(e)
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

    j = json.dumps(datas)
    return j

# 将人脸coding转为字符串
def face_analysis(image_face_encoding):
    # 将numpy array类型转化为列表
    encoding__array_list = image_face_encoding.tolist()

    # 将列表里的元素转化为字符串
    encoding_str_list = [str(i) for i in encoding__array_list]

    # 拼接列表里的字符串
    encoding_str = ','.join(encoding_str_list)

    return

# md5加密
def md5(password):
    md5 = hashlib.md5()
    # 进行加密，python2可以给字符串加密，python3只能给字节加密
    md5.update(password.encode())
    password_md5 = md5.hexdigest()

    return password_md5

# 将numpy array类型转化string
def numpy_string(face_image):
    face_encodings = face_recognition.face_encodings(face_image)[0]
    # 将numpy array类型转化为列表
    encoding__array_list = face_encodings.tolist()

    # 将列表里的元素转化为字符串
    encoding_str_list = [str(i) for i in encoding__array_list]

    # 拼接列表里的字符串
    encoding_str = ','.join(encoding_str_list)

    return encoding_str

# 将string 转为numpy array
def string_numpy(face_image_string):
    # 转换list
    dlist = face_image_string.strip(' ').split(',')
    # 将list中str转换为float
    dfloat = list(map(float, dlist))
    arr = np.array(dfloat)

    known_face_encodings.append(arr)

    return known_face_encodings




