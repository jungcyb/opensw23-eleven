from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from PIL import Image
from io import BytesIO
import os
import io
import random
import string
import sys
import shutil
import base64

app = Flask(__name__)
# drawing 은 그림파일 저장하는 경로, filename 은 upload 된 그림파일 저장하는 경로
drawing = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'
filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'

@app.route('/')
def index():
    return render_template('index.html')

# upload for drawing image
@app.route('/upload2', methods=['POST'])
def upload2():
    cdir = os.getcwd().split('\\')[-1]
    if cdir == 'opensw23-eleven':
        ()
    elif cdir == 'server' or cdir == 'pytorch-CycleGAN-and-pix2pix-master':
        os.chdir('..')
    else:
        os.chdir('opensw23-eleven')
    print('5')
    image_data_url = request.json['image_data']
    # chattgpt 짱
    # 데이터 URL에서 base64 인코딩된 이미지 부분 추출
    _, encoded_image = image_data_url.split(',', 1)

    # 패딩 확인 및 필요한 패딩 추가
    padding = len(encoded_image) % 4
    if padding > 0:
        encoded_image += '=' * (4 - padding)

    try:
        # 이미지 데이터 디코딩
        image_data = base64.b64decode(encoded_image)
        image = Image.open(BytesIO(image_data))
        pixels = image.load()
        width, height = image.size

        #배경을 하얀색으로 변환
        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if a == 0:
                    pixels[x, y] = (255, 255, 255, 255)
        
        output_image = BytesIO()
        image.save(output_image, format='PNG')
        image_data_r = output_image.getvalue()

        # 이미지 파일로 저장
        drawing_fake = drawing.split('.')[0]+'_fake.png'
        drawing_path = 'server/static/img/drawing_img/'+drawing
        
        
        with open(drawing_path, 'wb') as file:
            file.write(image_data_r)
        shutil.copy('server/static/img/drawing_img/' + drawing, 'pytorch-CycleGAN-and-pix2pix-master/datasets/elevenTest/test')
        print('이미지 저장 성공')

        # 저장된 이미지 파일 경로 응답으로 전송 <= ? 
        image_path = os.path.abspath(drawing)
        modelRun_drawing(drawing)
        
        return jsonify({'success':True})

    except base64.binascii.Error as e:
        print('이미지 저장 실패:', e)
        return {'error': '이미지 저장 실패'}


    return '이미지 데이터가 성공적으로 전송되었습니다.'

# server -> client converted drawing image return 
# 이거 왜 안되는지 모르겠네여
@app.route('/get_drawing', methods=['GET'])
def get_drawing():
    print("event")
    drawing_file_path = 'static/img/drawing_result/'+drawing.split('.')[0]+'_fake.png'
    return send_file(drawing_file_path, mimetype='image/jpeg')

# save and convert uploaded image / client -> server
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
    modelRun_uploaded(filename)
    
    return jsonify({'success':True})
    return redirect(url_for('show_image', filename=filename))

# server -> client converted upload image return
@app.route('/get_image', methods=['GET'])
def get_image():
    
    filename_fake = filename.split('.')[0]+'_fake.png'
    image_file_path = 'static/img/result/'+filename_fake
    return send_file(image_file_path, mimetype='image/jpeg')
    
# static/img/upload_img/filename 저장
def save_image(image_data, filename):
    # 이미지 데이터를 디코딩
    image_data = base64.urlsafe_b64decode(image_data.split(',')[1])
    
    # 이미지 파일로 저장
    file_path = 'server/static/img/upload_img/'+filename
    print(file_path)
    with open(file_path, 'wb') as f:
        f.write(image_data)
    shutil.copy('server/static/img/upload_img/' + filename, 'pytorch-CycleGAN-and-pix2pix-master/datasets/elevenTest/test')

    return
# run test.py
def modelRun_uploaded(filename):
    filename = filename.split('.')[0]
    # directory 위치 변경
    os.chdir("pytorch-CycleGAN-and-pix2pix-master")
    # test.py 실행
    os.system("python ..\\pytorch-CycleGAN-and-pix2pix-master\\test.py --dataroot datasets/elevenTest --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")
    # static/img/result 에 저장
    shutil.copy('results/edges2shoes_pretrained/test_latest/images/'+filename+'_fake.png', '../server/static/img/result/')
    return 
# run test.py
def modelRun_drawing(drawing):
    drawing = drawing.split('.')[0]
    # directory 위치 변경
    os.chdir("pytorch-CycleGAN-and-pix2pix-master")
    # test.py 실행
    os.system("python ..\\pytorch-CycleGAN-and-pix2pix-master\\test.py --dataroot datasets/elevenTest --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")
    # static/img/drwaing_result 에 저장
    shutil.copy('results/edges2shoes_pretrained/test_latest/images/'+drawing+'_fake.png', '../server/static/img/drawing_result/')
    return 
    

if __name__ == '__main__':
    # 서버 실행
    app.run(debug=True)