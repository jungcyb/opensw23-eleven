from flask import Flask, render_template, request, redirect, url_for
import os
import random
import string
import sys
import shutil



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
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'

    cdir = os.getcwd().split('\\')[-1]
    print(os.getcwd())
    print(cdir)
    if cdir == 'opensw23-eleven':
        ()
    elif cdir == 'server' or cdir == 'pytorch_CycleGAN-and-pix2pix-master':
        os.chdir('..')
    else:
        os.chdir('opensw23-eleven')
    # static/img 안에 저장
    file.save(os.path.join('server/static/img', filename))
    # test 파일 안 이미지 폴더에 저장
    shutil.copy('server/static/img/' + filename, 'pytorch-CycleGAN-and-pix2pix-master/datasets/elevenTest/test')

    modelRun(filename)
    return redirect(url_for('show_image', filename=filename))


def modelRun(filename):
    filename = filename.split('.')[0]
    # directory 위치 변경
    os.chdir("pytorch-CycleGAN-and-pix2pix-master")
    # test.py 실행
    os.system("python ..\\pytorch-CycleGAN-and-pix2pix-master\\test.py --dataroot datasets/elevenTest --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")
    # static/img/result 에 저장
    shutil.copy('results/edges2shoes_pretrained/test_latest/images/'+filename+'_fake.png', '../server/static/img/result/')
    return 

@app.route('/convert', methods = ['POST'])
def convert():
    file = request.files[filename]
    
#    return url_for('show_convert_image')
    return redirect(url_for('show_convert_image'))

# 저장된 이미지를 보여주는 엔드포인트
@app.route('/image/<filename>')
def show_image(filename):
    filename = '../pytorch-CycleGAN-and-pix2pix-master/result/edges2shoes_pretrained/test_latest/images/'+filename
    return render_template('index.html', filename=filename)


@app.route('/image/<filename>/convert')
def show_convert_image(filename):
#    filename = '../pytorch-CycleGAN-and-pix2pix-master/result/edges2shoes_pretrained/test_latest/images/'+filename
    filename = 'server/static/img/result'+filename.split('.'[0])+'_fake.png'
    return render_template('index.html', filename=filename)

if __name__ == '__main__':
    # uploads 디렉토리 생성
    os.makedirs('uploads', exist_ok=True)
    
    # 서버 실행
    app.run(debug=True)
