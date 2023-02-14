# MySQL

## 설치와 실행 ; brew를 활용하여 패키지 설치하고 실행하기!

- 홈브류 ; 맥용 패키지 관리 애플리케이션

  ```
  brew install mysql
  
  mysql --version
  # (출력) mysql  Ver 8.0.32 for macos13.0 on arm64 (Homebrew)

  mysql.server start
  # (출력) Starting MySQL
  # (출력) . SUCCESS!
  ```

## 보안 설정

- 홈브류는 간편하지만 *커뮤니티 기반으로 운영된다*

  ```
  mysql_secure_installation

  # 비밀번호 복잡성 유무
  # 비밀번호 설정
  # 사용자 설정 ; 사용자 옵션 사용 여부 확인
  # 원격 접속 설정 ; 다른 IP에서 root로 접속 활성화 여부
  # test 데이터베이스 설정 ; Test용 DB
  # 권한 적용 여부 설정 ; 권한 변경 시 테이블에 적용 (DB 서버의 권한을 테이블에도 적용?)
  ```

## Workbench 활용 MySQL 접속 방법

- 로컬에서 실행 중인 MySQL 서버 사용하는 경우

  - hostname ; localhost

  - 기본 포트 3306

## 실습 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법

- 실습용 DB 파일 다운로드 후 import

- 파일명 더블클릭하여 선택 후 Query Editor 클릭

- 입력 후 (번개) 눌러서 쿼리 실행 후 출력 확인