while True:
    print('-=' * 12)
    print('\033[32;42m      CALCULATOR     \033[m')
    print('-=' * 12)
    num1 = int(input('\033[4mEnter the first number: \033[m'))
    num2 = int(input('\033[4mEnter the second number: \033[m'))
    print('\033[===== MENU =====\033[m')
    print('\033[4m[ 1 ] Add\033[m')
    print('\033[4m[ 2 ] Multiply\033[m')
    print('\033[4m[ 3 ] Compare\033[m')
    print('\033[4m[ 4 ] New numbers\033[m')
    print('\033[4m[ 5 ] Exit\033[m')
    print('\033[4m[ 6 ] Subtract\033[m')
    print("\033[4m[ 7 ] Divide\033[m")
    choice = int(input('\033[4mSelect option (1-7): \033[m'))
    if choice == 1:
            print('\033[33m{} + {} = {} \033[m'.format(num1, num2, num1 + num2))
    elif choice == 2:
          print("\033[33m{} x {} = {}\033[m".format(num1, num2, num1*num2))
    elif choice == 3:
          if num1 > num2:
                print('\033[32m{} is greater than {}\033[m'.format(num1, num2))
          elif num2 > num1:
            print('\033[32m{} is greater than {}\033[m'.format(num2, num1))
          else:
            print('\033[34mBoth numbers are equal. \033[m')
    elif choice== 4:
         print('\033[36mYou chose to enter new numbers.\033[m')
         continue 
    elif choice == 5:
         print('\033[31mExiting the program...\033[m')
         exit()
    elif choice == 6:
         print('\033[32m{} - {} = {}\033[m'.format(num1, num2, num1-num2))
    elif choice == 7:
         if num2 == 0:
              print('\033[31mCannot divide by zero.\033[m')
         else:
              print('\033[32m{} ÷ {} = {:.2f}\033[m'.format(num1, num2, num1/num2))
                
          
    else:
            print('\033[31mInvalid option. Please try again\033[m')