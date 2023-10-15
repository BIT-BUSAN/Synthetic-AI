#이미지 크기 조절(키우기)
from PIL import Image

# 이미지 파일 열기
image = Image.open('input_img.jpg')

# 원하는 새로운 가로 및 세로 크기 정의
new_width = 2000  # 새로운 가로 크기
new_height = 1800  # 새로운 세로 크기

# 이미지를 늘리는 데 사용할 배경 이미지 생성
background = Image.new("RGB", (new_width, new_height), (255, 255, 255, 0))  # 투명한 배경 이미지 생성

# 원본 이미지를 캔버스 가운데에 붙여넣기
x_offset = (new_width - image.width) // 2
y_offset = (new_height - image.height) // 2
background.paste(image, (x_offset, y_offset))

# 결과 이미지 저장
background.save('control_img.jpg')
