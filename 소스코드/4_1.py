import numpy as np                         # 수치 계산을 위한 numpy 모듈 불러오기
import matplotlib.pyplot as plt            # 시각화를 위한 matplotlib 모듈 불러오기

# 함수 정의: f(x) = x^2
def f(x):
    return x**2

# 전진 차분법 공식: f'(x) ≈ (f(x+h) - f(x)) / h
def forward_diff(x, h):
    return (f(x + h) - f(x)) / h

# x 값들을 linspace로 생성 (1부터 4까지 4개 값)
x_values = np.linspace(1, 4, 4)
h = 0.01                                   # 전진 차분용 아주 작은 h 값

# 전진 차분 근사값과 실제 도함수 값을 저장할 리스트
approx_deriv = []                          # 전진 차분 근사값 저장 리스트
actual_deriv = []                          # 실제 도함수값 저장 리스트 (f'(x) = 2x)

# 각 x에서 도함수 계산
for x in x_values:
    df_approx = forward_diff(x, h)         # 전진 차분 근사값 계산
    df_actual = 2 * x                      # 실제 도함수값 계산
    approx_deriv.append(df_approx)
    actual_deriv.append(df_actual)

    # 결과 출력
    print(f"x = {x:.2f} | Exact f'(x) = {df_actual:.5f} | Approx. f'(x) = {df_approx:.5f} | Error = {abs(df_approx - df_actual):.5f}")

# ----------------- 시각화 -------------------
plt.figure(figsize=(8, 5))                 # 그래프 크기 설정
plt.plot(x_values, actual_deriv, label="Exact Derivative: f'(x) = 2x", color="blue", linewidth=2)         # 실제 도함수 그래프
plt.plot(x_values, approx_deriv, label="Forward Difference Approximation", color="orange", linestyle="--", marker='o') # 전진 차분 근사값 그래프

# 그래프 정보 설정
plt.title("Numerical Derivative of f(x) = x² using Forward Difference")  # 그래프 제목
plt.xlabel("x")                                                           # x축 레이블
plt.ylabel("f'(x)")                                                       # y축 레이블
plt.grid(True, linestyle='--', alpha=0.5)                                 # 격자선 표시
plt.legend()                                                              # 범례 표시
plt.tight_layout()                                                        # 레이아웃 자동 조정
plt.show()                                                                # 그래프 출력
