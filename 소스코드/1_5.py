import numpy as np  # numpy 라이브러리 불러오기
import matplotlib.pyplot as plt  # 시각화를 위한 matplotlib 불러오기

# 원래의 데이터 값 지정
x1, y1 = 10, 20  # 첫 번째 데이터 포인트 (시간, 대기 시간)
x2, y2 = 14, 60  # 두 번째 데이터 포인트 (시간, 대기 시간)

# 보간할 시간: 12시
x_pred = 12

# 선형 보간 공식 적용
y_pred = ((x_pred - x1) / (x2 - x1)) * (y2 - y1) + y1

# 결과 출력
print("Predicted wait time at 12:00 using linear interpolation:")
print(f"Time: {x_pred}h, Predicted Wait Time: {y_pred:.2f} min")

# 시각화
plt.figure(figsize=(7, 5))

# 원본 점 플로팅
plt.scatter([x1, x2], [y1, y2], color='blue', label="Original Data Points")
plt.plot([x1, x2], [y1, y2], 'k--', label="Interpolation Line")

# 예측된 점 플로팅
plt.scatter(x_pred, y_pred, color='red', label="Interpolated at 12:00")
plt.annotate(f"({x_pred}, {y_pred:.1f})", (x_pred, y_pred),
             textcoords="offset points", xytext=(0, 10), ha='center')

# 그래프 라벨 설정
plt.xlabel("Time (hour)")
plt.ylabel("Wait Time (min)")
plt.title("Predicted Wait Time at 12:00 using Linear Interpolation")
plt.grid(True)
plt.legend()
plt.show()
