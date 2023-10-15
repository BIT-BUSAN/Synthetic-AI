#크기가 같은 이미지 합성코드(겹치기)
from PIL import Image

baseLayerSize = (2000, 1400)
baseLayer = Image.new("RGBA", baseLayerSize)

image = Image.open('rev_img1.png')
imagecut = Image.open('background_img.png')

# image700 이미지를 baseLayer와 동일한 크기로 조정
image700 = imagecut.resize(baseLayerSize)
imager = image.resize(baseLayerSize)

# 이미지 모드와 크기 확인
# print(f"image700 모드: {image700.mode}, 크기: {image700.size}")
# print(f"imager 모드: {imager.mode}, 크기: {imager.size}")

# 이미지 모드를 "RGBA"로 변경
# RGB가 아닌 RGBA를 사용해야한다
image700 = image700.convert("RGBA")
imager = imager.convert("RGBA")

# 이미지를 원하는 위치에 붙여넣습니다.
position = (0, 0)  # 붙여넣을 위치를 지정
baseLayer.paste(image, position)

# 이미지를 겹치기 위해 Image.alpha_composite를 사용합니다.
result_image = Image.alpha_composite(image700, imager)

# 이미지를 표시하고 저장합니다.
result_image.show()
result_image.save('result.png')
