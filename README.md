# 숨어있는 숫자의 덧셈 (1) 

<p>
문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
</p>

```
<제한 사항>
1 ≤ my_string의 길이 ≤ 1,000
my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

=== 입출력 예 ===
my_string	      result
"aAb1B2cC34oOp"	10
"1a2b3c4d123"	  16
```

<p>입출력 예 설명</p>

```
입출력 예 #1

"aAb1B2cC34oOp"안의 한자리 자연수는 1, 2, 3, 4 입니다. 따라서 1 + 2 + 3 + 4 = 10 을 return합니다.
입출력 예 #2

"1a2b3c4d123Z"안의 한자리 자연수는 1, 2, 3, 4, 1, 2, 3 입니다. 따라서 1 + 2 + 3 + 4 + 1 + 2 + 3 = 16 을 return합니다.
```

<a href="https://school.programmers.co.kr/learn/challenges/beginner?order=acceptance_desc&languages=python">출처: 프로그래머스 코딩 테스트 연습</a>
