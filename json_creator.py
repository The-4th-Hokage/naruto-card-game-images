import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
url_append = 'https://raw.githubusercontent.com/The-4th-Hokage/naruto-card-game-images/master/photo_data/'

photo_dir = BASE_DIR / "photo_data"
photo_data_dict = {}

for category in os.listdir(photo_dir):
    for filename in os.listdir(photo_dir / category):
        list_images = []
        if os.path.isdir(photo_dir / os.path.join(category, filename)):
            for j in os.listdir(photo_dir / os.path.join(category, filename)):
                list_images.append(url_append+category+'/'+filename+'/'+j)
            photo_data_dict.update({filename.lower(): {'images':list_images, 'category': category}})
        else:
            list_images.append(url_append+category+'/'+filename)
            photo_data_dict.update({filename[:-4].lower(): {'images':list_images, 'category': category}})

with open('img_data.json','w') as f:
    f.write(json.dumps(photo_data_dict, indent=4))