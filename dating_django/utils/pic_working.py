from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):

    photo = Image.open(input_image_path)
    photo = photo.convert('RGB')
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("/Users/rodionibragimov/Documents/DatingSite/dating_django/utils/arial.ttf", 50)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)
