#family details

details = input("Do you want to store  your family details in database : yes or no :? " ).lower()

while(details != " " or " no") :
        sir_name = input("Enter your sir name: ")
        for each_row in range(1,5):
                name = input("enter your full name")
                print(f"{sir_name} . {name}")
                