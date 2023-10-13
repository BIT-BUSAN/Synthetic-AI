import cv2

# 이미지 합성 함수
def blend_images(background_img, foreground_img, position):
    if foreground_img is None:
        print("전경 이미지를 읽을 수 없습니다.")
        return background_img

    h, w, _ = foreground_img.shape
    y_offset, x_offset = position

    # 합성할 위치를 계산하여 이미지 합성
    background_img[y_offset:y_offset + h, x_offset:x_offset + w] = foreground_img

    return background_img

# 이미지 파일 경로
background_img_path = "C:\\Users\\김김주영\\Desktop\\ppt\\무지개 배경.jpg"
foreground_img_path = "C:\\Users\\김김주영\\Desktop\\ppt\\따봉페페.jpg"


# 이미지 로드
background_img = cv2.imread(background_img_path)
foreground_img = cv2.imread(foreground_img_path, cv2.IMREAD_UNCHANGED)

if background_img is None:
    print("배경 이미지를 읽을 수 없습니다.")
elif foreground_img is not None:
    # 전경 이미지를 합성할 위치 설정 (왼쪽 위 모서리 좌표)
    position = (100, 100)

    # 이미지 합성
    blended_img = blend_images(background_img.copy(), foreground_img, position)

    # 결과 이미지 출력
    cv2.imshow('Blended Image', blended_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("전경 이미지를 읽을 수 없습니다.")