from codecs import charmap_build
from email.policy import default
from sqlite3 import Timestamp
import string
from django.db import models
from accounts.models import User


class University(models.Model):
    name = models.CharField(max_length=20, null=True)  # 학교 이름
    photo = models.ImageField(null=True, blank=True,
                              upload_to="univ_photo")  # 학교 사진
    student_num = models.IntegerField(default=0, null=True)  # 학교에 속한 학생 인원
    throw_num = models.IntegerField(default=0, null=True)  # 쓰레기 버린 횟수
