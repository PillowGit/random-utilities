from os import walk, listdir
#from rich import print
from PIL import Image

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
def get_ascii_char(val: int) -> str:
    return ASCII_CHARS[val // 4]

def find_local_images() -> list[str]:
    # Try to find all the files in the current directory
    file_filter = lambda f: f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".webp")
    files = []
    for f in listdir("."):
        if file_filter(f):
            files.append(f)
    # If there are no files, print a message and return
    if not files:
        raise Exception("No images found in the current directory or subdirectories")
    else:
        return files

def get_file_choice(files: list[str]) -> str:
    # Print the files and ask the user to choose one
    print("Pick an image to convet:")
    for i, f in enumerate(files):
        print(f"[{i+1}] {f}")
    choice = int(input("Enter the number of the file you want to use: "))-1
    # Return their choice
    return files[choice]

def open_img_in_greyscale(file: str) -> Image.Image:
    img = Image.open(file)
    img.thumbnail((img.width//4, img.height//4))
    return img.convert("L")

def extract_pixels(img: Image.Image) -> list[list[int]]:
    w = img.width
    pixels = [[]]
    for pixel in img.getdata():
        pixels[-1].append(pixel)
        if len(pixels[-1]) == w:
            pixels.append([])
    pixels.pop()
    return pixels

def run() -> None:
    files = find_local_images()
    choice = get_file_choice(files)
    print(f"Your choice: {choice}")
    img = open_img_in_greyscale(choice)
    pixels = extract_pixels(img)
    out = ""
    for r in pixels:
       out += " ".join([get_ascii_char(p) for p in r]) + "\n"
    print(out)
    open(choice[:choice.find(".")] + "_but_ascii.txt","w").write(out)

if __name__ == "__main__":
    run()
