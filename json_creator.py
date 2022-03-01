import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
url_append = 'https://raw.githubusercontent.com/The-4th-Hokage/naruto-card-game-images/master/photo_data/'

photo_dir = BASE_DIR / "photo_data"
photo_data_dict = {}

for foldername in os.listdir(photo_dir):
    list_images = []
    for filename in os.listdir(photo_dir / foldername):
        if os.path.isdir(photo_dir / os.path.join(foldername, filename)):
            for i in os.listdir(photo_dir / os.path.join(foldername, filename)):
                list_images.append(url_append+filename+'/'+i)
            photo_data_dict.update({filename.lower(): {'images':list_images, 'category': foldername}})
        else:
            list_images.append(url_append+filename)
            photo_data_dict.update({filename[:-4].lower(): {'images':list_images, 'category': foldername}})

with open('img_data.json','w') as f:
    f.write(json.dumps(photo_data_dict, indent=4))