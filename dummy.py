import sys 
s = sys.stdin.readline().strip()

if s==s[::-1]:
  print("Palindrome")
else:
  print("Non Palindrome")
