from rembg import remove
from PIL import Image

input_path = 'a_man.jpg'
output_path = 'rmMANpi3c.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
