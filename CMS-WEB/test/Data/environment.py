
'''
2018-09-03
guoyue
环境配置
'''
class CMS_Environment (object):
    cms_web_baseurl = {
        'QAFC':'http://cms-web.qafc.ops.com/client/login',
        'DEV':'http://cms-web.dev.ops.com/client/login',
        'UAT':'http://cmsuat.yiqiguang.com/client/login'
    }

class CMS_Account(object):
    data = {'siji': {'password': 'siji123', 'username': 'siji'},
            'tubobo': {"password": "xiansheng123", "username": "xiansheng"}
            }

# class CMS_MYSQL():

if __name__=='__main__':
    url=CMS_Environment().cms_web_baseurl['QAFC']
    print('url:',url)