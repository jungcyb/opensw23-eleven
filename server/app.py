from flask import Flask, render_template, request, redirect, url_for
import os
import random
import string

app = Flask(__name__)

# 파일 업로드를 위한 HTML 템플릿
@app.route('/')
def index():
    return render_template('index.html')

# 이미지를 업로드하고 저장하는 엔드포인트
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']  # 업로드된 파일 가져오기

    # 임의의 파일 이름 생성
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.jpg'

    # Flask 는 static 안에 파일만 인식 가능
    file.save(os.path.join('static/img', filename))
#   file.save(os.path.join('uploads', filename))

    return redirect(url_for('show_image', filename=filename))

# 저장된 이미지를 보여주는 엔드포인트
@app.route('/image/<filename>')
def show_image(filename):
    filename = 'img/'+filename
    return render_template('index.html', filename=filename)


if __name__ == '__main__':
    # uploads 디렉토리 생성
    os.makedirs('uploads', exist_ok=True)
    
    # 서버 실행
    app.run()
