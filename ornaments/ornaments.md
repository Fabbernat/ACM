# Ornaments
A factory is making ornaments for the upcoming holidays. Ornaments consist of a 2D glass sphere (i.e., a circle) that is designed to hang off a hook or nail using a string that tightly wraps around the ornament.

Your task is to write a program that calculates the length of the string, given the radius 
𝑟
r of the circle, the distance 
ℎ
h from the knot to the center of the circle, and some multiplier to account for the excess needed to tie the knot.

## Input
The input will contain multiple test cases, up to 200. Each test case contains a single line with three integers 
𝑟
r (
1
≤
𝑟
≤
10
,
000
1≤r≤10,000), 
ℎ
h (
𝑟
≤
ℎ
≤
10
,
000
r≤h≤10,000), and 
𝑠
s (
0
≤
𝑠
≤
100
0≤s≤100). The input terminates with a line containing 0 0 0.

## Output
For each test case, output the length of the needed string, rounded to two decimals.

### Sample Input

1 3 10
2 5 8
10 11 0
0 0 0
### Sample Output

10.43
18.46
63.40