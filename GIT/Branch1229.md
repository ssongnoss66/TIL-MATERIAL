# 1229 THU

## 😛 branch

- branch : 독립적인 작업흐름을 만들고 관리

### @ 명령어

- 브랜치 생성 *(master) $ git branch {branch name}*

- 브랜치 이동 *(master) $ git checkout {branch name}*

- 브랜치 생성 및 이동 *(master) $ git checkout -b {branch name}*

- 브랜치 목록 *(master) $ git branch*

- 브랜치 삭제 *(master) $ git branch -d {branch name}*

## 😕 Git Flow

- Git을 활용하여 협업하는 흐름

- 브랜치를 활용하는 전략

  ![branch](https://gmlwjd9405.github.io/images/types-of-git-branch/total-branch.png)

  ![gitflow](https://user-images.githubusercontent.com/121418205/209908818-1e02d725-12ca-4ead-9c7f-ff3ed34562b4.jpg)

### @ GitHub Flow 기본 원칙

- master branch는 반드시 배포 가능한 상태

- feature branch는 각 기능의 의도를 알 수 있도록 작성

- Commit message는 명확하게 작성

- Pull Request 통해 협업 진행

- 변경사항 반영하고 싶으면 master branch에 병합

### @ GitHub Flow Models

- Shared Respository Model

- Fork & Pull Model

