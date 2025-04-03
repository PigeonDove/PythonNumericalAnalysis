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