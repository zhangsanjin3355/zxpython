def print_menu():
    print("="*50)
    print("  名片管理系统  ")
    print("="*50)

def print_triangle():
    i = 1
    while i<=5:
        j = 1
        while j<=i:
            print("*",end="")
            j+=1
        print("")
        i+=1



print_triangle()
print_menu()
