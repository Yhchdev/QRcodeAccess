from flask import jsonify
from flask import Blueprint
import time

from model import *

from utils import *


access = Blueprint('access',__name__)




# app post上传的数据 => 保存数据
@access.route('/access/',methods = ['POST'])
def access():
    # 获取post表单数据

    accessInfo = AccessInfo()

    accessInfo.name = ""
    accessInfo.sex = ""



    idcard_sha256 = sha256_digest(idcard=);

    accessInfo.idcard_sha256 = idcard_sha256;

    one = accessInfo.insertOne(accessInfo)



