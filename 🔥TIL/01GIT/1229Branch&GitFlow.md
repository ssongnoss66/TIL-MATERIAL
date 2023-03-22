# 😛 branch

- branch : 독립적인 작업흐름을 만들고 관리

## @ 브랜치 명령어

- 브랜치 생성 *(master) $ git branch {branch name}*

- 브랜치 이동 *(master) $ git checkout {branch name}*

- 브랜치 생성 및 이동 *(master) $ git checkout -b {branch name}*

- 브랜치 목록 *(master) $ git branch*

- 브랜치 삭제 *(master) $ git branch -d {branch name}*

## MERGE

- 각 branch 작업 이력 합치는 명령어

  - 동일한 파일을 수정한 경우 충돌 발생 ; 직접 해당 파일 확인하고 적절하게 수정한 이후 직접 커밋 실행

  - 다른 파일을 수정한 경우 ; 충돌 없이 자동으로 Merge Commit 생성됨

- merge - fast forward

  - 기존 master 브랜치에 변경사항 없어 단순히 앞으로 이동

    1. feature-a branch로 이동 후 commit

    2. master 별도 변경 없음

    3. master branch로 병합

- merge - merge commit

  - 기존 master 브랜치에 변경사항 있어 병합 커밋 발생

    1. feature-a branch로 이동 후 commit

    2. master branch commit

    3. master branch로 병합

# 😕 Git Flow

- Git을 활용하여 협업하는 흐름

- 브랜치를 활용하는 전략

  ![branch](https://gmlwjd9405.github.io/images/types-of-git-branch/total-branch.png)

  ![gitflow](https://user-images.githubusercontent.com/121418205/209908818-1e02d725-12ca-4ead-9c7f-ff3ed34562b4.jpg)

## @ GitHub Flow 기본 원칙

- master branch는 반드시 배포 가능한 상태

- feature branch는 각 기능의 의도를 알 수 있도록 작성

- Commit message는 명확하게 작성

- Pull Request 통해 협업 진행

- 변경사항 반영하고 싶으면 master branch에 병합

## @ GitHub Flow Model에 따른 작업 순서

- Shared Repository Model (갑 = respository owner / project manager 을 = collaborator)

  > 동일한 저장소를 공유하여 활용

  1. 팀원 초대 및 저장소 Clone

    - step 0-1. Invite collaborator
    
      - 갑이 을 초대
      
      - collaborator에 등록되어야 해당 저장소에 대한 push 권한 생김

    - step 0-2. Accept Invitation

      - (을) 이메일 통해 초대 수락

      - 해당 저장소 주소 뒤에 /invitation 붙이는 것도 가능

    - step 0-3. Clone project(remote) repository

      - (을) Clone 이후 작업 환경 설정 마무리

  2. 브랜치에서 작업 및 GitHub Push

    - Step 1. Feature branch 생성 및 작업

      - (을) 항상 독립적인 feature branch에서 작업

      - master branch는 배포 가능한 상태를 유지

      - feature branch는 기능 개발 (이름 생성 시 기능을 명시)

    - Step 2-1. Commit

      - (을) Commit으로 작업의 이력을 남긴다

      - 코드 변화에 맞춰 실시 (**단순 중간 저장 X**)

    - Step 2-2. Push to remote repository

      - (을) 완성된 코드는 원격 저장소에 push

      - 원격 저장소에 공개된 이력은 **절대 변경 금지**

  3. Pull Request 생성

    - step 3-1. Open a Pull Request

      - (을) 깃헙에 들어가서 Pull Request

    - step 3-2. Create Pull Request

      - (을) PR 설정 진행 후 요청 생성

  4. Review 및 Merge

    - step 4. Merge pull request

      - (갑) 작성된 코드 확인 후 병합
      
      - 코드 리뷰 진행 후 관리자 판단 하에 병합

      - 병합 과정에서 충돌 발생 시 해결 후 병합

      - master branch로 병합할 때는 코드가 배포 가능한 상태여야 한다

  5. 병합 완료 후 개발을 한다면?

    - (을) 로컬 저장소에서는 merge된 branch 삭제하고 master branch를 업데이트 이후 1. ~ 3. 과정 반복

- Fork & Pull Model

  > Repository > Collaborator에 등록되지 않은 상태에서 진행 (깃헙 기반 오픈소스 참여시)

  1. Fork & Clone

    - step 0-1. Fork repository

      - (을) Forking project repository

      - 원격 저장소를 fork
    
      - 내 저장소로 복제본 가져옴으로써 로컬 작업 후 원격 저장소로 push할 수 있게 됨

    - step 0-2. Clone project(remote) repository

      - (을) Clone 후 작업 환경 설정 마무리

      - **Clone시 반드시 본인 저장소인지 확인**

  2. ~ 4.는 Shared Repository Model과 동일

  5. 병합 완료 후 개발을 한다면?

    - (을) 로컬 저장소에서는 merge된 branch 삭제하고 master branch를 업데이트

    - master branch는 원본 저장소를 받아와야 하며 별도의 원격 저장소를 추가하여 진행 가능 
    
        (GitHub에서 fetch upstream도 가능)