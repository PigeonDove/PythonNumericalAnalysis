import numpy as np  # numpy 라이브러리를 불러와 수학 연산 (sqrt 등) 을 사용할 수 있게 함

# 실제 sqrt(2)의 값 (numpy의 sqrt 함수 사용)
actual_value = np.sqrt(2)

# 백분율 허용 범위 설정
percent_tolerance = 0.0001

# 함수 정의: f(x) = x^2 - 2, 이 함수의 근을 찾는 것이 목적
def f(x):
    return x**2 - 2

# 도함수 정의: f'(x) = 2x
def df(x):
    return 2 * x

# 초기 추정값 설정 (대략적으로 루트2와 가까운 값이면 더 빠르게 수렴)
x = 2

# 반복 횟수를 저장할 변수 초기화
step = 0

# 뉴턴-랩슨법 시작 (조건을 만족할 때까지 무한 반복)
while True:
    fx = f(x)           # 현재 x에서의 함수값 계산
    dfx = df(x)         # 현재 x에서의 도함수값 계산
    step += 1           # 반복 횟수를 1 증가

    next_x = x - fx / dfx  # 뉴턴-랩슨 공식 적용: x_{n+1} = x_n - f(x_n)/f'(x_n)

    relative_error = abs((actual_value - next_x) / actual_value) * 100

    if relative_error < percent_tolerance:  # 오차가 percent_tolerance보다 작으면 반복 종료
        break

    x = next_x  # 다음 반복을 위해 x 업데이트

relative_error = abs((actual_value - next_x) / actual_value) * 100

# 반복이 끝난 후 결과 출력
print(f"Actual sqrt(2) Value: {actual_value:.6f}")          # 실제 sqrt(2) 값을 소수점 6자리까지 출력
print(f"Newton-Raphson sqrt(2) Value: {next_x:.6f}")        # 뉴턴-랩슨법으로 계산한 결과 출력
print(f"Steps Taken: {step}")                               # 반복 횟수 출력
print("Relative Error: {:.10f}%".format(relative_error))     # 상대오차 출력
