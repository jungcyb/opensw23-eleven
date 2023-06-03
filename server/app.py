from flask import Flask, render_template, request, redirect, url_for
import os
import random
import string
import sys


app = Flask(__name__)

# 파일 업로드를 위한 HTML 템플릿
@app.route('/')
def index():
    return render_template('index.html')

# 이미지를 업로드하고 저장하는 엔드포인트
@app.route('/upload', methods=['POST'])
def upload():
        # 임의의 파일 이름 생성
    file = request.files['image']  # 업로드된 파일 가져오기
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.jpg'

    #static/img 안에 저장
    file.save(os.path.join('static/img', filename))

    #테스트 파일 안의 이미지 폴더에 저장
    file.save(os.path.join('../pytorch-CycleGAN-and-pix2pix-master/datasets//elevenTest/test/', filename))
#   file.save(os.path.join('uploads', filename))

    modelRun()
    return redirect(url_for('show_image', filename=filename))


def modelRun():
    os.system("python ..\\pytorch-CycleGAN-and-pix2pix-master\\test.py --dataroot datasets/elevenTest --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")
    return 

# 저장된 이미지를 보여주는 엔드포인트
@app.route('/image/<filename>')
def show_image(filename):
    
    filename = '../pytorch-CycleGAN-and-pix2pix-master/result/edges2shoes_pretrained/test_latest/images/'+filename
    return render_template('index.html', filename=filename)


@app.route('/image/<filename>/convert')
def show_convert_image(filename):
    filename = '../pytorch-CycleGAN-and-pix2pix-master/result/edges2shoes_pretrained/test_latest/images/'+filename
    return render_template('index.html', filename=filename)

if __name__ == '__main__':
    # uploads 디렉토리 생성
    os.makedirs('uploads', exist_ok=True)
    
    # 서버 실행
    app.run(debug=True)
