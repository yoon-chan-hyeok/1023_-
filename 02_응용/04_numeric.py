"""04 응용: 결측 대체와 숫자 변환을 짧은 Pipeline으로 연결합니다."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 제공: data/는 입력 자료, outputs/는 실행 결과를 보관합니다. 이 파일의 위치를 기준으로 읽습니다.
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "data" / "requests.csv")
# 제공: 먼저 20%를 test로 보관하고, 남은 80% 중 25%를 valid로 나눕니다.
# random_state는 재현용 고정값입니다. stratify는 성공/실패 비율을 고려합니다.
train_valid, test = train_test_split(
    data, test_size=0.2, random_state=42, stratify=data["failed"])
train, valid = train_test_split(
    train_valid, test_size=0.25, random_state=42, stratify=train_valid["failed"])
# test는 개수 확인 외에 사용하지 않습니다.

numeric_columns = ["input_chars", "allowed_tools"] #numeric_columns는 숫자형 열의 이름을 담은 리스트입니다. 이 리스트에는 "input_chars"와 "allowed_tools"라는 두 개의 열 이름이 포함되어 있습니다. 이 열들은 결측값 대체와 표준화 작업을 수행할 대상이 됩니다.
numeric = Pipeline([("fill", SimpleImputer(strategy="median")),
                    ("scale", StandardScaler())])   ##numeric은 Pipeline 객체로, 결측값 대체와 표준화를 순차적으로 수행하는 파이프라인입니다. Pipeline은 여러 전처리 단계를 연결하여 하나의 객체로 만들 수 있게 해줍니다. 여기서는 두 단계가 포함되어 있습니다. 첫 번째 단계는 "fill"이라는 이름으로 SimpleImputer를 사용하여 결측값을 중앙값(median)으로 대체합니다. 두 번째 단계는 "scale"이라는 이름으로 StandardScaler를 사용하여 데이터를 표준화합니다. 이렇게 하면 train 데이터에서 학습한 결측값 대체와 표준화 정보를 valid 데이터에 적용할 수 있습니다.
train_ready = numeric.fit_transform(train[numeric_columns])
# TODO A04-1: 학습된 numeric으로 valid의 숫자 2열을 변환하세요.
valid_ready = valid[numeric_columns].to_numpy()#to_numpy()는 pandas DataFrame을 numpy 배열로 변환하는 메서드입니다. valid_ready = valid[numeric_columns].to_numpy()는 valid DataFrame에서 numeric_columns에 해당하는 열들을 선택하고, 이를 numpy 배열로 변환하여 valid_ready 변수에 저장합니다. 이렇게 하면 valid 데이터의 숫자형 열들을 train 데이터에서 학습한 결측값 대체와 표준화 정보를 적용할 수 있습니다.

print("중앙값:", numeric["fill"].statistics_.tolist())
print("train/valid 모양:", train_ready.shape, valid_ready.shape)
print("valid 처음 2행:")
print(valid_ready[:2].round(3))
