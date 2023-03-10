# 1229 THU

## ๐ branch

- branch : ๋๋ฆฝ์ ์ธ ์์ํ๋ฆ์ ๋ง๋ค๊ณ  ๊ด๋ฆฌ

### @ ๋ธ๋์น ๋ช๋ น์ด

- ๋ธ๋์น ์์ฑ *(master) $ git branch {branch name}*

- ๋ธ๋์น ์ด๋ *(master) $ git checkout {branch name}*

- ๋ธ๋์น ์์ฑ ๋ฐ ์ด๋ *(master) $ git checkout -b {branch name}*

- ๋ธ๋์น ๋ชฉ๋ก *(master) $ git branch*

- ๋ธ๋์น ์ญ์  *(master) $ git branch -d {branch name}*

### MERGE

- ๊ฐ branch ์์ ์ด๋ ฅ ํฉ์น๋ ๋ช๋ น์ด

  - ๋์ผํ ํ์ผ์ ์์ ํ ๊ฒฝ์ฐ ์ถฉ๋ ๋ฐ์ ; ์ง์  ํด๋น ํ์ผ ํ์ธํ๊ณ  ์ ์ ํ๊ฒ ์์ ํ ์ดํ ์ง์  ์ปค๋ฐ ์คํ

  - ๋ค๋ฅธ ํ์ผ์ ์์ ํ ๊ฒฝ์ฐ ; ์ถฉ๋ ์์ด ์๋์ผ๋ก Merge Commit ์์ฑ๋จ

- merge - fast forward

  - ๊ธฐ์กด master ๋ธ๋์น์ ๋ณ๊ฒฝ์ฌํญ ์์ด ๋จ์ํ ์์ผ๋ก ์ด๋

    1. feature-a branch๋ก ์ด๋ ํ commit

    2. master ๋ณ๋ ๋ณ๊ฒฝ ์์

    3. master branch๋ก ๋ณํฉ

- merge - merge commit

  - ๊ธฐ์กด master ๋ธ๋์น์ ๋ณ๊ฒฝ์ฌํญ ์์ด ๋ณํฉ ์ปค๋ฐ ๋ฐ์

    1. feature-a branch๋ก ์ด๋ ํ commit

    2. master branch commit

    3. master branch๋ก ๋ณํฉ

## ๐ Git Flow

- Git์ ํ์ฉํ์ฌ ํ์ํ๋ ํ๋ฆ

