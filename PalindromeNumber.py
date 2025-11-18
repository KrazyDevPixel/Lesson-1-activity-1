num=int(input("Enter a palindrome number: "))
orinum=num
revnum=0
while num>0:
    digit=num%10
    revnum=revnum*10+digit
    num=num//10
if orinum==revnum:
    print(f"{orinum} is a palindrome number.")
else:
    print(f"{orinum} is not a palindrome number.")
