# 😎 **CLI**

## @ CLI ( Command Line Interface )

  - **명령**을 해야 결과가 도출됨

  - 프롬프트 기본 인터페이스 ; 컴퓨터 정보 / 디렉토리 / $

  - 명령어 기본 구조 ; 특정 프로그램을 어떠한 인자와 함께 호출하도록 명령



## @ CLI와 GUI

> 그래픽 기반 인터페이스인 **GUI**  명령 기반 인터페이스인 **CLI**



## @ 디렉토리 관리

  - **pwd** : 현재 디렉토리 출력

  - **cd 디렉토리이름** : 디렉토리 이동

  - **cd ..** : 상위 디렉토리로 이동

  - **ls** : 목록

  - **mkdir** : 디렉토리 생성

  - **touch** : 파일 생성

  - **rm 파일명** : 파일 삭제

  - **rm -r 폴더명** : 폴더 삭제



# 😎 **GIT**

> GIT을 활용하여 파일을 버전별로 관리!

## @ 분산버전관리시스템 (DVCS)

  - 원격 저장소 통해 협업

  - 모든 히스토리를 클라이언트들이 공유

  - 로컬에서도 버전을 기록하고 관리한다

## @ 명령어

  - **git init** : 특정 폴더를 git 저장소로 만들어 git으로 관리 ( *.git 폴더가 생성되고 git bash에는 (master)라는 표기 생김* )
  
  - **git add <파일명>** : working directory 상의 내용을 staging area에 추가 ( *untracked -> staged / modified -> staged* )

  - **git commit -m '<커밋메시지>'** : staged 상태의 파일들을 커밋을 통해 **버전**으로 기록 
    > 커밋메시지는 명확하게!

  - **git log** : 현재 저장소에 기록된 커밋을 조회

    - git log -1 : 최근 한 개
    
    - git log --oneline : 한줄로
    
    - git log -2 --oneline : 최근 두 개를 한줄로

  - **git status** : git 저장소에 있는 파일의 상태 확인

    - untracked files : 버전으로 관리된 적 없음 *(Next Step : add하여 staging area로)*

    - changes not staged for commit : add 했던 파일을 수정한 상태 *(Next Step : add 하여 staging area로 보내거나 commit 하여 버전에 반영)*

    - changes to be committed : add 된 상태 *(Next Step : commit하여 버전에 반영)*

    - nothing to commit, working tree clean : working directory가 비어있음