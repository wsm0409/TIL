# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2.  연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3.  신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;
```

```
MAX(height)  MIN(height)  MAX(weight)  MIN(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT count(height) FROM healthcare WHERE 160 <= height and  
170 >= height;
```

```
count(height)
-------------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.

```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 and waist != ""  ORDER BY waist DESC LIMIT 5;
```

```
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;  
count(*)
```

```
36697
```
### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT count(blood_pressure) FROM healthcare WHERE blood_pressure <= 120;
```

```
count(blood_pressure)
---------------------
423239
```
### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT count(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
count(waist)
------------
145819
```
### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```
### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id,weight FROM healthcare ORDER BY height DESC LIMIT 1 OFFSET 1;
```

```
id     weight
-----  ------
46642  100
```
### 11. BMI가 30이상인 사람의 수를 출력하시오.

```sql
 SELECT count(*) FROM healthcare WHERE weight/(0.0001*height*height) >= 30;
```

```
count(*)
--------
53121
```
### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

```sql
SELECT id,weight/(0.0001*height*height) FROM healthcare WHERE smoking =3 ORDER BY weight/(0.0001*height*height) DESC LIMIT 5;
```

```
231431  50.78125
934714  49.9479708636837
722707  48.828125
947281  47.7502295684114
948801  47.7502295684114
```
### 13. 흡연이 3인 사람 중에서 공백을 제외한 혈압이 가장 높은 3명의 id와 혈압을 출력하세요.

```sql
SELECT id, blood_pressure FROM healthcare WHERE smoking = 3 and blood_pressure != "" ORDER BY blood_pressure DESC LIMIT 3;

```

```
id      blood_pressure
------  --------------
12682   260
825986  241
747506  240
```
### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```
### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```
