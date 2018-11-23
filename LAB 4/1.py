sb=0
cb=0
while 1:
    print"Saving balance is",sb
    print"Current balance is",cb
    choice = input("Enter 1 for saving and 2 for current and 3 to exit")
    if choice==1:
        print"Enter 1 to deposit and 2 to withdraw"
        ch=input('Enter Choice')
        if ch==1:
            de=input("Enter amount")
            sb+=de
        elif ch==2:
            if sb<1000:
                print"Error"
            else:
                wi=input("Enter amount")
            if sb-wi>1000:
                print"Amount withdrawl",wi
                sb-=wi
            else:
                break
    elif choice==1:
        while 1:
            print"Enter 1 to deposit and 2 to withdraw"
            ch=input("Enter Choice")
            if ch==1:
                de=input("Enter amount")
                cb+=de
            elif ch==2:
                if cb<10000:
                    print"Error"
                else:
                    wi=input("Enter amount")
                    if cb-wi>=10000:
                        print"Amount Withdrawl",wi
                        cb-=wi
                    else:
                        break
            elif choice==3:
                break;
