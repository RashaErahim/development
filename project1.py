welcome_message='Welcome to our website Rasha.com'
Passward_rules=''' the passward must be:
at least 8 characters
contain at least on uppercase 
contain at least one lower case 
contain at least one digit 
contain at least one of these characters :!,@,$,%,^,*,&
doesn't contain any spaces
'''
username_rules= '''The username must be :
must be start  with lower case and only contain letters,numbers and underscore.

'''
print(welcome_message)
print(Passward_rules)
print(username_rules)
username,passward,system_username,system_passward='','','',''
error_message=['invalid username','username is taken','invalid passward']
invalid_username=error_message[0]
username_taken=error_message[1]
invalid_passward=error_message[2]
while True:
     username = input('Please enter username: ') 
     passward=input('Please enter passward:')
     #testing username:
     #test_1: Check if the first letter in the usrename is lowercase
     if not username[0].islower():  
          print(invalid_username)
          continue
     #test_2:test :test if the username contain letters,numbers, and underscore.
     alphnumric_test=username.isalnum() or username=='_'
     if not (username.isalnum() or username=='_'):
          print(invalid_username)
          continue
     #testing passward:
     #test_1:at least contain 8 characters
     eight_characters_test=len(passward) >=8
     if not eight_characters_test:
          print(invalid_passward)
          continue
     # #test_2:contain at least one  uppercase letter
     uppercase_letter_test=passward.isupper()
     print(uppercase_letter_test)
     if not (uppercase_letter_test):
          print(invalid_passward)
          continue
     #test_3:contain at least one lowecase letter.
     loercase_letter_test=passward.islower()
     print(loercase_letter_test)
     if not loercase_letter_test:
          print(invalid_passward)
          continue 
     #print('this pass testing')
     #test_4:contain at least one digit
     one_digit_test=passward.isdigit()
     print(one_digit_test)
     if not one_digit_test:
          print(invalid_passward)
          continue
     #test_5:test it contain special characters
     special_char="!,@,#,$,^,&,*,_,-"
     for char in passward:
          if char in special_char:
               print("this pass test")
     else:
               print(invalid_passward)

               continue
     #test_6:test it doesn't contain space
     if ' ' in passward:
           print(invalid_passward)
           continue
username_taken="'admin',admin123,user1,superuser" 
if username in username_taken:
     print("username_taken")
     

           


     system_username=username
     print(system_username)

