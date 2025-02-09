"""
Author: Benny
Date: Nov 2019
"""
import argparse
import os
import nibabel as nib
from pathlib import Path
import sys
from tqdm import tqdm
import numpy as np

def main():
    for data in [x for x in os.listdir('./data/ribfrac/ribfrac-train-images-1/Part1/')]:
        try:
            source = nib.load('./data/ribfrac/ribfrac-train-images-1/Part1/'+data)
            source = source.get_fdata()
            source[source >= 200] = 1
            source[source != 1] = 0

            label = nib.load('./data/RibSeg/nii/'+data[:-12]+'rib-seg.nii.gz')
            label = label.get_fdata()

            temp = np.argwhere(source == 1)
    #         choice = np.random.choice(temp.shape[0], 30000, replace=False)
    ##         downsample
    #         points = temp[choice, :]

            label_selected_points = []
            for i in temp:
                label_selected_points.append(label[i[0]][i[1]][i[2]])
            label_selected_points = np.array(label_selected_points)
            np.save('./data/pn/data_pn/train'+data[:-13], temp)
            np.save('./data/pn/label_pn/train' + data[:-13], label_selected_points)
        except:
            print(data,"has no label file.")


    for data in [x for x in os.listdir('./data/ribfrac/ribfrac-train-images-2/Part2/')]:
        try:
            source = nib.load('./data/ribfrac/ribfrac-train-images-2/Part2/'+data)
            source = source.get_fdata()
            source[source >= 200] = 1
            source[source != 1] = 0

            label = nib.load('./data/RibSeg/nii/'+data[:-12]+'rib-seg.nii.gz')
            label = label.get_fdata()

            temp = np.argwhere(source == 1)
    #         choice = np.random.choice(temp.shape[0], 30000, replace=False)
    #         # downsample
    #         points = temp[choice, :]

            label_selected_points = []
            for i in temp:
                label_selected_points.append(label[i[0]][i[1]][i[2]])
            label_selected_points = np.array(label_selected_points)
            np.save('./data/pn/data_pn/train'+data[:-13], temp)
            np.save('./data/pn/label_pn/train' + data[:-13], label_selected_points)
        except:
            print(data,"has no label file.")


    for data in [x for x in os.listdir('./data/ribfrac/ribfrac-val-images/')]:
        try:
            source = nib.load('./ribfrac/ribfrac-val-images/' + data)
            source = source.get_fdata()
            source[source >= 200] = 1
            source[source != 1] = 0

            label = nib.load('./data/RibSeg/nii/' + data[:-12] + 'rib-seg.nii.gz')
            label = label.get_fdata()

            temp = np.argwhere(source == 1)
    #         choice = np.random.choice(temp.shape[0], 30000, replace=False)
    #         # downsample
    #         points = temp[choice, :]

            label_selected_points = []
            for i in temp:
                label_selected_points.append(label[i[0]][i[1]][i[2]])
            label_selected_points = np.array(label_selected_points)
            np.save('./data/pn/data_pn/val' + data[:-13], temp)
            np.save('./data/pn/label_pn/val' + data[:-13], label_selected_points)
        except:
            print(data,"has no label file.")


    for data in [x for x in os.listdir('./data/ribfrac/ribfrac-test-images/')]:
        try:
            source = nib.load('./data/ribfrac/ribfrac-test-images/'+data)
            source = source.get_fdata()
            source[source >= 200] = 1
            source[source != 1] = 0

            label = nib.load('./data/RibSeg/nii/'+data[:-12]+'rib-seg.nii.gz')
            label = label.get_fdata()

            temp = np.argwhere(source == 1)
    #         choice = np.random.choice(temp.shape[0], 30000, replace=False)
    #         # downsample
    #         points = temp[choice, :]

            label_selected_points = []
            for i in temp:
                label_selected_points.append(label[i[0]][i[1]][i[2]])
            temp = np.array(temp)
            np.save('./data/pn/data_pn/test'+data[:-13], temp)
            np.save('./data/pn/label_pn/test' + data[:-13], label_selected_points)
        except:
            print(data,"has no label file.")

if __name__ == '__main__':
    main()

