import requests
from bs4 import BeautifulSoup
import webbrowser

def search_images(keyword,num_images):
    url = f"https://www.google.com/search?q=부산+{keyword}+바닷가&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = []
    for img in soup.find_all('img', limit=num_images):
        image_url = img['src']
        if not image_url.endswith('.gif'):
            image_urls.append(image_url)

    return image_urls


keyword = input("검색할 키워드 입력: ")
num_images = 2
image_urls = search_images(keyword, num_images)


for url in image_urls:
    webbrowser.open_new_tab(url)
