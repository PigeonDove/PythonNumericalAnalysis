import numpy as np
import matplotlib.pyplot as plt

# 함수 정의: 적분 대상 함수 f(x) = √x
def f(x):
    return np.sqrt(x)

# 적분 구간 설정
first, last = 0, 4
m = 4                         # 구간 수 (짝수여야 함)
h = (last - first) / m        # 간격

# 초기화
areas = 0                     # 면적 총합

# 2칸씩 건너뛰며 3개 점(x0, x1, x2)을 사용해 면적 계산
i = 0
while i < m:
    x0 = first + i * h
    x1 = x0 + h
    x2 = x0 + 2*h

    area = (x2 - x0) / 6 * (f(x0) + 4*f(x1) + f(x2))  # 심슨의 법칙
    areas += area

    print(f"[{x0:.2f}, {x2:.2f}] -> f = ({f(x0):.4f}, {f(x1):.4f}, {f(x2):.4f}) , area = {area:.4f}")

    i += 2                             # 두 칸씩 진행

# 실제 정적분 값 계산
actual = (2/3) * last**(3/2)
error = abs(actual - areas) / actual * 100

# 결과 출력
print(f"\nSimpson's Rule Approximation: {areas:.4f}")
print(f"Actual Value: {actual:.4f}")
print(f"Relative Error: {error:.2f}%")
