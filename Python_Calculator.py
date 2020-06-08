while(True):
    choice = int(input(" press 1 for addition \n press 2 for substraction  \n press 3 for multipication   \n press 4 for division \n press 5 for exit \n enter your choice : "))
    if choice==5:
        print("Thank you for visiting!")
        break
    num = int(input('enter your 1st number : '))
    num2 = int(input('enter your 2nd number : '))
    if choice==1:
        sum = (num + num2)
        print('Addition of' +str(num)+' and '+str(num2)+' is ', sum)
    elif choice==2:
        minus = (num - num2)
        print('your solution = ', minus)
    elif choice==3:
        multiply = (num*num2)
        print('your solution = ', multiply)
    elif choice==4:
        divide = (num/num2)
        print('your solution = ', divide)
