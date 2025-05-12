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

# 그래프를 위한 리스트 초기화
midpoints = []                 # 직사각형 중간점 저장 리스트
heights = []                   # 각 중간점에서의 함수값 저장 리스트

# 시작 구간 ~ 마지막 구간까지 반복
while i < last :
    width = step                                  # 직사각형의 가로 길이
    mid = (i + (i + step)) / 2                    # 중간값 계산
    height = f(mid)                               # 함수 f에서의 높이값 계산
    area = width * height                         # 넓이 계산
    areas += area                                 # 총 넓이에 누적
    print(f"{mid:.2f} , {height:.4f} , {area:.4f}") # 각 단계별 정보 출력

    midpoints.append(mid)                         # 그래프를 위한 중간점 좌표 저장
    heights.append(height)                        # 그래프를 위한 높이 저장

    i += step                                     # 다음 구간으로 이동

# 실제 적분값 계산: ∫₀⁴ √x dx = (2/3) * 4^(3/2) = (2/3) * 8 = 16/3
actual = (2/3) * last**(3/2)                       # 정확한 적분값
error = abs(actual - areas) / actual * 100         # 상대 오차 계산 (%)

# 결과 출력
print(f"Midpoint Rule Approximation: {areas:.4f}") # 직사각형법 적분 근사값 출력
print(f"Actual Value: {actual:.4f}")               # 실제 적분값 출력
print(f"Relative Error: {error:.2f}%")             # 상대 오차 출력

# ----------------- 그래프 시각화 -------------------

# x값 생성: 부드러운 곡선을 위한 400개 점 생성
x_vals = np.linspace(first, last, 400)            # 곡선 그리기용 x값
y_vals = f(x_vals)                                # 곡선 f(x) = √x의 y값

# 그래프 설정
plt.figure(figsize=(8, 5))                        # 그래프 크기 설정
plt.plot(x_vals, y_vals, label='f(x) = √x', color='blue') # 원래 함수 곡선 그리기

# 직사각형 하나씩 그리기
for j in range(len(midpoints)):
    plt.bar(midpoints[j], heights[j], width=step, alpha=0.4,
            align='center', color='orange', edgecolor='black',
            label='Midpoint Rectangles' if j == 0 else "")  # 첫 직사각형만 범례 표시

# 그래프 제목, 라벨, 범례 등 설정
plt.title('Numerical Integration using Midpoint Rule')      # 그래프 제목
plt.xlabel('x')                                              # x축 라벨
plt.ylabel('f(x)')                                           # y축 라벨
plt.legend()                                                 # 범례 표시
plt.grid(True, linestyle='--', alpha=0.5)                    # 그리드 표시
plt.tight_layout()                                           # 레이아웃 정리
plt.show()                                                   # 그래프 출력
