import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

size = 100

datas_x = list(range(size)) * size
datas_y = [i for i in range(size) for _ in range(size)]
datas_z = np.random.random(size**2).tolist()
datas_out = [0] * size ** 2

datas_scan_y_z = []

for k in range(size):
	datas_scan_y_z.append(size * k - 0)
print(datas_z)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection = "3d")
size_read = size
size_read_bf = 0

line_2 = ax.scatter(datas_x, datas_y, datas_z, c = datas_z, cmap = 'gist_earth', marker = "o")
#line_og = ax.scatter(datas_x, datas_y, datas_z, color = "#e3dfde", marker = ".")
line, = ax.plot(datas_x[size_read_bf:size_read], datas_y[size_read_bf:size_read], datas_z[size_read_bf:size_read], marker = ".", color = 'red')
liney, = ax.plot(list(map(lambda x:datas_x[x], datas_scan_y_z)), list(map(lambda x:datas_y[x], datas_scan_y_z)), list(map(lambda x:datas_z[x], datas_scan_y_z)), marker = ".", color = 'green')
fig.colorbar(line_2)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

speed = 0.2
flatness_scan = 5 #*fns
corner_point = 2

p = 0

for a in range(flatness_scan * size):
	print(f"Info [{a}]: Is working! -> {round(a / flatness_scan * size * 100, 1)}%")
	line.set_xdata(datas_x[size_read_bf:size_read])
	line.set_ydata(datas_y[size_read_bf:size_read])
	line.set_3d_properties(datas_z[size_read_bf:size_read]) 
	liney.set_xdata(list(map(lambda x:datas_x[x], datas_scan_y_z)))
	liney.set_ydata(list(map(lambda x:datas_y[x], datas_scan_y_z)))
	liney.set_3d_properties(list(map(lambda x:datas_z[x], datas_scan_y_z))) 
	line_2._offsets3d = (datas_x, datas_y, datas_z)
	line_2.set_array(datas_z)
	plt.pause(speed)
	plt.draw()
	for i in range(len(datas_z[size_read_bf:size_read]) - corner_point):
		fist_num = datas_z[size_read_bf:size_read][i]
		end_num = datas_z[size_read_bf:size_read][i+corner_point]

		average = (fist_num + end_num) / 2

		datas_z.pop(round(i+size_read_bf))
		datas_z.insert(round(i+size_read_bf), average)
		datas_z.pop(round(i+size_read_bf+corner_point/2))
		datas_z.insert(round(i+size_read_bf+corner_point/2), average)
		datas_z.pop(round(i+size_read_bf+corner_point))
		datas_z.insert(round(i+size_read_bf+corner_point), average)
	
	datas_scan_y_z.clear()
	
	for i in range(size):
		fist_num = datas_z[size * i + p]
		if size * (i + 2) + p < size**2:
			end_num = datas_z[size * (i + 2) + p]

			average = (fist_num + end_num) / 2
			datas_z.pop(size * i + p)
			datas_z.insert(size * i + p, average)
			datas_z.pop(size * (i + 1) + p)
			datas_z.insert(size * (i + 1) + p, average)
			datas_z.pop(size * (i + 2) + p)
			datas_z.insert(size * (i + 2) + p, average)

		datas_scan_y_z.append(size * i + p)
		print(size * (i + 2) + p)
	if size_read == len(datas_x):
		size_read_bf = 0
		size_read = size
	else:
		size_read_bf += size
		size_read += size
	
	if p == size - 1:
		p = 0
	else:
		p += 1

print(f"Info [{a}]: End work! -> 100%")
plt.show()


"""import matplotlib.pyplot as plt
import numpy as np
import time

# Dữ liệu ban đầu
x = np.random.rand(10)
y = np.random.rand(10)

# Tạo biểu đồ phân tán ban đầu
scatter_plot = plt.scatter(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Dynamic Scatter Plot')
plt.show(block=False)

# Cập nhật liên tục biểu đồ
for i in range(100):
    # Cập nhật dữ liệu mới
    x = np.random.rand(10)
    y = np.random.rand(10)
    
    # Cập nhật vị trí các điểm dữ liệu trong biểu đồ phân tán
    scatter_plot.set_offsets(np.column_stack((x, y)))
    
    # Hiển thị biểu đồ
    plt.pause(0.0001)  # Tạm dừng 0.5 giây để tạo hiệu ứng liên tục

plt.show()"""
"""import matplotlib.pyplot as plt
import numpy as np
import time

# Dữ liệu ban đầu
datas_x = np.random.rand(10)
datas_y = np.random.rand(10)
datas_z = np.random.rand(10)

# Tạo biểu đồ phân tán 3D ban đầu
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter_plot = ax.scatter(datas_x, datas_y, datas_z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Dynamic 3D Scatter Plot')
plt.show(block=False)

# Cập nhật liên tục biểu đồ
for i in range(100):
    # Cập nhật dữ liệu mới
    datas_x = np.random.rand(10)
    datas_y = np.random.rand(10)
    datas_z = np.random.rand(10)
    
    # Cập nhật vị trí các điểm dữ liệu trong biểu đồ phân tán 3D
    scatter_plot._offsets3d = (datas_x, datas_y, datas_z)
    
    # Hiển thị biểu đồ
    plt.draw()
    plt.pause(0.1)  # Tạm dừng 0.1 giây để tạo hiệu ứng liên tục

plt.show()"""
