import numpy as np              # 수학 연산을 위한 numpy 모듈 불러오기
import matplotlib.pyplot as plt # 시각화를 위한 matplotlib 모듈 불러오기

# 함수 정의: 적분할 대상 함수 f(x) = √x
def f(x):
    return np.sqrt(x)

# 적분 구간 설정
first, last = 0, 4              # 구간 [0, 4]
step = 1                        # 간격 (사다리꼴 밑변의 길이)

# 시작 위치 초기화
i = first                       # 반복문 시작 위치
areas = 0                       # 넓이 총합 초기값

# 그래프를 위한 리스트 초기화
x_vals_trap = []               # 사다리꼴의 좌측 점 저장
y_vals_trap = []               # 각 점에서의 함수값 저장

# 시작 구간 ~ 마지막 구간까지 반복
while i < last:
    x0 = i                                      # 구간 시작점
    x1 = i + step                               # 구간 끝점
    y0 = f(x0)                                  # f(x0)
    y1 = f(x1)                                  # f(x1)
    area = ( (step) * (y0 + y1) ) / 2           # 사다리꼴 넓이 공식 적용
    areas += area                               # 넓이 누적
    print(f"[{x0:.2f}, {x1:.2f}] , heights = ({y0:.4f}, {y1:.4f}) , area = {area:.4f}") # 출력

    x_vals_trap.append(x0)                      # 시작점 저장
    y_vals_trap.append(y0)                      # 시작점의 y값 저장

    i += step                                   # 다음 구간으로 이동

# 마지막 점 추가 (사다리꼴 끝점)
x_vals_trap.append(last)                        # 마지막 x값
y_vals_trap.append(f(last))                     # 마지막 y값

# 실제 적분값 계산: ∫₀⁴ √x dx = (2/3) * 4^(3/2) = (2/3) * 8 = 16/3
actual = (2/3) * last**(3/2)                     # 정확한 적분값
error = abs(actual - areas) / actual * 100       # 상대 오차 계산 (%)

# 결과 출력
print(f"Trapezoidal Rule Approximation: {areas:.4f}") # 사다리꼴법 적분 근사값 출력
print(f"Actual Value: {actual:.4f}")                  # 실제 적분값 출력
print(f"Relative Error: {error:.2f}%")                # 상대 오차 출력

# ----------------- 그래프 시각화 -------------------

# 부드러운 곡선을 위한 x값 생성
x_curve = np.linspace(first, last, 400)           # 곡선 그리기용 x값
y_curve = f(x_curve)                              # 곡선 y값

# 그래프 설정
plt.figure(figsize=(8, 5))                        # 그래프 크기 설정
plt.plot(x_curve, y_curve, label='f(x) = √x', color='blue') # 원래 함수 곡선

# 사다리꼴 그래프 그리기
for j in range(len(x_vals_trap) - 1):
    xs = [x_vals_trap[j], x_vals_trap[j], x_vals_trap[j+1], x_vals_trap[j+1]]
    ys = [0, y_vals_trap[j], f(x_vals_trap[j+1]), 0]
    plt.fill(xs, ys, 'orange', edgecolor='black', alpha=0.4,
             label='Trapezoids' if j == 0 else "") # 첫 구간만 범례 표시

# 그래프 제목, 라벨, 범례 등 설정
plt.title('Numerical Integration using Trapezoidal Rule')    # 그래프 제목
plt.xlabel('x')                                              # x축 라벨
plt.ylabel('f(x)')                                           # y축 라벨
plt.legend()                                                 # 범례 표시
plt.grid(True, linestyle='--', alpha=0.5)                    # 그리드 표시
plt.tight_layout()                                           # 레이아웃 정리
plt.show()                                                   # 그래프 출력
