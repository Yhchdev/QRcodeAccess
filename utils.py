import hashlib



# 身份信息sha256加密
def sha256_digest(idcard):
    sha256 = hashlib.sha256()
    sha256.update(idcard.encode('utf-8'))
    res = sha256.hexdigest()
    return res

# 生成二维码


# 解析二维码
