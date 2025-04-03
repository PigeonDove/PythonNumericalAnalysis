import numpy as np  # numpy 라이브러리 불러오기
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 matplotlib 라이브러리 불러오기

# 실제 sqrt(2)의 값 (numpy의 sqrt 함수 이용)
actual_value = np.sqrt(2)

# 선형 보간법을 위한 두 개의 데이터 포인트 설정
x1, y1 = 1, np.sqrt(1)  # 첫 번째 데이터 포인트 (1, 1)
x2, y2 = 4, np.sqrt(4)  # 두 번째 데이터 포인트 (4, 2)

# 선형 보간법 공식 적용하여 sqrt(2) 값을 근사적으로 계산
x_pred = 2  # 보간을 수행할 x 값 (즉, sqrt(2)의 x 값)
y_pred = ((x_pred - x1) / (x2 - x1)) * (y2 - y1) + y1  # 선형 보간법 공식 적용

# 오차 계산 (상대 오차)
relative_error = (abs(actual_value - y_pred) / actual_value) * 100  # 상대 오차 계산

# 결과 출력 (콘솔 출력)
print(f"Actual sqrt(2) Value: {actual_value:.4f}")  # 실제 sqrt(2) 값 출력
print(f"Interpolated sqrt(2) Value: {y_pred:.4f}")  # 선형 보간법을 이용한 근사 sqrt(2) 값 출력
print(f"Relative Error: {relative_error:.2f}%")  # 상대 오차 출력

# 그래프 크기 설정
plt.figure(figsize=(6, 4))  # 가로 6, 세로 4 크기의 그래프 생성

# sqrt(x) 함수 그래프 그리기 (실제 제곱근 값)
x_values = np.linspace(0, 5, 100)  # 0부터 5까지 100개의 x 값을 생성
y_values = np.sqrt(x_values)  # 각 x 값에 대한 sqrt(x) 계산
plt.plot(x_values, y_values, label="y = sqrt(x)", color="blue")  # 그래프에 sqrt(x) 함수 곡선 추가

# 주어진 데이터 포인트 (x1, y1), (x2, y2) 표시
plt.scatter([x1, x2], [y1, y2], color='blue', label="Given Data Points")  # 데이터 포인트 점 표시
plt.plot([x1, x2], [y1, y2], 'k--', label="Interpolation Line")  # 보간 직선 추가 (점선)

# 보간된 sqrt(2) 값 표시
plt.scatter(x_pred, y_pred, color='red', label=f"Interpolated sqrt(2) ≈ {y_pred:.4f}")  # 보간된 값 점 표시

# 데이터 포인트에 라벨 추가
plt.text(x1, y1, f"({x1}, {y1})", verticalalignment='bottom', horizontalalignment='right', fontsize=10)  # (1,1) 라벨 추가
plt.text(x2, y2, f"({x2}, {y2})", verticalalignment='bottom', horizontalalignment='left', fontsize=10)  # (4,2) 라벨 추가
plt.text(x_pred, y_pred, f"({x_pred}, {y_pred:.4f})", verticalalignment='bottom', horizontalalignment='right', fontsize=10, color='red')  # 보간된 sqrt(2) 값 라벨 추가

# 그래프 제목 및 축 레이블 설정
plt.xlabel("x")  # x축 레이블 추가
plt.ylabel("y = sqrt(x)")  # y축 레이블 추가
plt.title("Linear Interpolation for sqrt(2)")  # 그래프 제목 설정
plt.legend()  # 범례 추가
plt.grid(True)  # 격자 추가하여 가독성 향상

# 그래프 출력
plt.show()  # 그래프 표시


