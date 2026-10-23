"""01 기본필수: CSV에서 입력과 정답을 각각 꺼냅니다."""
from pathlib import Path
import pandas as pd

# 제공: 이 Python 파일과 같은 폴더에 있는 CSV를 읽습니다. 작업 폴더를 바꾸어도 됩니다.
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "requests.csv")
#path file은 현재 파일의 경로를 나타내고, resolve()는 절대 경로로 변환하며, parent는 해당 파일이 속한 디렉토리를 반환합니다. 따라서 HERE는 현재 스크립트 파일이 위치한 디렉토리의 절대 경로를 나타냅니다.
#즉 현재 위치의 절대 경로를 하나 만들고 그다음에 requests.csv를 읽어서 data에 넣습니다.

# X는 예측 전에 알 수 있는 정보입니다. ID와 정답은 입력에 넣지 않습니다.
# TODO B01-1: 입력 열을 input_chars와 task_type 두 개로 바꾸세요.
X = data[["input_chars", "task_type"]]  # TODO B01-1: 입력 열을 input_chars와 task_type 두 개로 바꾸세요.
#X = data["input_chars", "task_type"]  # TODO B01-1: 입력 열을 input_chars와 task_type 두 개로 바꾸세요.

# TODO B01-2: 정답 열 failed를 선택하세요. 0은 성공, 1은 실패입니다.
y = data["failed"]  # TODO B01-2: 정답 열 failed를 선택하세요. 0은 성공, 1은 실패입니다.

#y = data["input_chars"]

print("입력 열:", X.columns.tolist())# x의 열 이름을 리스트로 바꿔서 출력합니다.
print("X 모양:", X.shape)
print("y 모양:", y.shape)
print("처음 3개 정답:", y.head(3).tolist())
