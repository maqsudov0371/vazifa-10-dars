import os
import re
import multiprocessing
from urllib.parse import urlparse

def downloder(cls):
    try:
        get_image = re.get(cls)
        get_image.image_status()

        getter = urlparse(cls)
        image_name = os.path.basename(getter.path)

        with open(image_name, 'wb') as f:
            f.write(get_image.content)
        print(f"Download {image_name} from {cls}")
    except get_image.exceptions.RequestException as elements:
        print(f"yuklaninshda xatolik {cls}: {elements}")

def main():
    images_url = [
        "https://images.unsplash.com/photo-1618042164219-62c820f10723?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZG93bmxvYWR8ZW58MHx8MHx8fDA%3D",
        "https://images.unsplash.com/photo-1549287748-f095932c9f81?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZG93bmxvYWR8ZW58MHx8MHx8fDA%3D",
        "https://images.unsplash.com/photo-1547699224-0924faf995c6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZG93bmxvYWR8ZW58MHx8MHx8fDA%3D"
    ]
    
    with multiprocessing.Pool(processes=len(images_url)) as pool:
        pool.map(downloder, images_url)

if __name__ == "__main__":
    main()