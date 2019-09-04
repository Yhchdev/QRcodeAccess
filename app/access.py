from flask import jsonify
from flask import Blueprint
import time

from model import *


access = Blueprint('access',__name__)



@access.route('/access/',methods = ['POST'])
def access():
    # 获取post表单数据

    accessInfo = AccessInfo()

    accessInfo.name = ""
    accessInfo.sex = ""


    one = accessInfo.insertOne(accessInfo)