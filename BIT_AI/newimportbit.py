import requests
import cv2
import numpy as np

# 이미지 다운로드 함수
def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

# 이미지 합성 함수
def blend_images(background_img, foreground_img, position):
    h, w, _ = foreground_img.shape
    y_offset, x_offset = position

    # 합성할 위치를 계산하여 이미지 합성
    background_img[y_offset:y_offset + h, x_offset:x_offset + w] = foreground_img

    return background_img

# 이미지 다운로드 받을 URL 설정
background_img_url = "https://example.com/background.jpg"
foreground_img_url = "https://example.com/foreground.jpg"

# 이미지 파일 저장 경로 설정
background_img_path = "background.jpg"
foreground_img_path = "foreground.jpg"

# 이미지 다운로드
download_image(background_img_url, background_img_path)
download_image(foreground_img_url, foreground_img_path)

# 이미지 로드
background_img = cv2.imread(background_img_path)
foreground_img = cv2.imread(foreground_img_path, cv2.IMREAD_UNCHANGED)

# 전경 이미지를 합성할 위치 설정 (왼쪽 위 모서리 좌표)
position = (100, 100)

# 이미지 합성
blended_img = blend_images(background_img.copy(), foreground_img, position)

# 결과 이미지 출력
cv2.imshow('Blended Image', blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()