print("Welcome to Tossin's")
Name = input("Please enter your name:  ")
Number = int(input("Please enter your contact  number: "))
print("Hello ",Name,"Please place your order below")
tops=""
cost=0
print("Press 1 for Veg \nPress 2 for Non-Veg ")
preference_choice=int(input("Enter your preference:  "))
if preference_choice == 1:
    print("Press 1 for Normal crust\nPress 2 for Thin crust\nPress 3 for Cheese Burst")
    crust_type=int(input("Please select your type of crust: "))
    if crust_type ==1:
        print("Press 1 for Margarita\nPress 2 for Farm Fresh\nPress 3 for Paneer Bonanza")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+200   
            pizza="Margarita -     200Rs."         
        if pizza_type==2:
            cost=cost+250
            pizza="Farm Fresh -    250Rs."                   
        if pizza_type==3:
            cost=cost+300
            pizza="Paneer Bonanza- 300Rs."
                   
    if crust_type==2:
        print("Press 1 for Margarita\nPress 2 for Farm Fresh\nPress 3 for Paneer Bonanza")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+250
            pizza="Margarita -     250Rs."                    
        if pizza_type==2:
            cost=cost+300
            pizza="Farm Fresh-    300Rs."                    
        if pizza_type==3:
            cost=cost+350
            pizza="Paneer Bonanza- 350Rs."
                   
    if crust_type==3:
        print("Press 1 for Margarita\nPress 2 for Farm Fresh\nPress 3 for Paneer Bonanza")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+300
            pizza="Margarita -     300Rs."                    
        if pizza_type==2:
            cost=cost+350
            pizza="Farm Fresh-    350Rs."                    
        if pizza_type==3:
            cost=cost+400
            pizza="Paneer Bonanza- 400Rs."
                   
if preference_choice==2:
    print("Press 1 for Normal crust\nPress 2 for Thin crust\nPress 3 for Cheese Burst")
    crust_type=int(input("Please select your type of crust: "))
    if crust_type ==1:
        print("Press 1 for butter chicken\nPress 2 for chicken tikka\nPress 3 for Pepperoni")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+250
            pizza="Butter chicken - 250Rs."                   
        if pizza_type==2:
            cost=cost+250
            pizza="Chicken tikka -  250Rs."                   
        if pizza_type==3:
            cost=cost+300
            pizza="Pepperoni -      300Rs."
                   
    if crust_type==2:
        print("Press 1 for butter chicken\nPress 2 for chicken tikka\nPress 3 for Pepperoni")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+300
            pizza="Butter chicken - 300Rs."                    
        if pizza_type==2:
            cost=cost+300
            pizza="Chicken tikka -  300Rs."                   
        if pizza_type==3:
            cost=cost+350
            pizza="Pepperoni -      350Rs."
                   
    if crust_type==3:
        print("Press 1 for butter chicken\nPress 2 for chicken tikka\nPress 3 for Pepperoni")
        pizza_type =int(input("Please select your type of pizza: "))
        if pizza_type == 1:
            cost=cost+350
            pizza="Butter chicken - 350Rs."                     
        if pizza_type==2:
            cost=cost+350
            pizza="Chicken tikka -  350Rs."                   
        if pizza_type==3:
            cost=cost+400
            pizza="Pepperoni -      400Rs."
while True:
   print("Press 1 for onions-20Rs.\nPress 2 for capsicums-20Rs.\nPress 3 for olives-30Rs.\nPress 4 for jalapenos-30Rs.\nPress 5 for extra cheese-40Rs.\Press 6 for mushrooms-30Rs.\nPress 7 for Exit")
   toppings=int(input("Please select your prefered toppings: "))
   if toppings==1:
       cost=cost+20
       tops=tops+"Onion-20Rs. \n"
   elif toppings==2:
       cost=cost+20
       tops=tops+"Capsicum-20Rs. \n"
   elif toppings==3:
       cost=cost+30
       tops=tops+"Olives-30Rs. \n"
   elif toppings==4:
       cost=cost+30
       tops=tops+"Jalapenos-30Rs. \n"
   elif toppings==5:
       cost=cost+40
       tops=tops+"Extra Cheese-40Rs. \n"
   elif toppings==6:
       cost=cost+30
       tops=tops+"Mushrooms-30Rs. \n"
   elif toppings==7:
       break
   else:
       print("Invalid Input")
print("**********************************")       
print("the Pizza you have ordered is ",pizza)       
print("the toppings you have selected\n ",tops)        
total_cost=cost+(18/100)*cost                              
print("the Bill is  ",cost,"Rs.")  
print("the GST is  ",(18/100)*cost,"Rs.")
print("the Final amount is  ",total_cost,"Rs.")                 
print("***********************************")                                      
                                  
                   
                       
                                               
                   
               
        