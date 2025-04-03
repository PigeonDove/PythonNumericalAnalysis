import numpy as np                # numpy 모듈을 np라는 이름으로 불러옴
import matplotlib.pyplot as plt   # matplotlib의 pyplot 모듈을 plt라는 이름으로 불러옴

# f(x) = sqrt(x) 함수에 따른 데이터 포인트 정의 (np.sqrt 사용)
x1, y1 = 1, np.sqrt(1)   # 첫 번째 데이터 포인트: x=1, y=sqrt(1)=1
x2, y2 = 4, np.sqrt(4)   # 두 번째 데이터 포인트: x=4, y=sqrt(4)=2
x3, y3 = 9, np.sqrt(9)   # 세 번째 데이터 포인트: x=9, y=sqrt(9)=3

# 보간할 x 값 설정 (여기서는 sqrt(2)를 근사하기 위해 x=2 사용)
x_interp = 2

# x=2에서의 첫 번째 라그랑주 기저 다항식 계산
L1 = ((x_interp - x2) * (x_interp - x3)) / ((x1 - x2) * (x1 - x3))
# x=2에서의 두 번째 라그랑주 기저 다항식 계산
L2 = ((x_interp - x1) * (x_interp - x3)) / ((x2 - x1) * (x2 - x3))
# x=2에서의 세 번째 라그랑주 기저 다항식 계산
L3 = ((x_interp - x1) * (x_interp - x2)) / ((x3 - x1) * (x3 - x2))

# x=2에서의 보간값 P_x 계산 (각 데이터 포인트의 y값과 기저 다항식의 곱의 합)
P_x = y1 * L1 + y2 * L2 + y3 * L3

# 실제 sqrt(2) 값 계산 (np.sqrt 사용)
actual_value = np.sqrt(2)

# 실제 값과 보간값의 상대 오차 계산
relative_error = abs((actual_value - P_x) / actual_value) * 100

# 결과 출력: 실제 sqrt(2), 보간된 sqrt(2), 상대 오차
print("Actual sqrt(2) Value: {:.6f}".format(actual_value))
print("Interpolated sqrt(2) Value: {:.6f}".format(P_x))
print("Relative Error: {:.4f}%".format(relative_error))

# 그래프에 사용할 x 값의 범위 생성 (0부터 9.5까지 500개의 점)
x_vals = np.linspace(0, 9.5, 500)

# 각 x에 대해 라그랑주 기저 다항식 계산
L1_vals = ((x_vals - x2) * (x_vals - x3)) / ((x1 - x2) * (x1 - x3))
L2_vals = ((x_vals - x1) * (x_vals - x3)) / ((x2 - x1) * (x2 - x3))
L3_vals = ((x_vals - x1) * (x_vals - x2)) / ((x3 - x1) * (x3 - x2))

# 각 기저 다항식에 해당하는 y값을 곱한 후 합산하여 보간 다항식의 y 값 계산
y_vals = y1 * L1_vals + y2 * L2_vals + y3 * L3_vals

# 실제 sqrt(x) 함수의 y 값 계산
actual_y_vals = np.sqrt(x_vals)

# 그래프 그리기 시작
plt.figure(figsize=(10, 6))  # 그림의 크기를 설정

# 보간 다항식 곡선 그리기 (파란색 실선)
plt.plot(x_vals, y_vals, label="Interpolated Polynomial", color="blue")

# 실제 sqrt(x) 함수 곡선 그리기 (주황색 점선)
plt.plot(x_vals, actual_y_vals, label="Actual sqrt(x) Function", color="orange", linestyle="--")

# 원래의 데이터 포인트를 붉은 점으로 표시
plt.scatter([x1, x2, x3], [y1, y2, y3], color="red", label="Data Points", zorder=5)

# x=2에서 보간된 값을 녹색 점으로 강조하여 표시
plt.scatter(x_interp, P_x, color="green", label="Interpolated value at x=2", zorder=5)

# x=2에서 실제 sqrt(2) 값을 보라색 점으로 표시
plt.scatter(x_interp, actual_value, color="purple", label="Actual sqrt(2) Value", zorder=5)

# x=2에서 보간된 값에 좌표 주석 추가 (녹색 점)
plt.annotate("Interpolated: ({:.2f}, {:.2f})".format(x_interp, P_x),
             xy=(x_interp, P_x),                   # 주석이 달릴 점의 좌표
             xytext=(x_interp + 0.5, P_x + 0.1),     # 주석 텍스트가 위치할 좌표
             arrowprops=dict(facecolor="black", arrowstyle="->"))  # 화살표 속성 설정

# x=2에서 실제 sqrt(2) 값에 좌표 주석 추가 (보라색 점)
plt.annotate("Actual: ({:.2f}, {:.2f})".format(x_interp, actual_value),
             xy=(x_interp, actual_value),          # 주석이 달릴 점의 좌표
             xytext=(x_interp + 0.5, actual_value - 0.2),  # 주석 텍스트가 위치할 좌표
             arrowprops=dict(facecolor="black", arrowstyle="->"))  # 화살표 속성 설정

plt.xlabel("x")  # x축 레이블 설정
plt.ylabel("y")  # y축 레이블 설정
plt.title("Quadratic Lagrange Interpolation for sqrt(x) and Comparison with Actual Function")  # 그래프 제목 설정
plt.legend()     # 범례 표시
plt.grid(True)   # 격자 표시
plt.show()       # 그래프 출력
