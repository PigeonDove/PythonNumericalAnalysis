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
i = 1
areas = 0                     # 면적 총합

# 그래프 시각화를 위한 좌표 리스트
x_curve = np.linspace(first, last, 400)       # 원함수 곡선 그릴 x값
y_curve = f(x_curve)                          # 원함수 곡선 y값

x_parabola_sections = []                      # 각 심슨 구간의 x좌표 저장
y_parabola_sections = []                      # 각 심슨 구간의 y좌표 저장

# Simpson's Rule 계산 및 시각화용 좌표 수집
while i <= m // 2:
    x1 = first + (2*i - 2) * h
    x2 = first + (2*i - 1) * h
    x3 = first + (2*i) * h

    area = (x3 - x1) / 6 * (f(x1) + 4*f(x2) + f(x3))
    areas += area

    print(f"[{x1:.2f}, {x3:.2f}] -> f = ({f(x1):.4f}, {f(x2):.4f}, {f(x3):.4f}) , area = {area:.4f}")

    # 구간 내 부드러운 포물선 좌표 수집
    x_local = np.linspace(x1, x3, 100)
    # 라그랑주 보간 다항식(Lagrange interpolation)으로 포물선 계산
    y_local = f(x1)*(x_local - x2)*(x_local - x3)/((x1 - x2)*(x1 - x3)) \
            + f(x2)*(x_local - x1)*(x_local - x3)/((x2 - x1)*(x2 - x3)) \
            + f(x3)*(x_local - x1)*(x_local - x2)/((x3 - x1)*(x3 - x2))

    x_parabola_sections.append(x_local)
    y_parabola_sections.append(y_local)

    i += 1

# 실제 정적분 값 계산
actual = (2/3) * last**(3/2)
error = abs(actual - areas) / actual * 100

# 결과 출력
print(f"\nSimpson's Rule Approximation: {areas:.4f}")
print(f"Actual Value: {actual:.4f}")
print(f"Relative Error: {error:.2f}%")

# ---------------- 그래프 시각화 ----------------

plt.figure(figsize=(8, 5))

# 원래 함수 곡선 그리기
plt.plot(x_curve, y_curve, color='blue', label='f(x) = √x')

# 각 심슨 포물선 구간을 그리기
for idx, (x_sec, y_sec) in enumerate(zip(x_parabola_sections, y_parabola_sections)):
    plt.fill_between(x_sec, 0, y_sec, color='orange', alpha=0.4,
                     label='Simpson Parabolas' if idx == 0 else "")
    plt.plot(x_sec, y_sec, color='black', linewidth=1)

# 그래프 설정
plt.title("Numerical Integration using Simpson's Rule")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
