import numpy as np              # 수학 연산을 위한 numpy 모듈 불러오기
import matplotlib.pyplot as plt # 시각화를 위한 matplotlib 모듈 불러오기

# 함수 정의: 적분할 대상 함수 f(x) = √x
def f(x):
    return np.sqrt(x)

# 적분 구간 설정
first, last = 0, 4              # 구간 [0, 4]
step = 1                        # 직사각형의 너비 (간격)

# 시작 위치 초기화
i = first                       # 반복문 초기값
areas = 0                       # 넓이 총합 초기값

# 시작 구간 ~ 마지막 구간까지 반복
while i < last :
    width = step                                  # 직사각형의 가로 길이
    mid = (i + (i + step)) / 2                    # 중간값 계산
    height = f(mid)                               # 함수 f에서의 높이값 계산
    area = width * height                         # 넓이 계산
    areas += area                                 # 총 넓이에 누적
    print(f"{mid:.2f} , {height:.4f} , {area:.4f}") # 각 단계별 정보 출력

    i += step                                     # 다음 구간으로 이동

# 실제 적분값 계산: ∫₀⁴ √x dx = (2/3) * 4^(3/2) = (2/3) * 8 = 16/3
actual = (2/3) * last**(3/2)                       # 정확한 적분값
error = abs(actual - areas) / actual * 100         # 상대 오차 계산 (%)

# 결과 출력
print(f"Midpoint Rule Approximation: {areas:.4f}") # 직사각형법 적분 근사값 출력
print(f"Actual Value: {actual:.4f}")               # 실제 적분값 출력
print(f"Relative Error: {error:.2f}%")             # 상대 오차 출력