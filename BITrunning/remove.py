#이미지 배경 삭제코드
from rembg import remove #이거 안됌왜
from PIL import Image

input_path = 'control_img.jpg'
output_path = 'rev_img1.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)