#-*- coding:utf-8 -*-

class settings:

  ALIPAY_INPUT_CHARSET = 'utf-8'

  # 合作身份者ID，以2088开头的16位纯数字
  ALIPAY_PARTNER = '***********'

  # 签约支付宝账号或卖家支付宝帐户
  ALIPAY_SELLER_EMAIL = '********'


  # 交易过程中服务器异步通知的页面 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
  ALIPAY_NOTIFY_URL='http://****/*****'

  ALIPAY_SHOW_URL=''

  # 访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http
  ALIPAY_TRANSPORT='https'

  SIGN_TYPE = "SHA-1"

  APP_ID = '***********'


  # 商户私钥
RSA_PRIVATE ="""-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDflKVAFSMULsaVbq1iMUSYguIdMWr8J9vOjgFFzeqDJOiBluE2
AmD5b4OJuKeLa6xRPqJj79OAhgH96fBVKDU1kxSZNOD3J56P1EmhS06xzlEtC16H
oapr9Tvvy3KblcPY6Xyu4R+dM+jj7ZX+IU5MeCfkNBlO5Rskwvq2F0e4OwIDAQAB
AoGBANmEtID0D3zNxRKu0+kM81Te+orz483+5ji+f00000000000000000000000
BuINj0g7t6Gi4hJYTffKcZdn1trGrSBMphFHxyJuSw4mOCI4lRMISLdRio5S34xn
b8HmhR7SM8wv2hOcJBLVbKvSnnygpG8GWatvRTe2C+IB8oaBAkEA+NQta00/c9Rw
Zqh3j8uYzE56mjRE6npENMcuJ2oM7JrthQUUigoXMdGOS9xkg2ZuO8MIkQWL4+oh
dHMreUj4HQJBAOYGMNbZbWJcztktzPanGlqiOY0gf2HN7nWPSnIiN1UKUcNXKu6J
+nOz1FdFk3PZzWiF8X/3fRMcr0x1lf8b8jcCQGmPwhECfYfLOUAj+k0Tp6gNJzAi
OpZq9mKZmXf5IrCB7YAALr19GGf3KfH+9tlT7DIIRKsZekZffn/jmC7lCPUCQQDC
+nxroeIWfpTXgvs6GGs+aERgXCudu/FltRBlrps4eobUDg9WI58odEaJs3BJw1Va
RC9xSVe725S8Ou/qTsYBAkApOVqJZ4q8poCZBUkKa08pZ1emaNWw9NI5UoVzArpw
H005O+HzbnhP/rS7FNTc8YXK70h5sM5VHSihtuyYO33C
-----END RSA PRIVATE KEY-----"""

RSA_PUBLIC="""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDflKVAFSMULsaVbq1iMUSYguId
MWr8J9vOjgFFzeqDJOiBluE2AmD5b4OJuKeLa6xRPqJj70000000000jkjl00000
NOD3J56P1EmhS06xzlEtC16Hoapr9Tvvy3KblcPY6Xyu4R+dM+jj7ZX+IU5MeCfk
NBlO5Rskwvq2F0e4OwIDAQAB
-----END PUBLIC KEY-----"""

RSA_ALIPAY_PUBLIC="""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA00000000000I6d306Q8fIfCOaTXyiUeJHkrIvYISRcc73s3vF1ZT7XN8RNPwJxo8pWaJMmvyTn9N4HQ632qJBVHf8sxHi/fEsraprwCtzvzQETrNRwVxLO5jVmRGi60j8Ue1efIlzPXV9je9mkjzOmdssymZkh2QhUrCmZYI/FCEa3/cNMW0QIDAQAB
-----END PUBLIC KEY-----"""


