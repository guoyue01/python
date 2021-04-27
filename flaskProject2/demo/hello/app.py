from flask import Flask
from flask import redirect, session, url_for, request,abort
import os

# 实例化Flask这个类，就得到了我们的程序实例app
# 传入Flask类构造方法的第一个参数是模块或包的名称,对于我们的程序来说（app.py），这个值为app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/hellos')
@app.route('/hellos/<name>')
@app.route('/apple', defaults={'name': 'xyz'})
def apples():
    return 'Hello World!'


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    print('get_name===>',name)
    if name is None:
        name = request.cookies.get('name', 'human')
        response = '<h1>hello,%s!</h1>' % name
        #根据用户认证状态返回不同的内容
        if 'logged_in' in session:
            response+='[Authenticated]'
        else:
            response+='[Not Authenticated]'
        return response

@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'welcome to admin page'

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))

@app.route('/login')
def login():
    session['logged_in'] = True  # 写入session
    return redirect(url_for('hello'))

@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>' %url_for('do_something',next=request.full_path)

@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do something and redirect</a>' %url_for('do_something',next=request.full_path)

def redirect_back(default='hello',**kwargs):
    for target in request.args.get('next'),request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default,**kwargs))

@app.route('/do-something')
def do_something():
    # return redirect(url_for('hello'))
    # return redirect(request.args.get('next',url_for('hello')))
    return redirect_back()
from urllib.parse import  urlparse,urljoin

def is_safe_url(target):
    ref_url=urlparse(request.host_url) #获取程序内的主机url
    # 使用urljoin将目标url转换成绝对url和主机地址进行验证
    test_url=urlparse(urljoin(request.host_url,target))
    # 使用urlparse模块提供的urlparse函数解析2个url
    #最后对目标url模式和主机地址进行验证，确保只有属于程序内的url会被返回
    return test_url.scheme in ('http','https') and ref_url.netloc==test_url.netloc

if __name__ == '__main__':
    app.run()
