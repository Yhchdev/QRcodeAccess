from flask import jsonify
from flask import Blueprint
from flask import request
import time

from model import *
from utils import *

access_blueprint = Blueprint('access',__name__)


@access_blueprint.route('/part/',methods= ['POST'])
def partForm():
    global name,sex,phone,address,id_card,people_num,cause,date,dateEnd,carry,plate_num
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    phone = data.get('phone')
    address = data.get('address')
    id_card = data.get('id_card')
    people_num = data.get('people_num')
    plate_num = data.get('plate_num')

    cause = data.get('cause')
    date = data.get('date')
    dateEnd = data.get('dateEnd')
    # 携带何物
    carry = data.get('carry')
    return "success"

# app post上传的数据 => 保存数据
@access_blueprint.route('/all/',methods = ['POST'])
def access():
    data = request.get_json()
    accessObj = AccessInfo
    respondent_name = data.get('respondent_name')
    respondent_dept = data.get('respondent_dept')


    info = {"name":name,"phone":phone,"idCard":id_card}
    img_base64 = make_code(info)

    access_new = AccessInfo(name=name,sex=sex,phone=phone,address=address,
                            id_card=id_card,idcard_sha256=id_card,people_num=people_num,plate_num=plate_num,
                            cause=cause,time_start = date,time_end = dateEnd,carry=carry,respondent_name=respondent_name,
                            respondent_dept=respondent_dept)

    #accessObj.insertOne(access_new)


    return img_base64





