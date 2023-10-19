from PIL import Image
from rembg import remove

image = Image.open('input_img.jpg')

new_width = 2000
new_height = 1800

background = Image.new("RGB", (new_width, new_height), (255, 255, 255, 0))  # 투명한 배경 이미지 생성

x_offset = (new_width - image.width) // 2
y_offset = (new_height - image.height) // 2
background.paste(image, (x_offset, y_offset))

#control_img로
background.save('control_img.jpg')

input_path = '../BIT_Image_Edited/control_img.jpg'
output_path = '../BIT_Image_Edited/rev_img.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

# 배경 이미지 경로
background_path = 'background_img.png'
# 사람 이미지 경로
person_path = '../BIT_Image_Edited/rev_img.png'

# 배경 이미지 열기
background = Image.open(background_path)

# 사람 이미지 열기
person = Image.open(person_path)

# 배경 이미지 크기 얻기
background_width, background_height = background.size

# 사람 이미지 크기 얻기
person_width, person_height = person.size

# 배경 이미지와 사람 이미지의 크기를 조정하여 같게 만듭니다.
background = background.resize((person_width, person_height))

# 이미지를 겹치기 위해 Image.alpha_composite를 사용합니다.
result_image = Image.alpha_composite(background.convert("RGBA"), person.convert("RGBA"))

# 결과 이미지 표시
result_image.show()

# 결과 이미지 저장
result_image.save('result.png')