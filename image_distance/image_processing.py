from PIL import ImageDraw, ImageFont

def process_image(image, x1, y1, x2, y2, real_distance):
    processed_image = image.copy()
    draw = ImageDraw.Draw(processed_image)
    draw.line((x1, y1, x2, y2), fill="black", width=2)
    draw.ellipse((x1-3, y1-3, x1+3, y1+3), fill="blue")
    draw.ellipse((x2-3, y2-3, x2+3, y2+3), fill="blue")

    font = ImageFont.truetype("arial.ttf", 20)
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    text = f"{real_distance:.2f} mm"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    draw.text((mid_x - text_width / 2, mid_y - text_height / 2), text, fill="blue", font=font)
    return processed_image
