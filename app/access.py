from flask import jsonify
from flask import Blueprint
from flask import request
import time

from model import *
from utils import *

access_blueprint = Blueprint('access',__name__)


@access_blueprint.route('/part/',methods= ['POST'])
def partForm():
    global name,sex,phone,address,id_card,people_num,cause,date,dateEnd,carry
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    phone = data.get('phone')
    address = data.get('address')
    id_card = data.get('id_card')
    people_num = data.get('people_num')
    cause = data.get('cause')
    date = data.get('date')
    dateEnd = data.get('dateEnd')
    carry = data.get('carry')
    return "success"

# app post上传的数据 => 保存数据
@access_blueprint.route('/all/',methods = ['POST'])
def access():
    accessObj = AccessInfo()
    data = request.get_json()
    respondent_name = data.get('respondent_name')
    respondent_dept = data.get('respondent_dept')


    info = {"name":name,"phone":phone,"idCard":id_card}
    img_base64 = make_code(info)


    return img_base64





