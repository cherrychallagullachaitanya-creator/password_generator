import random
Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['1','2','3','4','5','6','7','8','9','0']
sysmbols=['!','@','#','$','%','^','&','*','(',')','-','+','=','~','?']
no_of_letters=int(input("Enter the number of letters you want in your password?"))
no_of_sysmbols=int(input("Enter the number of sysmbols you want in your password?"))
no_of_digits=int(input("Enter the number digits you want in your password?"))
password_list=[]
for i in range(1,no_of_letters+1):
  char=random.choice(Letters)
  password_list+=char
for i in range(1,no_of_sysmbols+1):
  char=random.choice(sysmbols)
  password_list+=char
for i in range(1,no_of_digits+1):
  char=random.choice(digits)
  password_list+=char
random.shuffle(password_list)
password=""
for char in password_list:
  password+=char
print(password)
