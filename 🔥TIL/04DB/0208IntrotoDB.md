# 0208 WED

## ๐ซ  Intro

### @ Why Database

- ๋ฐ์ดํฐ

  - ์ ์ฅ์ด๋ ์ฒ๋ฆฌ์ ํจ์จ์ ์ธ ํํ๋ก ๋ณํ๋ ์ ๋ณด(information)

  - ์ ์ธ๊ณ์ ์ผ๋ก ๋ฐ์ดํฐ๋์ด ์ฆ๊ฐํ๋ฉฐ ๋ฐ์ดํฐ ์ผํฐ ์ญ์ ์ฑ์ฅ

  > ๋ฌดํํ ์ฆ๊ฐํ๊ณ  ์๋ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๊ณ  ์ ๊ด๋ฆฌํ์ฌ ํ์ฉํ  ์ ์๋ ๊ธฐ์ ์ด ํ์ํ๋ค!

- ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ์

  - ๊ณผ๊ฑฐ์๋ ํ์ผ(์ด๋์์๋ ์ฝ๊ฒ ์ฌ์ฉ ๊ฐ๋ฅ but ๋ฐ์ดํฐ ๊ตฌ์กฐ์  ๊ด๋ฆฌ ์ด๋ ค์)์ด๋ ์คํ๋ ๋ ์ํธ(์ด๊ณผ ํ์ผ๋ก ๋ฐ์ดํฐ ๊ตฌ์กฐ์  ๊ด๋ฆฌ ๊ฐ๋ฅ but ๋ฐ์ดํฐ๊ฐ ๋ฐฉ๋ํ๋ค๋ฉด?) ์ด์ฉํ์ฌ ๋ฐ์ดํฐ ๊ด๋ฆฌ

  - ์คํ๋ ๋ ์ํธ์ ํ๊ณ

    - ํฌ๊ธฐ ; ์ผ๋ฐ์ ์ผ๋ก ์ฝ 100๋ง ํ๊น์ง๋ง ์ ์ฅ ๊ฐ๋ฅ

    - ๋ณด์ ; ํ์ผ ๋ฐ ๋งํฌ ์์  ์ฌ๋ถ์ ๋ฐ๋ผ ์ ๊ทผ ๊ถํ ์ค์  > ๋ค์ํ ๊ถํ ์ค์  ์ ๊ณต X

    - ์ ํ์ฑ ; ๋ฐ์ดํฐ ๋ณ๊ฒฝ ์ ์ฌ๋ฌ ์ํธ์ ๋ถ์ฐ๋์ด ์๋ค๋ฉด ๋ณ๊ฒฝ์ ๋๋ฝ ๋ฐ ์ถ๊ฐ ๋ฌธ์  ๋ฐ์ ๊ฐ๋ฅ

### @ What is Database

- ๋ฐ์ดํฐ๋ฒ ์ด์ค ; ์ฒด๊ณ์ ์ธ ๋ฐ์ดํฐ ๋ชจ์ > ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๊ณ  ์กฐ์ํ๋ ์ญํ 

- ๊ฑฐ๋ํ๊ณ  ๋ณต์กํ ๋ฐ์ดํฐ๋ฅผ ๋ค๋ฃจ๊ธฐ ์ํด ๊ณ ์๋ ๋๊ตฌ > ๋ง์ ๊ธฐ๋ฅ ์ ๊ณต

- **CRUD (Create Read Update Delete)**

## ๐ง The Relation

### @ Relational Database

- ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค ; ๋ฐ์ดํฐ ๊ฐ์ **๊ด๊ณ**๊ฐ ์๋ ๋ฐ์ดํฐ ํญ๋ชฉ๋ค์ ๋ชจ์

  - ํ์ด๋ธ, ํ, ์ด์ ์ ๋ณด๋ฅผ **๊ตฌ์กฐํ**ํ๋ ๋ฐฉ์

  - **์๋ก ๊ด๋ จ๋ ๋ฐ์ดํฐ ํฌ์ธํธ๋ฅผ ์ ์ฅ**ํ๊ณ  ์ด์ ๋ํ **์ก์ธ์ค** ์ ๊ณต

    ![แแชแซแแจแแงแผแแตแแต](https://user-images.githubusercontent.com/121418205/217442075-a22bd616-6ec8-41fd-a246-d9b8fe13b096.png)

- ๊ด๊ณ ; ์ฌ๋ฌ ํ์ด๋ธ ๊ฐ์ (๋ผ๋ฆฌ์ ) ์ฐ๊ฒฐ

  - ๊ด๊ณ๋ก ์ธํด ๋ ํ์ด๋ธ์ ์ฌ์ฉํ์ฌ ๋ฐ์ดํฐ๋ฅผ ๋ค์ํ ํ์์ผ๋ก ์กฐํ ๊ฐ๋ฅ (ํน์  ๋ ์ง ๊ตฌ๋งค ๊ณ ๊ฐ ์ ์ฒด ์กฐํ, ์ง๋ ๋ฌ ๋ฐฐ์ก ์ง์ฐ ๊ณ ๊ฐ ์กฐํ ๋ฑ)

- ์์

  - ๋ค์๊ณผ ๊ฐ์ด ๊ฐ ๊ณ ๊ฐ์ด ์ฃผ๋ฌธํ ์ฃผ๋ฌธ๋ฐ์ดํฐ๊ฐ ํ์ด๋ธ์ ์ ์ฅ๋์ด ์๋ค๊ณ  ๊ฐ์ 
    
    ![แแชแซแแจแแงแผแแตแแต2](https://user-images.githubusercontent.com/121418205/217446013-0c44c670-14ee-413e-bf39-219e6da1bb83.png)

    - ๊ธฐ๋ณธ ํค (Primary Key) ; (๊ณ ๊ฐ ํ์ด๋ธ) ๊ฐ ๋ฐ์ดํฐ์ ๊ณ ์ ํ ์๋ณ ๊ฐ ๋ถ์ฌ

    - ์ธ๋ ํค (Foreign Key) ; (์ฃผ๋ฌธ ํ์ด๋ธ) ๊ณ ๊ฐ์ ๊ณ ์ ํ ์๋ณ ๊ฐ ์ ์ฅ

- ์ฉ์ด

  - Table (Rlation) ; ๋ฐ์ดํฐ ๊ธฐ๋กํ๋ **์ต์ข ์์น**

  - Field (Column, Attribute) ; ๊ฐ ํ๋์๋ ๊ณ ์ ํ ๋ฐ์ดํฐ ํ์(ํ์) ์ง์ ๋จ

  - Record (Row, Tuple) ; ๊ฐ ๋ ์ฝ๋์๋ ๊ตฌ์ฒด์  ๋ฐ์ดํฐ ๊ฐ ์ ์ฅ

  - Database (Schema) ; ํ์ด๋ธ์ ์งํฉ (Set of tables)

  - Primary Key ; ๊ฐ ๋ ์ฝ๋์ ๊ณ ์ ํ ๊ฐ / ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค์์ **๋ ์ฝ๋์ ์๋ณ์**๋ก ํ์ฉ

  - Foreign Key ; ํ์ด๋ธ์ ํ๋ ์ค ๋ค๋ฅธ ํ์ด๋ธ์ ๋ ์ฝ๋๋ฅผ ์๋ณํ  ์ ์๋ ํค / ๊ฐ ๋ ์ฝ๋์์ ์๋ก ๋ค๋ฅธ ํ์ด๋ธ ๊ฐ์ **๊ด๊ณ๋ฅผ ๋ง๋๋ ๋ฐ** ์ฌ์ฉ

### @ RDBMS

- DBMS (Database Management System) ; ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ๊ด๋ฆฌํ๋ ์ํํธ์จ์ด ํ๋ก๊ทธ๋จ

- **R**DBMS (**Relational** Database Management System) ;  **๊ด๊ณํ** ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ๊ด๋ฆฌํ๋ ์ํํธ์จ์ด ํ๋ก๊ทธ๋จ (MySQL, PostgreSQL, Oracle Database, MS SQL Server ๋ฑ)

- ๋ฐ์ดํฐ ์ ์ฅ ๋ฐ ๊ด๋ฆฌ๋ฅผ ์์ดํ๊ฒ ํ๋ ์์คํ

- ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ฌ์ฉ์ ๊ฐ์ ์ธํฐํ์ด์ค ์ญํ  ; ์ฌ์ฉ์๊ฐ ๋ฐ์ดํฐ ๊ตฌ์ฑ, ์๋ฐ์ดํธ ๋ชจ๋ํฐ๋ง, ๋ฐฑ์, ๋ณต๊ตฌ ๋ฑ์ ํ  ์ ์๋๋ก ๋์

- MySQL

  - ๊ฐ์ฅ ๋๋ฆฌ ์ฌ์ฉ๋๋ ์คํ ์์ค RDBMS

  - ํน์ง 

    - ๋ค์ํ ์ด์์ฒด์ ์์ ์คํ ๊ฐ๋ฅ

    - ์ฌ๋ฌ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด๋ฅผ ์ํ ๋ค์ํ API ์ ๊ณต

    - MySQL Workbench Tool ํตํด ๊ทธ๋ํฝ ์ธํฐํ์ด์ค(GUI) ์ ๊ณต

  - ๊ตฌ์กฐ

    - **Table โ Database โ Database Server (MySQL)**

    ![MySQLแแฎแแฉ](https://user-images.githubusercontent.com/121418205/217448843-217c8fe2-b3ad-49ca-8e6b-52b5a01d2834.png)
    