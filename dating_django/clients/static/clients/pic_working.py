from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(input_image_path,
                   text, pos):

    photo = Image.open(input_image_path)
    photo = photo.convert('RGB')
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype('clients/static/clients/utils/arial.ttf', 50)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(input_image_path)


# watermark_text(input_image_path='media/cheetos.jpeg',
#                text='DatingSite',
#                pos=(0, 0))