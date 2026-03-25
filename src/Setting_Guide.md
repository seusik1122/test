

## 자, 다들 빅데이터 분석 프로젝트 들으니 이미 해본겁니다.  


1. Python `3.11.9` 설치하기 (파이썬 공식 홈페이지에서 다운로드하여 설치합니다)    
[매우 중요] 설치 파일 실행 시, 첫 화면 맨 아래에 있는 `Add Python.exe to PATH` 체크박스를 무조건!! 체크하고 설치를 진행해 주세요. (체크 안 하면 나중에 명령어 실행이 안 됩니다.)  
<br><br>


2. VSCode에서 프로젝트 열기  
VSCode에서 `CAPSTONE_TEAM_PROJECT` 리포지토리 폴더를 엽니다.  
상단 메뉴의 [ 터미널 ] - [ 새 터미널 ]을 엽니다.
<br><br>


3. 가상환경(venv) 생성하기  
터미널에 `python -m venv venv`를 입력하고 엔터를 칩니다. (잠시 기다리면 venv라는 폴더가 생성됩니다.)  
<br><br>


4. 가상환경 실행(활성화)하기  
터미널에 `venv\Scripts\activate`를 입력하여 가상환경을 켭니다.<br>  
🚨 만약 빨간 글씨로 '보안 오류(스크립트를 실행할 수 없음)'가 뜬다면?  
당황하지 말고 터미널에 아래 명령어를 복사+붙여넣기  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`  
(이후 다시 venv\Scripts\activate 입력)  
(맥(Mac) 사용자의 경우: `source venv/bin/activate` 입력)
<br><br>


5. 필수 패키지 다운로드
터미널 입력창 맨 앞에 초록색으로 (venv) 가 떴는지 확인합니다! (이게 떠 있어야 가상환경에 성공적으로 들어온 것입니다.)
가상환경에 들어왔다면, `python -m pip install -r requirements.txt`를 입력해 프로젝트에 필요한 모든 패키지를 한 번에 설치합니다.
<br><br>


6. 테스트 파일 실행해보기  
터미널에 `python src/test/basic_print.py`로 실행해보기.
<br><br>