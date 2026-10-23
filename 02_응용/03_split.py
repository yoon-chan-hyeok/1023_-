"""03 응용: 전체 표를 함께 나누면 입력과 정답이 따로 섞이지 않습니다."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

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

print("분할:", len(train), len(valid), len(test))
# TODO A03-1: valid의 정답 개수를 세도록 자료를 바꾸세요.
valid_counts = valid["failed"].value_counts().sort_index()#value_counts()는 pandas Series에서 각 고유값의 개수를 세는 메서드입니다. sort_index()는 인덱스를 기준으로 정렬하는 메서드입니다. valid["failed"].value_counts().sort_index()는 valid DataFrame의 "failed" 열에서 각 고유값(0과 1)의 개수를 세고, 그 결과를 인덱스 순서대로 정렬하여 valid_counts 변수에 저장합니다. 이렇게 하면 valid 데이터에서 성공과 실패의 개수를 쉽게 확인할 수 있습니다.
print("valid 정답 개수:", valid_counts.to_dict())#to_dict()는 pandas Series를 딕셔너리로 변환하는 메서드입니다. valid_counts.to_dict()는 valid_counts Series를 딕셔너리로 변환하여 출력합니다. 이렇게 하면 valid 데이터에서 성공과 실패의 개수를 딕셔너리 형태로 확인할 수 있습니다.
print("seed: 42 / 42")
