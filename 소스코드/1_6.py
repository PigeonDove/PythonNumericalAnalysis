import numpy as np  # numpy 라이브러리 불러오기
import matplotlib.pyplot as plt  # 시각화를 위한 matplotlib 불러오기

# 원래의 데이터 값 지정
x1, y1 = 10, 20  # 첫 번째 데이터 포인트 (시간, 대기 시간)
x2, y2 = 14, 60  # 두 번째 데이터 포인트 (시간, 대기 시간)

# 보간할 시간 값들 (10.4부터 14.0까지 9개 생성)
x_pred = np.linspace(10.4, 13.6, 9)

# 선형 보간법 공식 적용
y_pred = ((x_pred - x1) / (x2 - x1)) * (y2 - y1) + y1

# 보간 결과 출력
print("Predicted wait times using linear interpolation:")  # 예측 결과 제목 출력
for x, y in zip(x_pred, y_pred):
    print(f"Time: {x:.1f}h, Predicted Wait Time: {y:.2f} min")  # 예측 시간과 대기 시간 출력

# 시각화 시작
plt.figure(figsize=(7, 5))  # 그래프 크기 설정

# 원본 점 플로팅
plt.scatter([x1, x2], [y1, y2], color='blue', label="Original Data Points")  # 실제 데이터 점 표시
plt.plot([x1, x2], [y1, y2], 'k--', label="Interpolation Line")  # 점선을 이용한 선형 연결

# 예측된 보간 점 플로팅
plt.scatter(x_pred, y_pred, color='red', label="Interpolated Values")  # 예측값 점 표시

# 그래프 라벨 설정
plt.xlabel("Time (hour)")  # x축 라벨
plt.ylabel("Wait Time (min)")  # y축 라벨
plt.title("Predicted Wait Time using Linear Interpolation")  # 그래프 제목
plt.grid(True)  # 격자 표시
plt.legend()  # 범례 표시
plt.show()  # 그래프 출력