import numpy as np              # 수학 연산을 위한 numpy 모듈 불러오기
import matplotlib.pyplot as plt # 시각화를 위한 matplotlib 모듈 불러오기

# 함수 정의: 적분할 대상 함수 f(x) = √x
def f(x):
    return np.sqrt(x)

# 적분 구간 설정
first, last = 0, 4              # 구간 [0, 4]
m = 4                           # 구간 수 (짝수만 가능)
h = (last - first) / m          # 간격

# 시작 위치 초기화
i = 0
areas = 0

# 시각화를 위한 점 저장 리스트
x_vals_simpson = []
y_vals_simpson = []
area_patches = []               # 면적 시각화를 위한 패치 정보

# 2칸씩 건너뛰며 3개 점(x1, x2, x3)을 사용해 면적 계산
while i < m:
    x1 = first + i * h
    x2 = x1 + h
    x3 = x1 + 2*h

    area = (x3 - x1) / 6 * (f(x1) + 4*f(x2) + f(x3))  # 심슨의 법칙
    areas += area

    print(f"[{x1:.2f}, {x2:.2f}] -> f = ({f(x3):.4f}, {f(x2):.4f}, {f(x3):.4f}) , area = {area:.4f}")

    # 시각화용 점 저장
    x_vals_simpson.extend([x1, x2])
    y_vals_simpson.extend([f(x1), f(x2)])

    # 면적 시각화용 패치 저장 (곡선으로 채우기 위해 세 점 보간)
    x_patch = np.linspace(x1, x3, 100)
    # 라그랑주 보간식 기반 근사 곡선 생성
    def P(x):  # 2차 다항 근사식
        return f(x1) * (x - x2)*(x - x3) / ((x1 - x2)*(x1 - x3)) + \
               f(x2) * (x - x1)*(x - x3) / ((x2 - x1)*(x2 - x3)) + \
               f(x3) * (x - x1)*(x - x2) / ((x3 - x1)*(x3 - x2))

    y_patch = P(x_patch)
    area_patches.append((x_patch, y_patch))

    i += 2

# 실제 적분값 계산: ∫₀⁴ √x dx = (2/3) * 4^(3/2) = 16/3
actual = (2/3) * last**(3/2)
error = abs(actual - areas) / actual * 100

# 결과 출력
print(f"\nSimpson's Rule Approximation: {areas:.4f}")
print(f"Actual Value: {actual:.4f}")
print(f"Relative Error: {error:.2f}%")

# ----------------- 그래프 시각화 -------------------

# 부드러운 곡선을 위한 x값 생성
x_curve = np.linspace(first, last, 400)
y_curve = f(x_curve)

# 그래프 설정
plt.figure(figsize=(8, 5))
plt.plot(x_curve, y_curve, label='f(x) = √x', color='blue')

# 심슨 면적 영역 색칠 (각 구간의 근사 다항함수)
for j, (xs, ys) in enumerate(area_patches):
    plt.fill_between(xs, ys, color='orange', edgecolor='black', alpha=0.4,
                     label="Simpson's Approx." if j == 0 else "")

# 그래프 제목, 라벨, 범례 등 설정
plt.title("Numerical Integration using Simpson's Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
