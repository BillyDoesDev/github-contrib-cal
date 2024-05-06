from PIL import Image

def get_chart(path:str, rows, cols) -> dict:
    img = Image.open(path).convert(mode="L")
    scaley = img.height // rows + 1
    scalex = img.width // cols + 1

    data = {}
    y_index = 0
    for y in range(0, img.height, scaley):
        x_index = 0
        for x in range(0, img.width, scalex):
            
            box = []
            for y_ in range(y, y + scaley):
                for x_ in range(x, x + scalex):
                    try:
                        box.append(img.getpixel((x_, y_)))
                    except IndexError:
                        pass
            
            avg = sum(box) // len(box)
            data[f"{x_index}x{y_index}"] = avg
            x_index += 1
        #     print(f"{'*' if avg < 127 else ' '}", end="")
        y_index += 1
        # print()
    
    return data


if __name__ == "__main__":
    print(get_chart("assets/text.png", rows=7, cols=52))
        