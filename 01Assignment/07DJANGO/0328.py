"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""

In [1]: Todo.objects.create(content='실습 제출', priority=5,completed=False, deadline='2023-03-28')
Out[1]: <Todo: Todo object (1)>

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""

In [1]: Todo.objects.create(content='데일리 설문(오후) 제출', deadline='2023-03-28')
Out[1]: <Todo: Todo object (2)>

"""
3. 임의의 할 일 5개 생성
"""

In [2]: Todo.objects.create(content='random1')
Out[2]: <Todo: Todo object (3)>

In [3]: Todo.objects.create(content='random2')
Out[3]: <Todo: Todo object (4)>

In [4]: Todo.objects.create(content='random3')
Out[4]: <Todo: Todo object (5)>

In [5]: Todo.objects.create(content='random4')
Out[5]: <Todo: Todo object (6)>

In [6]: Todo.objects.create(content='random5')
Out[6]: <Todo: Todo object (7)>

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""

In [1]: Todo.objects.order_by('pk')
Out[1]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>, <Todo: Todo object (8)>, <Todo: Todo object (9)>, <Todo: Todo object (10)>]>

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""

In [2]: Todo.objects.order_by('-priority')
Out[2]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (3)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (4)>, <Todo: Todo object (7)>, <Todo: Todo object (8)>, <Todo: Todo object (9)>, <Todo: Todo object (10)>, <Todo: Todo object (2)>]>

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

In [3]: Todo.objects.get(pk=1)
Out[3]: <Todo: Todo object (1)>

"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""

In [15]: newspaper.objects.get(pk=1).journalist
Out[15]: 'Laney Mccullough'

"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""

In [9]: newspaper.objects.filter(journalist='Laney Mccullough').count()
Out[9]: 858

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""

In [10]: newspaper.objects.order_by('-pk')
Out[10]: <QuerySet [<newspaper: newspaper object (10000)>, <newspaper: newspaper object (9999)>, <newspaper: newspaper object (9998)>, <newspaper: newspaper object (9997)>, <newspaper: newspaper object (9996)>, <newspaper: newspaper object (9995)>, <newspaper: newspaper object (9994)>, <newspaper: newspaper object (9993)>, <newspaper: newspaper object (9992)>, <newspaper: newspaper object (9991)>, <newspaper: newspaper object (9990)>, <newspaper: newspaper object (9989)>, <newspaper: newspaper object (9988)>, <newspaper: newspaper object (9987)>, <newspaper: newspaper object (9986)>, <newspaper: newspaper object (9985)>, <newspaper: newspaper object (9984)>, <newspaper: newspaper object (9983)>, <newspaper: newspaper object (9982)>, <newspaper: newspaper object (9981)>, '...(remaining elements truncated)...']>

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""

In [11]: newspaper.objects.order_by('-created_at')
Out[11]: <QuerySet [<newspaper: newspaper object (4719)>, <newspaper: newspaper object (97)>, <newspaper: newspaper object (5500)>, <newspaper: newspaper object (4918)>, <newspaper: newspaper object (5753)>, <newspaper: newspaper object (3706)>, <newspaper: newspaper object (4012)>, <newspaper: newspaper object (452)>, <newspaper: newspaper object (6865)>, <newspaper: newspaper object (3265)>, <newspaper: newspaper object (2643)>, <newspaper: newspaper object (7022)>, <newspaper: newspaper object (3700)>, <newspaper: newspaper object (3236)>, <newspaper: newspaper object (9607)>, <newspaper: newspaper object (4461)>, <newspaper: newspaper object (419)>, <newspaper: newspaper object (251)>, <newspaper: newspaper object (8613)>, <newspaper: newspaper object (1670)>, '...(remaining elements truncated)...']>

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

In [12]: newspaper.objects.filter(journalist__contains='Britney').count()
Out[12]: 799

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""

In [33]: qrst = newspaper.objects.filter(journalist = 'Britney Mahoney') | newspaper.objects.filter(journalist = 'Arianna Walls') | newspaper.objects.filter(journalist = 'Carl Short')
In [34]: qrst.count()
Out[34]: 2469

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""

In [38]: newspaper.objects.filter(created_at__gt='2000-01-01 00:00:00').count()
Out[38]: 4355

"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""
In [22]: print(f"title : {Newspaper.objects.last().title}\ncontent : {Newspaper.objects.last().content}\njournalist : {Newspaper.objects.last().journalist}")
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough