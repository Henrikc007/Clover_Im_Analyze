import numpy as np
import matplotlib.pyplot as plt
import torch

x_train = np.array ([[4.7], [2.4], [7.5] , [4.3], [7.816], 
                    [8.9], [5.2], [8.59], [2.1], [8], 
                    [10], [4.5], [6], [4]],
                    dtype = np.float32)

y_train = np.array ([[2.6], [1.6], [3.09] , [2.4], [3.357], 
                    [2.6], [1.96], [3.53], [1.76], [3.2], 
                    [3.5], [1.6], [2.5], [2.2]],
                    dtype = np.float32)

print(x_train)

plt.figure(figsize=(12,8))
plt.scatter(x_train,y_train,label='original data', s=250, c='g')

plt.legend()
#plt.show()

X_train = torch.from_numpy(x_train)
Y_train = torch.from_numpy(y_train)

print('requires_grad for X_train', X_train.requires_grad)
print('requires_grad for Y_train', Y_train.requires_grad)

input_size=1
hidden_size=1
output_size=1

w1 = torch.rand(input_size,
                hidden_size,
                
                requires_grad=True)

w2 = torch.rand(hidden_size,
                output_size,
                
                requires_grad=True)
print(w1.shape)
print(w2.shape)

learning_rate = 1e-7

for iter in range(1,10000):
    y_pred = X_train.mm(w1).mm(w2)
    loss = (y_pred - Y_train).pow(2).sum()
    
    if iter % 500 ==0:
        print(iter, loss.item())
        
    loss.backward()
    
    with torch.no_grad():
        w1_= learning_rate * w1.grad
        w2_= learning_rate * w2.grad
        w1.grad.zero_()
        w2.grad.zero_()
        
print('w1: ',w1 )
print('w2: ', w2)

x_train_tensor=torch.from_numpy(x_train)
y_predicted_tensor=x_train_tensor.mm(w1).mm(w2)
predicted=y_predicted_tensor.detach().numpy()
plt.plot(x_train_tensor,predicted,label='fitted line')


#adding a random data that fits a linear relationship

# new_x_data=x_train
# new_a=np.random.default_rng()
# new_b=np.random.default_rng()
# new_y_data=(np.random.random_sample((13,))-0.5)*2
# new_y_data=(new_x_data*new_a.random())+(new_a.random())+new_y_data
# new_x_tensor=torch.from_numpy(new_x_data)

# print(new_x_tensor)
# new_y_predicted_tensor=new_x_tensor.mm(w1).mm(w2)
# new_predicted=new_y_predicted_tensor.detach().numpy()
# plt.scatter(new_x_data,new_y_data,label='random dataset',s=250,c='r')
# plt.plot(new_x_data,new_predicted,label='fitted line')

plt.show()