# practiceChatBot

[ 개발 환경 구성 가이드 ]

1. 사용 툴 & 소프트웨어
1.1) IDE: VS Code
1.2) Intepreter: Python 3.11  (* 주의사항: 3.12에서는 openai 지원이 안되므로 3.11 버전 사용)
1.3) VS Code 사용 플러그인
1.3.a. Korean Language Pack for Visual Studio Code: VS Code 한글 메뉴 지원 플러그인
1.3.b. Python: 파이썬 사용을 위한 플러그인
1.3.c. Git Graph: 깃 관련 플러그인
1.3.d. PowerShell: 가상환경 접속이 잘 안될 때 사용
1.3.e. open in browser 왜 설치 했을까요...^^;
1.3.f. BackendFuction 음...이것도 잘...

2. Git 구성 & 가상환경 생성
2.1) 깃 로그인하여 Repository 생성 (Public, Readme 선택)
2.2) 깃 클라이언트 설치 (https://git-scm.com)
2.3) PC에서 DOS Command 창 실행하여 Repository 연동할 디렉토리로 이동
2.4) 다음 명령어 입력하여 실행

git clone https://github.com/swcodedu/practiceChatBot

2.5) 다음 명령어 입력하여 가상환경 생성

python -m venv venv

3. 가상환경 실행 & 필요한 라이브러리 설치
3.1) VS Code 실행
3.2) "파일 > 폴더열기" 통해 깃에서 복사한 프로젝트 폴더 오픈
3.3) VS Code 상단 메뉴에서 "..." 클릭하여 터미널 > 새 터미널

실행하면 가상환경으로 들어가는 것이 정상
"(venv) PS 프로젝트 디렉토리" 형태로 나와야 하며, 나오지 않는 경우 인터넷 검색하여 해결 바람

3.4) 라이브러리는 install.txt 파일에 모두 있으므로 다음 명령어를 실행하여 일괄 설치

* 주의: 반드시 가상환경 내에서 실행하여 설치해야 함

pip install -r requirements.txt

4. 환경파일 구성
4.1) 프로젝트 폴더에 .env 파일 생성
4.2) .env 파일에 Open API Key 입력 (다음 두 줄을 값과 함께 입력)

OPENAI_API_KEY=
ORGANIZATION=

4.3) .gitegnore 파일이 있는지 확인 (여러가지 내용들이 들어 있음, 원작자에게서 copy 해옴)

----------------------------------------------------------------------------------------
여기까지 했으면 잘 된것임. 이제 작업 하시면 됩니다 ^^
----------------------------------------------------------------------------------------

99. Trouble Shooting

종종 가상환경 실행하는 Activates 파일 실행시 시큐리티 오류가 나고는 합니다.
인터넷에 많이 있기는 한데요, 제가 해결한 방법을 설명드릴게요.

99.1) VS Code Plugin 중에서 PowerShell Extention 설치
이 플러그인을 설치하면 자동으로 venv 환경으로 접속됨

99.2) 윈도우 파워셀에서 변경
99.2.a. 윈도우 PowerShell 을 관리자 권한으로 실행
99.2.b 다음 명령어를 차례대로 실행 (선택 옵션 A)

Set-ExecutionPolicy Unrestricted -Scope Process
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

* 어떤 의미인지는 저도 잘 몰라요, 이렇게 해결하라고 해서 해보니까 됐어요 ^^;