import numpy as np
import scipy.ndimage as nd
import scipy.io as io
import os
LOCAL_PATH = "/home/ets/lixiang/tf-3dgan-master/sample-data/volumetric_data/"
def getVoxelFromMat(path, cube_len=64):
    voxels = io.loadmat(path)['instance']
    voxels = np.pad(voxels,(1,1),'constant',constant_values=(0,0))
    if cube_len != 32 and cube_len == 64:
        voxels = nd.zoom(voxels, (2,2,2), mode='constant', order=0)
    return voxels
def transferMatToVoxel(directory_list):
    i  = 0
    for i in range(len(directory_list)):
        # so far the path of  object iterating
        objPath = directory_list[i] + "/30" + "/train/"
        obj = os.path.split(directory_list[i])[-1]
        matList = [f for f in os.listdir(objPath) if f.endswith('.mat')]
        for mat in matList:
            mat_name = os.path.splitext(mat)[0]
            volume = np.asarray(getVoxelFromMat(objPath + mat, 64),dtype=np.bool)
            np.save("../sample-data/volumetric_data/" + obj + "/30/train/" + mat_name + ".npy", volume)
if __name__ == '__main__':
    directory_list = []
    files = os.listdir(LOCAL_PATH)
    #get each directory's path
    for file in files:
        m = os.path.join(LOCAL_PATH, file)
        directory_list.append(m)
    transferMatToVoxel(directory_list)


