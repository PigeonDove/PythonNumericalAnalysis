import numpy as np  # numpy 라이브러리를 불러와 수학 연산 (sqrt 등) 을 사용할 수 있게 함

# 실제 sqrt(2)의 값 (numpy의 sqrt 함수 사용)
actual_value = np.sqrt(2)

# 백분율 허용 범위 설정
percent_tolerance = 0.0001

# 함수 정의: f(x) = x^2 - 2, 이 함수의 근을 찾는 것이 목적
def f(x):
    return x**2 - 2

# 초기 두 추정값 설정
x0 = 2.1
x1 = 2.0

# 반복 횟수를 저장할 변수 초기화
step = 0

# Secant Method 시작
while True:
    fx0 = f(x0)
    fx1 = f(x1)
    step += 1  # 반복 횟수를 1 증가

    # Secant Method 공식 적용
    next_x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

    # 상대오차 계산
    relative_error = abs((actual_value - next_x) / actual_value) * 100

    if relative_error < percent_tolerance:  # 오차가 허용범위보다 작으면 종료
        break

    # 다음 반복을 위해 값 업데이트
    x0, x1 = x1, next_x

# 반복이 끝난 후 결과 출력
print(f"Actual sqrt(2) Value: {actual_value:.6f}")            # 실제 sqrt(2) 출력
print(f"Secant Method sqrt(2) Value: {next_x:.6f}")           # 계산된 sqrt(2) 출력
print(f"Steps Taken: {step}")                                 # 반복 횟수 출력
print("Relative Error: {:.10f}%".format(relative_error))      # 상대오차 출력
    