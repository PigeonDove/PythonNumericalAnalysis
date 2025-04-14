import numpy as np  # numpy 라이브러리를 불러와 수학 연산 (sqrt 등) 을 사용할 수 있게 함

# 실제 sqrt(2)의 값 (numpy의 sqrt 함수 사용)
actual_value = np.sqrt(2)

# 이분법을 위한 초기 범위 설정: 1부터 2 사이에서 sqrt(2)를 찾기 위해 low와 high 값 설정
low = 1.0
high = 2.0

# 오차 허용 범위 설정 (정확히 f(x)=0이 아니더라도 이만큼 작으면 만족)
tolerance = 0.01

# 함수 정의: f(x) = x^2 - 2, 이 함수의 근을 찾는 것이 목적 (즉, f(x) = 0이 되는 x)
def f(x):
    return x**2 - 2

# 반복 횟수를 저장할 변수 초기화
step = 0

# 이분법 시작 (조건을 만족할 때까지 무한 반복)
while True:
    mid = (low + high) / 2  # 현재 범위의 중간값을 계산
    step += 1  # 반복 횟수를 1 증가

    if abs(f(mid)) < tolerance:  # f(mid)의 절댓값이 오차 허용 범위보다 작으면 반복 종료
        break

    if f(low) * f(mid) < 0:  # 근이 low와 mid 사이에 있으면
        low = low            # low는 그대로 유지
        high = mid           # high를 mid로 옮김
    else:                    # 근이 mid와 high 사이에 있으면
        low = mid            # low를 mid로 옮김
        high = high          # high는 그대로 유지
# 반복이 끝난 후 결과 출력
print(f"Actual sqrt(2) Value: {actual_value:.6f}")          # 실제 sqrt(2) 값을 소수점 6자리까지 출력
print(f"Bisection sqrt(2) Value: {mid:.6f}")                # 이분법으로 계산한 결과 출력
print(f"Steps Taken: {step}")                               # 반복 횟수 출력
