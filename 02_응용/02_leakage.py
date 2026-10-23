"""02 응용: 결측 평균 대체를 train에서만 학습합니다."""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# NaN은 결측 개념을 배우기 위해 의도적으로 넣은 빈 값입니다.
train = pd.DataFrame({"value": [10, 20, np.nan]})
valid = pd.DataFrame({"value": [100, np.nan]})
imputer = SimpleImputer(strategy="mean")#imputer는 결측값을 대체하는 클래스입니다. strategy="mean"은 평균으로 대체하겠다는 의미입니다.mean 은 기존에 설정된 결측값 대체 전략 중 하나로, 결측값을 해당 열의 평균으로 대체합니다. 즉, train 데이터에서 결측값이 있는 경우, train 데이터의 나머지 값들의 평균을 계산하여 결측값을 대체합니다.
imputer.fit(train)#fit() 메서드는 train 데이터에서 결측값을 대체할 평균을 계산합니다. 이때 train 데이터의 결측값은 무시하고, 나머지 값들의 평균을 계산합니다. vaild = pd.DataFrame({"value": [100, np.nan]})#valid 데이터는 train 데이터에서 학습한 평균을 사용하여 결측값을 대체합니다. 따라서 valid 데이터의 결측값은 train 데이터의 평균으로 대체됩니다.
# TODO A02-1: imputer.transform(valid)로 train의 평균을 적용하세요.
valid_ready = valid.to_numpy() #to_numpy()는 pandas DataFrame을 numpy 배열로 변환하는 메서드입니다. valid_ready = valid.to_numpy()는 valid DataFrame을 numpy 배열로 변환하여 valid_ready 변수에 저장합니다. 이렇게 하면 valid 데이터의 결측값을 train 데이터에서 학습한 평균으로 대체할 수 있습니다. 만약 안하면 valid 데이터의 결측값은 그대로 남아있게 됩니다. 따라서 valid 데이터의 결측값을 train 데이터에서 학습한 평균으로 대체하기 위해서는 imputer.transform(valid) 메서드를 사용해야 합니다.
valid_noNAN = imputer.transform(valid_ready) #imputer.transform(valid)는 train 데이터에서 학습한 평균을 valid 데이터에 적용하여 결측값을 대체합니다. transform() 메서드는 fit() 메서드로 학습한 평균을 사용하여 valid 데이터의 결측값을 대체합니다. 따라서 valid 데이터의 결측값은 train 데이터에서 학습한 평균으로 대체됩니다.
#imputer.fit(valid_ready) #
print("train에서 배운 값:", imputer.statistics_.tolist())
print("valid 변환:", valid_noNAN.tolist())
print("valid에서 fit 또는 fit_transform을 다시 호출하지 않습니다.")
