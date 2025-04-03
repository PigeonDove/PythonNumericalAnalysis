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