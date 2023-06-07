from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from PIL import Image
import os
import io
import random
import string
import sys
import shutil
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sub.html')


@app.route('/upload', methods=['POST'])
def upload():
    cdir = os.getcwd().split('\\')[-1]
    if cdir == 'opensw23-eleven':
        ()
    elif cdir == 'server' or cdir == 'pytorch-CycleGAN-and-pix2pix-master':
        os.chdir('..')
    else:
        os.chdir('opensw23-eleven')
        
    image_data = request.form['imageData']
    # 이미지 데이터를 디코딩하고 파일로 저장
    
    save_image(image_data, filename=filename)
    modelRun(filename)
    
    return jsonify({'success':True})
    return redirect(url_for('show_image', filename=filename))

@app.route('/get_image', methods=['GET'])
def get_image():
    image_file_path = 'static/img/result/'+filename_fake
    return send_file(image_file_path, mimetype='image/jpeg')

@app.route('/upload/<filename>')
def show_image(filename):
    print(filename)
    origin_file = filename
    convert_file = '/static/img/result/'+filename
    print(filename)
    return render_template('sub.html', origin_file=origin_file, convert_file=convert_file)
#    return redirect(url_for('show', filename=filename))
    

def save_image(image_data, filename):
    # 이미지 데이터를 디코딩
    image_data = base64.urlsafe_b64decode(image_data.split(',')[1])
    
    # 이미지 파일로 저장
    file_path = 'server/static/img/upload_img/'+filename
    with open(file_path, 'wb') as f:
        f.write(image_data)
    shutil.copy('server/static/img/upload_img/' + filename, 'pytorch-CycleGAN-and-pix2pix-master/datasets/elevenTest/test')

    return

def modelRun(filename):
    print("1")
    filename = filename.split('.')[0]
    # directory 위치 변경
    os.chdir("pytorch-CycleGAN-and-pix2pix-master")
    # test.py 실행
    os.system("python ..\\pytorch-CycleGAN-and-pix2pix-master\\test.py --dataroot datasets/elevenTest --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")
    # static/img/result 에 저장
    shutil.copy('results/edges2shoes_pretrained/test_latest/images/'+filename+'_fake.png', '../server/static/img/result/')
    return 
    

if __name__ == '__main__':
    # 서버 실행
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'
    filename_fake = filename.split('.')[0]+'_fake.png'
    app.run(debug=True,host='0.0.0.0',port='1010')