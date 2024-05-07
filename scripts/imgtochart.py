from PIL import Image, ImageOps
import os
import math
import json

def get_chart(path:str, rows, cols, inv, disp=False) -> dict: # returns a coordinate : luminosity mapping
    img = Image.open(path).convert(mode="L")
    # img = ImageOps.invert(img)
    img = img.resize((rows * img.width // img.height, rows), resample=Image.NEAREST) # or use Image.NEAREST
    
    data = {}
    for y in range(rows):
        for x in range(cols):
            try:
                data[f"{x}x{y}"] = math.floor(img.getpixel((x, y)) / (256 / 5))
            except IndexError:
                data[f"{x}x{y}"] = 4
            
            if inv: data[f"{x}x{y}"] = 4 - data[f"{x}x{y}"] % 4 if data[f"{x}x{y}"] != 4 else 0

            if disp: print(" " if data[f"{x}x{y}"] == 4 else data[f"{x}x{y}"], end="")
        if disp: print()

    return data


def get_frames(video_path:str, rows, cols, inv, disp=False, cache_reload=False) -> dict:

    if not cache_reload:
        print("attempting reload from cache...")
        try:
            with open(".frames_cache.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            pass

    print("computing frame info...")
    data = {}
    # print(len(os.listdir(os.path.join(video_path))))
    for index in range(1, len(os.listdir(os.path.join(video_path))) + 1):
        print(f"processing frame{index}...")
        data[f"frame{index}"] = get_chart(os.path.join(video_path, f"frame{index}.png"), rows, cols, inv, disp)
    print("Done!")

    # cache this for later...
    with open(".frames_cache.json", mode="w", encoding="utf-8") as f:
        print("caching frame info...")
        f.write(json.dumps(data, indent=4))
    return data


if __name__ == "__main__":
    # get_chart("assets/frames/frame5197.png", rows=7, cols=52, inv=False, disp=True)
    get_frames("assets/frames", rows=7, cols=52, inv=False, disp=True, cache_reload=True)