- ๋ธ๋์น๋ฅผ ํ์ฉํ๋ ์ ๋ต

  ![branch](https://gmlwjd9405.github.io/images/types-of-git-branch/total-branch.png)

  ![gitflow](https://user-images.githubusercontent.com/121418205/209908818-1e02d725-12ca-4ead-9c7f-ff3ed34562b4.jpg)

### @ GitHub Flow ๊ธฐ๋ณธ ์์น

- master branch๋ ๋ฐ๋์ ๋ฐฐํฌ ๊ฐ๋ฅํ ์ํ

- feature branch๋ ๊ฐ ๊ธฐ๋ฅ์ ์๋๋ฅผ ์ ์ ์๋๋ก ์์ฑ

- Commit message๋ ๋ชํํ๊ฒ ์์ฑ

- Pull Request ํตํด ํ์ ์งํ

- ๋ณ๊ฒฝ์ฌํญ ๋ฐ์ํ๊ณ  ์ถ์ผ๋ฉด master branch์ ๋ณํฉ

### @ GitHub Flow Model์ ๋ฐ๋ฅธ ์์ ์์

- Shared Repository Model (๊ฐ = respository owner / project manager ์ = collaborator)

  > ๋์ผํ ์ ์ฅ์๋ฅผ ๊ณต์ ํ์ฌ ํ์ฉ

  1. ํ์ ์ด๋ ๋ฐ ์ ์ฅ์ Clone

    - step 0-1. Invite collaborator
    
      - ๊ฐ์ด ์ ์ด๋
      
      - collaborator์ ๋ฑ๋ก๋์ด์ผ ํด๋น ์ ์ฅ์์ ๋ํ push ๊ถํ ์๊น

    - step 0-2. Accept Invitation

      - (์) ์ด๋ฉ์ผ ํตํด ์ด๋ ์๋ฝ

      - ํด๋น ์ ์ฅ์ ์ฃผ์ ๋ค์ /invitation ๋ถ์ด๋ ๊ฒ๋ ๊ฐ๋ฅ

    - step 0-3. Clone project(remote) repository

      - (์) Clone ์ดํ ์์ ํ๊ฒฝ ์ค์  ๋ง๋ฌด๋ฆฌ

  2. ๋ธ๋์น์์ ์์ ๋ฐ GitHub Push

    - Step 1. Feature branch ์์ฑ ๋ฐ ์์

      - (์) ํญ์ ๋๋ฆฝ์ ์ธ feature branch์์ ์์

      - master branch๋ ๋ฐฐํฌ ๊ฐ๋ฅํ ์ํ๋ฅผ ์ ์ง

      - feature branch๋ ๊ธฐ๋ฅ ๊ฐ๋ฐ (์ด๋ฆ ์์ฑ ์ ๊ธฐ๋ฅ์ ๋ช์)

    - Step 2-1. Commit

      - (์) Commit์ผ๋ก ์์์ ์ด๋ ฅ์ ๋จ๊ธด๋ค

      - ์ฝ๋ ๋ณํ์ ๋ง์ถฐ ์ค์ (**๋จ์ ์ค๊ฐ ์ ์ฅ X**)

    - Step 2-2. Push to remote repository

      - (์) ์์ฑ๋ ์ฝ๋๋ ์๊ฒฉ ์ ์ฅ์์ push

      - ์๊ฒฉ ์ ์ฅ์์ ๊ณต๊ฐ๋ ์ด๋ ฅ์ **์ ๋ ๋ณ๊ฒฝ ๊ธ์ง**

  3. Pull Request ์์ฑ

    - step 3-1. Open a Pull Request

      - (์) ๊นํ์ ๋ค์ด๊ฐ์ Pull Request

    - step 3-2. Create Pull Request

      - (์) PR ์ค์  ์งํ ํ ์์ฒญ ์์ฑ

  4. Review ๋ฐ Merge

    - step 4. Merge pull request

      - (๊ฐ) ์์ฑ๋ ์ฝ๋ ํ์ธ ํ ๋ณํฉ
      
      - ์ฝ๋ ๋ฆฌ๋ทฐ ์งํ ํ ๊ด๋ฆฌ์ ํ๋จ ํ์ ๋ณํฉ

      - ๋ณํฉ ๊ณผ์ ์์ ์ถฉ๋ ๋ฐ์ ์ ํด๊ฒฐ ํ ๋ณํฉ

      - master branch๋ก ๋ณํฉํ  ๋๋ ์ฝ๋๊ฐ ๋ฐฐํฌ ๊ฐ๋ฅํ ์ํ์ฌ์ผ ํ๋ค

  5. ๋ณํฉ ์๋ฃ ํ ๊ฐ๋ฐ์ ํ๋ค๋ฉด?

    - (์) ๋ก์ปฌ ์ ์ฅ์์์๋ merge๋ branch ์ญ์ ํ๊ณ  master branch๋ฅผ ์๋ฐ์ดํธ ์ดํ 1. ~ 3. ๊ณผ์  ๋ฐ๋ณต

- Fork & Pull Model

  > Repository > Collaborator์ ๋ฑ๋ก๋์ง ์์ ์ํ์์ ์งํ (๊นํ ๊ธฐ๋ฐ ์คํ์์ค ์ฐธ์ฌ์)

  1. Fork & Clone

    - step 0-1. Fork repository

      - (์) Forking project repository

      - ์๊ฒฉ ์ ์ฅ์๋ฅผ fork
    
      - ๋ด ์ ์ฅ์๋ก ๋ณต์ ๋ณธ ๊ฐ์ ธ์ด์ผ๋ก์จ ๋ก์ปฌ ์์ ํ ์๊ฒฉ ์ ์ฅ์๋ก pushํ  ์ ์๊ฒ ๋จ

    - step 0-2. Clone project(remote) repository

      - (์) Clone ํ ์์ ํ๊ฒฝ ์ค์  ๋ง๋ฌด๋ฆฌ

      - **Clone์ ๋ฐ๋์ ๋ณธ์ธ ์ ์ฅ์์ธ์ง ํ์ธ**

  2. ~ 4.๋ Shared Repository Model๊ณผ ๋์ผ

  5. ๋ณํฉ ์๋ฃ ํ ๊ฐ๋ฐ์ ํ๋ค๋ฉด?

    - (์) ๋ก์ปฌ ์ ์ฅ์์์๋ merge๋ branch ์ญ์ ํ๊ณ  master branch๋ฅผ ์๋ฐ์ดํธ

    - master branch๋ ์๋ณธ ์ ์ฅ์๋ฅผ ๋ฐ์์์ผ ํ๋ฉฐ ๋ณ๋์ ์๊ฒฉ ์ ์ฅ์๋ฅผ ์ถ๊ฐํ์ฌ ์งํ ๊ฐ๋ฅ 
    
        (GitHub์์ fetch upstream๋ ๊ฐ๋ฅ)