import numpy as np

x = np.array([1, 2, 3])
pi = np.array([0.1, 0.1, 0.8])
# #期望值
e = np.sum(x * pi)
print('E_pi[x]:', e)
# #蒙特卡洛方法
# n = 100
# samples =[]
# for _ in range(n):
#     s = np. random.choice(x, p=pi) # 使用 pi 进行采样
#     samples.append(s)

# mean = np.mean(samples)
# var = np.var(samples)
# print('MC: {:.2f} (var: {:.2f})'.format(mean, var))


b = np.array([0.2, 0.2, 0.6]) # 修改概率分布
n = 100
samples =[]
for _ in range(n):
	idx = np.arange(len(b)) # [0, 1, 2]
	i = np.random.choice(idx, p=b)
	s = x[i]
	rho = pi[i] / b[i]
	samples.append(rho * s)
mean = np.mean(samples)
var = np.var(samples)
print('IS: {:.2f} (var: {:.2f})'.format(mean, var))