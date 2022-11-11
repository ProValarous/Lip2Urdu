import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

IMG_SIZE = 128

def seg_sorter(seg: str):
    return int(seg[4:])

def load_segments(dir:str, start : int, end: int):
    data_path = dir
    data_arr = []
    path = os.listdir(data_path)
    path.sort(key=seg_sorter)
    for file in path[start:end]:
        seg_arr = []
        print(file)
        sub_path = os.path.join(data_path,file)
        for img in os.listdir(sub_path):
            img_path = os.path.join(data_path,file,img)
            a = cv2.imread(img_path)
            a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
            a = cv2.resize(a, (IMG_SIZE, IMG_SIZE)) 
            seg_arr.append(a)
        data_arr.append(seg_arr)
    nd_arr = np.array(data_arr)
    return nd_arr


def plot_segment(seg : np.ndarray):
    fig = plt.figure(figsize=(15,13))
    for i in range(75):  
        ax = fig.add_subplot(8, 10, i+1)
        ax.imshow(seg[i,:,:,:])
        ax.set_title('frame:{y}'.format(y=i))
        plt.axis('off')