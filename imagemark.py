from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
    W, H = photo.size
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    black = (112, 128, 144)
    font = ImageFont.truetype("./font.ttf", 12)
    w, h = drawing.textsize(text)
    drawing.text(((W-w)/2,0), text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)