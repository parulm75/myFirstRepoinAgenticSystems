import numpy as np
np.random.seed(42)
arr=np.random.rand(200,4)
mean_arr=np.mean(arr, axis=0)
std_arr=np.std(arr,axis=0)
normal_arr=(arr-mean_arr)/std_arr
train_data=arr[:round(0.8*len(arr))]
test_data=arr[round(0.8*len(arr)):]
train_data[5][2]=5
print(arr.shape)
print(mean_arr.shape)
print(train_data.shape)
print(test_data.shape)
print("Note: Modifying the slice affected the original array")
print(mean_arr)
print(std_arr)
print(normal_arr)