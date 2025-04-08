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

# 12시에서 보간값 계산
x_interp = 12
L1 = ((x_interp - x2)*(x_interp - x3)) / ((x1 - x2)*(x1 - x3))
L2 = ((x_interp - x1)*(x_interp - x3)) / ((x2 - x1)*(x2 - x3))
L3 = ((x_interp - x1)*(x_interp - x2)) / ((x3 - x1)*(x3 - x2))
P_x = y1 * L1 + y2 * L2 + y3 * L3

# 결과 출력
print("Predicted wait time at 12:00 using quadratic Lagrange interpolation:")
print(f"Time: {x_interp}h, Predicted Wait Time: {P_x:.2f} min")

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 라그랑주 보간 곡선
plt.plot(x_vals, y_vals, label="Lagrange Interpolation Curve", color="blue")

# 원래 데이터 포인트 표시
plt.scatter([x1, x2, x3], [y1, y2, y3], color="red", label="Original Data Points", zorder=5)

# 12시 예측값 점 표시
plt.scatter(x_interp, P_x, color="green", label="Predicted at 12:00", zorder=5)

# 주석 달기
plt.annotate(f"{P_x:.1f}", (x_interp, P_x),
             textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9)

# 꾸미기
plt.title("Theme Park Wait Time Prediction at 12:00 (Quadratic Lagrange Interpolation)")
plt.xlabel("Time (Hour)")
plt.ylabel("Waiting Time (Minutes)")
plt.grid(True)
plt.legend()
plt.show()
