
# Team Introduction
  ## team member’s names, IDs, and roles
  > 정호균
  - StudentID : 202211375
  - Role : Team Leader | Coder
  > 조익성
  - StudentID : 202011375
  - Role : Coder
  > 김형언
  - StudentID : 202211290
  - Role : Coder
  > 강조은
  - StudentID : 202211250
  - Role : Coder

# Topic Introduction
> __Edges to Photo__
- pytorch의 pix2pix모델을 사용하여 선화로 이루어진 신발 이미지를 실제 신발 이미지로 변환한다.
- 사용자가 그림을 그린 직후 바로 실사화해 결과를 보여주는 어플리케이션 제작을 목표로 한다.

> Code Source
- [Project Repository](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
- [Information](https://phillipi.github.io/pix2pix/)
- [Example](https://phillipi.github.io/pix2pix/images/sketch2photo_shoes/latest_net_G_sketch/index.html)

# Results
> input<br>
- <img src="./well_produced/degree_and_reflection/2/reflected_-45.png" width=256 height=256>

> output<br>
- <img src="./well_produced/degree_and_reflection/2/reflected_-45_res.png" width=256 height=256>

> input<br>
- <img src="./well_produced/line_width_and_two_object/normal.png" width=256 height=256>

> output<br>
- <img src="./well_produced/line_width_and_two_object/normal_res.png" width=256 height=256>

> input<br>
- <img src="./well_produced/position/bottom_middle.png" width=256 height=256>

> output<br>
- <img src="./well_produced/position/bottom_middle_res.png" width=256 height=256>

# Analysis/Visualization

## 1. 배경색
 배경색 `"cyan"`과 `"yellow"`의 경우 결과물에 있어 큰 차이가 없을 뿐 아니라

> 배경색 `"cyan"` input<br>
> <img src="./well_produced/background_color/cyan.png" width=256 height=256>

> 배경색 `"cyan"` output<br>
> <img src="./well_produced/background_color/cyan_res.png" width=256 height=256>

> 배경색 `"yellow"` input<br>
> <img src="./well_produced/background_color/yellow.png" width=256 height=256>

> 배경색 `"yellow"` output<br>
> <img src="./well_produced/background_color/yellow_res.png" width=256 height=256>

두 색을 혼합해 배경을 구성하더라도 유의미한 차이가 나타나지 않았다.

> 배경색 `"cyan and yellow"` input<br>
> <img src="./well_produced/background_color/cyan_yellow.png" width=256 height=256>

> 배경색 `"cyan"` output<br>
> <img src="./well_produced/background_color/cyan_yellow_res.png" width=256 height=256>

반면 `"cyan"`과 `"red"`를 혼합해 배경을 구성했을 경우 실사를 구성하는 색의 체도가 낮아진 것을 확인할 수 있었는데 이를 토대로 모델은 "배경색"의 `"체도"`에 영향을 받으나 `"색조"`에는 큰 영향을 받지 않는 것으로 보인다.

> 배경색 `"cyan and red"` input<br>
>![bg_cyan_red_input](./well_produced/background_color/cyan_red.png)

> 배경색 `"cyan"` output<br>
![bg_cyan_result](./well_produced/background_color/cyan_red_res.png)

## 2. 선 색
선화를 구성한는 선의 색상 역시 배경색과 비슷한 양상을 보였다.

`"cyan"`색,`"purple"`색, `"yellow"`색으로 그린 선화들은 실사의 색상이 모두 베이지 색으로 서로 큰 차이 없이 나왔으나,
> 선색 `"cyan"` input<br>
> <img src="./well_produced/color/1/cyan.png" width=256 height=256>

> 선색 `"cyan"` output<br>
![cl_cyan_result](./well_produced/color/1/cyan_res.png)

> 선색 `"yellow"` input<br>
> <img src="./well_produced/color/1/yellow.png" width=256 height=256>

> 선색 `"yellow"` output<br>
![cl_yellow_result](./well_produced/color/1/yellow_res.png)

> 선색 `"purple"` input<br>
> <img src="./well_produced/color/1/purple.png" width=256 height=256>

> 선색 `"purple"` output<br>
![cl_purple_result](./well_produced/color/1/purple_res.png)

`"black"`색상으로 구성한 선화 만큼은 채도가 낮아지고, `"붉은 색"` 실사로 나타나는 모습을 보였다.

> 선색 `"black"` input<br>
> <img src="./well_produced/color/1/black.png" width=256 height=256>

> 선색 `"black"` output<br>
![cl_black_result](./well_produced/color/1/black_res.png)

배경색뿐 아니라 모든 색에 대해 모델의 구분 기준은 채도로 유추된다.

또한 `배경색과 선색의 채도가 비슷할 수록`, 즉 채도가 높을 수록 `실사의 형태가 뭉개지는` 모습을 보인다. 이는 앞서 말한 듯 채도의 차이로 색을 구별하는 과정에서 `외곽 인식`에 문제가 생긴 것으로 보인다.

## 3. 각도 및 디테일

아래 3가지 각도에 대한 output을 보자.

> 각도 `"0"` input<br>
>![dg_0_input](./well_produced/degree_and_reflection/1/degree_0.png)

> 각도 `"0"` output<br>
![dg_0_result](./well_produced/degree_and_reflection/1/degree_0_res.png)

> 각도 `"45"` input<br>
>![dg_45_input](./well_produced/degree_and_reflection/1/degree_45.png)

> 각도 `"45"` output<br>
![dg_45_result](./well_produced/degree_and_reflection/1/degree_45_res.png)

> 각도 `"-45"` input<br>
>![dg_-45_input](./well_produced/degree_and_reflection/1/degree_-45.png)

> 각도 `"-45"` output<br>
![dg_-45_result](./well_produced/degree_and_reflection/1/degree_-45_res.png)

각도 45도에 대한 결과가 없던 신발끈의 디테일을 생성하는 등 가장 좋은 결과가 나왔다.

> 각도 `"45 - reflected"` input<br>
>![dg_45_reflected_input](./well_produced/degree_and_reflection/1/reflected_45.png)

> 각도 `"45 - reflected"` output<br>
![dg_45_reflected_result](./well_produced/degree_and_reflection/1/reflected_45_res.png)

이는 이미지를 반전 시켰을 때도 같은 결과가 나왔는데 이를 토대로 `신발 앞코는 바닥을`, 발을 집어넣는 `목 부분이 위를` 향할 수록 더 좋은 결과가 나오는 것을 알 수 있었다.

다만 선화의 디테일이 더 들어갔을 떄는 조금 다른 양상을 보였다.

> 각도 `"180"` input<br>
> <img src="./well_produced/degree_and_reflection/2/degree_180.png" width=256 height=256>

> 각도 `"180"` output<br>
![dg_180_result](./well_produced/degree_and_reflection/2/degree_180_res.png)

> 각도 `"-45"` input<br>
> <img src="./well_produced/degree_and_reflection/2/degree_-45.png" width=256 height=256>

> 각도 `"-45"` output<br>
![dg_-45_result2](./well_produced/degree_and_reflection/2/degree_-45_res.png)

> 각도 `"-45 - reflected"` input<br>
> <img src="./well_produced/degree_and_reflection/2/reflected_-45.png" width=256 height=256>

> 각도 `"-45 - reflected"` output<br>
![dg_-45_reflected_result](./well_produced/degree_and_reflection/2/reflected_-45_res.png)

각도 180과 각도 -45 중 180의 쪽이 `신발 밑창과 가죽의 경계 분할면`에서 더 나은 구분을 보인다. 이는 `선화의 각도보다 신발끈 등의 디테일`이 더 우선적으로 반영된다는 것으로 해석 될 수 있을 것 같다.

## 4. 선 두께

`"normal"`정도의 선 두께와 `"thick"`정도의 선 두께를 비교했을 때 확연히 `"normal"`쪽의 결과가 더 좋은 것을 볼 수 있다.

> 두께 `"normal"` input<br>
> <img src="./well_produced/line_width_and_two_object/normal.png" width=256 height=256>

> 두께 `"normal"` output<br>
> ![width_normal](./well_produced/line_width_and_two_object/normal_res.png)

> 두께 `"thick"` input<br>
> <img src="./well_produced/line_width_and_two_object/thick.png" width=256 height=256>

> 두께 `"thick"` output<br>
> ![width_thick](./well_produced/line_width_and_two_object/thick_res.png)

신발의 내 외부 경계가 `"thick"`에서 모호한 것을 보면 `선의 두께가 두꺼울 수록 경계 구분에 어려워하는 것으로 보인다.`

## 5. 두 물체의 우선순위

> `case1` input<br>
> <img src="./well_produced/line_width_and_two_object/normal_other.png" width=256 height=256>

> `case1` output<br>
> ![case1](./well_produced/line_width_and_two_object/normal_other_res.png)

> `case2` input<br>
> <img src="./well_produced/line_width_and_two_object/thick_other.png" width=256 height=256>

> `case2` output<br>
> ![case2](./well_produced/line_width_and_two_object/thick_other_res.png)

입력이미지에 두 선화가 존재할 경우 어떻게 되는지 비교해보았다. `case1`과 `case2`를 비교해보면 두 경우 모두 `얇은 선에 비해 두꺼운 선이 중점적으로 실사화`가 되었으나 모두 품질이 떨어지는 모습을 보인다. 이는 얇은 선의 왼쪽 선화가 영향을 미친 것으로 보이며 `case1`쪽이 더 노이즈가 큰 것을 보아 `두 물체 사이의 두께 차이가 적을 수록 노이즈가 큰 것으로 보인다.` 

## 6. 선화의 크기

> `big` input<br>
> ![big](./well_produced/object_size/big.png)

> `big` output<br>
> ![big](./well_produced/object_size/big_res.png)

> `small` input<br>
> ![small](./well_produced/object_size/small.png)

> `small` output<br>
> ![small](./well_produced/object_size/small_res.png)

`선화의 크기가 작을 수록 품질이 확연히 떨어지는` 모습을 확인할 수 있다.

## 7. 이미지의 크기

> `512` input<br>
> <img src="./well_produced/origin_size/512.png" width=512 height=512>

> `512` output<br>
> ![512](./well_produced/origin_size/512_res.png)

> `256` input<br>
> ![256](./well_produced/origin_size/256.png)

> `256` output<br>
> ![256](./well_produced/origin_size/256_res.png)

`입력 이미지 파일의 크기는 영향이 적은 것으로 보인다.` 이는 모델 내부 적으로 resize과정을 거치는 것으로 유추된다.

## 8. 선화의 위치

선화를 `가운데를 포함, 팔방`으로 옯겨가며 모델을 돌려본 결과 흥미로운 결과가 있었다. 아래 3가지 경우를 보면

> `bottom_middle` input<br>
> ![bottom_middle](./well_produced/position/bottom_middle.png)

> `bottom_middle` output<br>
> ![bottom_middle](./well_produced/position/bottom_middle_res.png)

> `middle` input<br>
> ![middle](./well_produced/position/middle.png)

> `middle` output<br>
> ![middle](./well_produced/position/middle_res.png)

> `top_middle` input<br>
> ![top_middle](./well_produced/position/top_middle.png)

> `top_middle` output<br>
> ![top_middle](./well_produced/position/top_middle_res.png)

`선화가 바닥에 가까울 수록 더 좋은 결과를 보이는 것을 알 수 있다.`

이는 좌우로 옮기더라도 동일한 양상을 보였다.

> `bottom_left` input<br>
> ![bottom_left](./well_produced/position/bottom_left.png)

> `bottom_left` output<br>
> ![bottom_left](./well_produced/position/bottom_left_res.png)

> `left` input<br>
> ![left](./well_produced/position/left.png)

> `left` output<br>
> ![left](./well_produced/position/left_res.png)

> `top_left` input<br>
> ![top_left](./well_produced/position/top_left.png)

> `top_left` output<br>
> ![top_left](./well_produced/position/top_left_res.png)

## 분석 결론
분석 결과 모델의 실사화 성능은 다음과 같은 요소에 영향을 받는 것으로 보인다.
```
1. 선의 두께 (얇을 수록 Good)
2. 선의 채도 (배경과 차이가 클 수록 Good)
3. 배경의 채도 (선과 차이가 클 수록 Good)
4. 선화의 위치 (바닥에 붙어 있을 수록 Good)
5. 선화의 디테일 (신발 끈 등 특징적인 디테일이 뚜렷할 수록 Good)
6. 선화의 각도 (사선으로 기울어져 있으며 신발코가 바닥을 향하는 것이 Good)
```

# Installation
## Environment
> os : window 10 / 11

> python : 3.9

## Overview
![FlowChart](./Resources/img/pix2pixChart.jpg)

## 1. Cloning

Repository를 Clone 받습니다.
<br>
## `clone 받은 Repository의 이름을 opensw23-eleven으로 유지 해주세요.` 

## 2. Moudle Install

![init_pip](./Resources/img/init_pip.png)

디렉토리 내부에서 init_pip.bat을 실행시켜줍니다. pip를 이용한 module다운로드를 자동으로 진행합니다.

## 3. Server Running

![running_server](./Resources/img/running_server.png)

디렉토리 내부에서 running_server.bat을 실행시켜줍니다. `flask`를 이용한 서버를 자동으로 실행하며 pretrained 모델이 없을 경우 다운로드합니다.

## 3-1. Model Download

![bitsman](./Resources/img/bitsman.png)

다음과 같은 cmd가 추가로 뜰 경우 모델을 다운로드 중인 것이니 모두 다운로드 될 떄까지 기다립니다.

![server](./Resources/img/server.png)

위와 같은 cmd는 서버를 실행 중인 것이니 종료하지 마십쇼.

## 4. Access

![chrome](./Resources/img/chrome.png)

chrome브라우저를 통해 위와 같이 입력하고 접속합니다.

## 5. Converting

![upload_area](./Resources/img/upload_area.png)

파일 선택 버튼을 누른 후 이미지를 선택, Convert버튼을 눌러 실사화 시킵니다.


![draw_area](./Resources/img/draw_area.png)

혹은 마우스 좌클릭으로 직접 그린 후 Convert버튼을 눌러 실사화 시킵니다.

## 6. Result

![result](./Resources/img/result.png)

Convert버튼 하단 영역에서 결과를 확인 할 수 있습니다.

# Presentation
