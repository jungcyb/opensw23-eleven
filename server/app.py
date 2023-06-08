from flask import Flask, render_template, request, make_response
import os
import random
import string
import base64

app = Flask(__name__)

# 파일 업로드를 위한 HTML 템플릿
@app.route('/')
def index():
    return render_template('index.html')

# 이미지를 업로드하고 저장하는 엔드포인트
@app.route('/upload', methods=['POST'])
def upload():
    # 임의의 파일 이름 생성
    file = request.files['image'] or request.form["image"]# 업로드된 파일 가져오기
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.png'

    cdir = os.getcwd().split('\\')[-1]
    print(os.getcwd())
    print(cdir)
    if cdir == 'opensw23-eleven':
        ()
    elif cdir == 'server' or cdir == 'pytorch-CycleGAN-and-pix2pix-master':
        os.chdir('..')
    else:
        os.chdir('opensw23-eleven')
    # static/img 안에 저장
    print(filename[:-4])

    dataDir = f'./pytorch-CycleGAN-and-pix2pix-master/datasets/{filename[:-4]}'

    os.mkdir(dataDir)
    os.mkdir(dataDir + "/test")
    file.save(os.path.join(dataDir + "/test", filename))
    modelRun(filename)
    print("convert end")
    # return Response("{'msg': 'success'}", status=200, content_type="json")

    with open(f"..\\pytorch-CycleGAN-and-pix2pix-master\\results\\edges2shoes_pretrained\\test_latest\\images\\{filename[:-4]}_fake.png", "rb") as f:
        image_binary = f.read()

        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename=filename)
        return response

def modelRun(filename):
    filename = filename.split('.')[0]
    # test.py 실행 # directory 위치 변경
    os.chdir("pytorch-CycleGAN-and-pix2pix-master")
    # test.py 실행
    os.system(f"python .\\test.py --dataroot datasets/{filename} --model test --netG unet_256 --direction BtoA --dataset_mode single --norm batch --name edges2shoes_pretrained --gpu_ids -1")

app.run()