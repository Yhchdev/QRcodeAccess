import hashlib
import qrcode
import base64
import io

# 身份信息sha256加密
def sha256_digest(idcard):
    sha256 = hashlib.sha256()
    sha256.update(idcard.encode('utf-8'))
    res = sha256.hexdigest()
    return res


# 生成二维码
def make_code(info):
    img = qrcode.make(data=info)

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    image_stream = buf.getvalue()
    heximage = base64.b64encode(image_stream)
    b64img = 'data:image/png;base64,' + heximage.decode()
    return b64img



# 解析二维码
