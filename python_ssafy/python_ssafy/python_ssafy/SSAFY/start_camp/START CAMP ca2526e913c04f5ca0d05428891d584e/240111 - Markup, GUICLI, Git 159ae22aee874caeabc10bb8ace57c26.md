# 240111 - Markup, GUICLI, Git

[https://abit.ly/pb-document](https://abit.ly/pb-document) 

### Markdown - 마크업 언어

[README.md](240111%20-%20Markup,%20GUICLI,%20Git%20159ae22aee874caeabc10bb8ace57c26/README.md)

- GUI/CLI

GUI의 장점 : 가독성, 기능성, “graph”, ‘diff 파일’, ‘CLI에서 하기 힘든 복잡한 활동, 분석에 편함’

CLI의 장점 : commit, push 등의 명령이 굉장히 빠름, 변화폭이 거의 없음.

→ 대부분 CLI를 사용하지만, graph나 diff의 경우에 GUI 사용

→ CLI에서 가장 중요한 것 : “경로”

### Git bash

- SSAFY@2▒▒PC178 MINGW64 ~/Desktop/Markdown
- MINGW64 : 윈도우에서 리눅스의 툴을 쓸 수 있게 해주는 프로젝트
- ~ : home directory [cd ~ : home] [cd - : 뒤로가기] [cd .. : 상위폴더]
- touch 파일명.확장자 : 파일 생성
- mkdir 폴더명 : 폴더 생성
- ls : 현재 경로의 모든 파일,폴더 찾아줌
- start : 파일 실행
- rm : 파일 삭제
- rm -r : 폴더 삭제
- Ctrl + Shift +c : 터미널에서 복사
- Shift + Insert : 터미널에 붙여넣기 (ctrl v 아님)
- Ctrl + c : 터미널 강제 종료
- Ctrl + L : 터미널 clean

### Github

- 버전관리
- History
- branch : 코드를 개발하거나 수정하는 데에 사용되는 작업 공간
- HEAD → MASTER = ‘현재 작업중인 커밋은 Master’ 라는 뜻

![Untitled](240111%20-%20Markup,%20GUICLI,%20Git%20159ae22aee874caeabc10bb8ace57c26/Untitled.png)

1. git 시작
- git init
1. commit 작성자 설정
- git config —global [user.name](http://user.name) JJuHS
- git config —global [user.email](http://user.email) ghtjd006098@gmail.com
- git config —global -l
1. add
- git add .
- git status
1. commit
- git commit -m “MESSAGE”
- git log
- git log후 branch가 이상한 경우 변경
    - git checkout master
1. remote
- git remote add origin https://github.com/JJuHS/SSAFY.git
- git remote -v
1. push
- git push -u origin master
1. 파일 내부가 변경된 경우
- git push origin master
1. 파일 위치에 변경이 있는경우
- git add .
- git commit -m “MESSAGE”
- git push origin master
1. 특정파일만 추가하려는 경우
- git add d.txt
- git commit -m “MESSAGE”
- git push origin master

### 

### Git pull

- 원격 저장소의 변경사항을 로컬에 적용하려는 경우
- git pull origin master

### Git clone

- 원격 저장소를 복제하려는 경우
- git clone [repository_url]

### Git branch

- 새로운 브랜치를 만들거나 기존의 브랜치를 확인하려는 경우
- git branch [branch_name] : 새로운 브랜치 생성
- git branch : 현재 브랜치 확인

### Git checkout

- 다른 브랜치로 이동하려는 경우
- git checkout [branch_name]

### Git merge

- 다른 브랜치의 변경사항을 현재 브랜치에 적용하려는 경우
- git merge [branch_name]

### Git stash

- 작업 중인 변경사항을 임시로 저장하려는 경우
- git stash

### Git fetch

- 원격 저장소의 최신 변경사항을 확인하려는 경우
- git fetch

### Git clone

- 원격 저장소의 전체 프로젝트를 복사하려는 경우
- git clone [repository_url]

### README.md

manual of project