S =input()
if(S==S[::-1]):
      print("Yes")
else:
      print("No")
'''In the above program, first take input from the user (using input OR raw_input() method) 
to check for palindrome. Then using slice operation [start:end:step], check whether the string 
is reversed or not. Here, step value of -1 reverses a string. If yes, it prints a palindrome else, 
not a palindrome.'''