import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

for i in range(1, 4):
    path = 'lunar0' + str(i) + '_raw.jpg' 
    img = Image.open(path)
    data = np.array(img).astype(float)

    min_val = np.min(data)
    max_val = np.max(data)

    scale = 255.0 / (max_val - min_val + 1e-9)
    upd = ((data - min_val) * scale).astype(np.uint8)

    new_file_path = 'moon' + str(i) + '.png'
    res_img = Image.fromarray(upd)
    res_img.save(new_file_path)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.imshow(data, cmap='gray', vmin=0, vmax=255)
    ax1.set_title("raw", fontsize=14)

    ax2.imshow(upd, cmap='gray', vmin=0, vmax=255)
    ax2.set_title("contrast", fontsize=14)

    plt.subplots_adjust(wspace=0.1)
    plt.savefig('moon_comparison.png')
    plt.show()