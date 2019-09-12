import eventlet
from flask import Flask
from flask_mqtt import Mqtt
from flask_cors import CORS
from flask_socketio import SocketIO

from app.access import access_blueprint
from app.service import prossMsg

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有域名跨域
CORS(app, supports_credentials=True)

app.config['MQTT_BROKER_URL'] = '39.129.9.137'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)
socketio = SocketIO(app)


app.register_blueprint(access_blueprint, url_prefix='/access')


# 连接后 =>订阅主题
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('qrcode')
    print("Connected with result code " + str(rc))

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    # 调用处理消息的函数
    prossMsg(message.payload)



# 发布主题和信息
@app.route('/mqtt/pub/<want_to_pub>', methods=['GET'])
def pub_my_msg(want_to_pub):
    mqtt.publish('result',want_to_pub)
    return want_to_pub


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, debug=True)