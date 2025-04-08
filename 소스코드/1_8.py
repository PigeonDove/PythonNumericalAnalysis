import numpy as np
import matplotlib.pyplot as plt

# 세 개의 데이터 포인트
x1, y1 = 10, 20
x2, y2 = 12, 36
x3, y3 = 14, 60

# x 값 범위 생성 (보간 곡선을 그리기 위한 범위)
x_vals = np.linspace(9.5, 14.5, 500)

# 각 x 값에서의 라그랑주 보간 다항식 계산
L1_vals = ((x_vals - x2)*(x_vals - x3)) / ((x1 - x2)*(x1 - x3))
L2_vals = ((x_vals - x1)*(x_vals - x3)) / ((x2 - x1)*(x2 - x3))
L3_vals = ((x_vals - x1)*(x_vals - x2)) / ((x3 - x1)*(x3 - x2))

# 보간된 y 값
y_vals = y1 * L1_vals + y2 * L2_vals + y3 * L3_vals

# 예측할 시각 리스트
x_interp_list = np.linspace(10.4, 13.6, 9)
predicted_vals = []

# 예측된 대기시간 계산
for x_interp in x_interp_list:
    L1 = ((x_interp - x2)*(x_interp - x3)) / ((x1 - x2)*(x1 - x3))
    L2 = ((x_interp - x1)*(x_interp - x3)) / ((x2 - x1)*(x2 - x3))
    L3 = ((x_interp - x1)*(x_interp - x2)) / ((x3 - x1)*(x3 - x2))
    P_x = y1 * L1 + y2 * L2 + y3 * L3
    predicted_vals.append(P_x)

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 라그랑주 보간 곡선
plt.plot(x_vals, y_vals, label="Interpolated Wait Time", color="blue")

# 실제 데이터 포인트
plt.scatter([x1, x2, x3], [y1, y2, y3], color="red", label="Original Data Points", zorder=5)

# 예측된 값들 표시
plt.scatter(x_interp_list, predicted_vals, color="green", label="Predicted Times", zorder=5)

# 각 예측된 점에 주석 달기 (간단히)
for xi, yi in zip(x_interp_list, predicted_vals):
    plt.annotate("{:.1f}".format(yi), (xi, yi), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

# 꾸미기
plt.title("Theme Park Waiting Time Prediction (Lagrange Interpolation)")
plt.xlabel("Time (Hour)")
plt.ylabel("Waiting Time (Minutes)")
plt.legend()
plt.grid(True)
plt.show()
