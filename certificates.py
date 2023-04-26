import csv
from PIL import Image, ImageDraw, ImageFont

NAME_FONT = ImageFont.truetype("bold.ttf", 72)
NAME_COORDS = (150, 735)


def read_csv():
    data = []

    with open("Certificate.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append({"name": row[0].strip()})

    return data

def write_name(name):
    template = Image.open("cert.png")
    CANVAS = ImageDraw.Draw(template)

    CANVAS.text(NAME_COORDS, name, font=NAME_FONT, fill=(0, 0, 0))
    return template
        
def main():

    data = read_csv()

    for item in data:
        template = write_name(item['name'])
        template.save(f"generated/{item['name']}.png")


if __name__ == "__main__":
    main()