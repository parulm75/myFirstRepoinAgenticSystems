import numpy as np
arr=np.array([1,3,5,23,2,13,24,4,31,23,45,5])
mean=np.sum(arr)/len(arr)
new_arr=((arr-mean)**2)/len(arr)
std=np.sum(new_arr)**0.5
normal=np.round((arr-mean)/std,2)
reshaped_arr=normal.reshape(3,4)
print(f"Original data: {arr}")
print(f"Mean: {mean:.2f}")
print(f"Standard Devisation: {std:.2f}")
print(f"Normalised data: {normal}")
print(f"Reshaped data shape: {reshaped_arr.shape}")
