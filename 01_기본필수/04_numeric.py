"""04 기본필수: 결측이 없는 숫자를 train 기준으로 표준화합니다."""
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 제공: 정상 숫자만 사용합니다. 결측 대체는 선택 단계에서 배웁니다.
train = pd.DataFrame({"input_chars": [100, 200, 300]})
valid = pd.DataFrame({"input_chars": [400, 500]})
scaler = StandardScaler()#StandardScaler는 데이터의 평균을 0, 표준편차를 1로 변환하는 전처리 클래스입니다. 이를 통해 데이터의 스케일을 맞추어 모델 학습에 도움을 줍니다.
scaler.fit(train)#STANDARSCARLER클래스로 만든 SCALER객체의 fit() 메서드는 train 데이터의 평균과 표준편차를 계산하여 학습합니다. 이렇게 학습한 평균과 표준편차는 이후 transform() 메서드에서 사용됩니다.

# transform은 이미 배운 평균과 크기를 사용합니다. 다시 fit하지 않습니다.
# TODO B04-1: scaler의 transform으로 valid를 변환하세요.
valid_ready = valid.transform(train) #transform() 메서드는 fit() 메서드로 학습한 평균과 표준편차를 사용하여 valid 데이터의 값을 변환합니다. 이렇게 하면 valid 데이터의 값이 train 데이터의 평균과 표준편차를 기준으로 표준화됩니다. 따라서 valid 데이터의 값은 train 데이터의 분포에 맞게 조정됩니다.
print("train에서 배운 평균:", scaler.mean_.tolist())
print("valid 변환 결과:")
print(valid_ready.round(3))
