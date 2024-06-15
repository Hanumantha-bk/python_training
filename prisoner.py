# n=5  #No of Prisoners
# c=2  #No of Chocaltes
# s=3
# l=(s+c-1)%n
# if l==0:
#     l==n
# print(l)

# # Functions :
# # Write once,execute many times
# # to call functions To Invoke the instruction set..
# def city():
#     print("Bangalore")
# city()

# # What are Parameters and Arguments 
# # Parameters : no of variables 
# # Arguments : 

# def city(a,b):
#     print("Ben")
#     print(a**b)
# city(2,3)

# # default arguments.
# # keyword arguments.
# # positional arguments.
# # arbitrary positional arguments.


# def city(name="Hyd"):
#     print(name)
# city()
# city("Blr")


# # Write a program to build a Login System Using Functions.
# # The function name should be login and register.
# # -it asks user to enter the details for registration and out of all this 
# # details only username and password should be stored.
# # -Now this function should ask aser name and password 
# # if these match with the registered details login success 
# # otherwise repeat the login process invalid credenitials.
# # Dictionary to store user credentials
# d = {}
# def register():
#     user_name = input("Enter username: ")
#     password = input("Enter password: ")
#     if user_name in d:
#         print("Username already exists! Try again.")
#     else:
#         d[user_name] = password

# def login():
#     print("Login:")
#     while True:
#         user_name = input("Enter username: ")
#         password = input("Enter password: ")
#         if user_name in d and d[user_name] == password:
#             print("Login successful!")
#             break
#         else:
#             print("Invalid credentials. Please try again.")

# def main():
#     while True:
#         print("\n1. Register")
#         print("\n2. Login")
#         print("\n3. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             register()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             print("Exiting the system.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
# def loginandreg():
#     d={}
#     print("Welcome to register")
#     u_name=input("Enter use:")
#     u_pwd=input("Enter u_id:")
#     name=input("enter name:")
#     ph_no=input("Enter Ph_no:")
#     d[u_name]=u_pwd
    
#     while True:
#         print("Welcome To Login")
#         l_name=input("enter login user")
#         l_pwd=input("enter login user password")
        
#         if l_name in d:
#             if d[l_name]==l_pwd:
#                 print("Login Success")
#                 break
#             else:
#                 print("Enter Valid passcode")
#         else:
#             print("user not found")
#             break

# loginandreg()
# str='hanumantha kuad man g'
# str_space=str.count(' ')
# print(str_space)

# def choclate(list):
#     c=0
#     empty=[]
#     for i in list:
#         if i==0:
#             continue
#             c+=1
#         else:
#             empty.append(i)
#     empty=empty+[0]*c
#     return empty
# list=[4,0,5,0,1,9,0,0]
# print(choclate(list))


# # i/p :list=[4,0,5,0,1,9,0,0]
# # o/p:[4,5,1,9,0,0,0,0]
# i=0
# j=0
# a=0
# for i in list:
#     if a[i]!=0:
#         a[j]=a[i]
#         j=j+1
#     else:
#         continue
# while j<list:
#     a[j]=0
#     j=j+1

    
# # Recursion :
# # One Big Problem can be broken into mulipe problems.

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# num=int(input("enter a num"))

# if num<0:
#     print("Write Positive Number")
# elif num==0:
#     print("Fact of 0! is 1")
# else:
#     print(fact(num))

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))
# nt=int(input("Enter a  NUm :"))
# if nt<=0:
#     print("Enter a Positive no")
# else:
#     print("Fibo Sequ are:")
# for i in range(nt):
#     print(fib(i))

# def two_pointer_approach(arr):
#     left_pointer = 0
#     right_pointer = len(arr) - 1
    
#     while left_pointer < right_pointer:
#         # Do something with arr[left_pointer] and arr[right_pointer]
#         left_pointer += 1  # Move left pointer
#         right_pointer -= 1  # Move right pointer
        
#     # Process the remaining elements or perform any final steps

# # Example usage:
# input_array = [1, 2, 3, 4, 5]
# two_pointer_approach(input_array)


# input:list=[2,1,0,1,1,2,0,0]
# output:list=[0,0,0,1,1,1,2,2]
# def chock(a):
#     i = 0
#     j = len(a)-1
#     # while i<j:
#     #     a[i],a[j] = a[j],a[i]
#     #     i+= 1  
#     #     j-= 1  
# list = [2,1,0,1,1,2,0,0]
# # chock(list.copy())  
# print(chock(list))
# def chock(a):
#     c_0=0
#     c_1=0
#     c_2=0
#     for i in range(len(a)):
#         if a[i]==0:
#             c_0 += 1
#         elif a[i]==1:
#             c_1 +=1
#         else:
#             c_2 +=1
#     j=0
#     while c_0>0:
#         a[j]=0
#         j+=1
#         c_0-=1
#     while c_1>0:
#         a[j]=1 
#         j+=1
#         c_1-=1  
#     while c_2>0:
#         a[j]=2 
#         j+=1
#         c_2-=1  
#     return a  
# list=[2, 1, 0, 1, 1, 2, 0, 0]
# listt=chock(list)
# print(listt)

# class CarShowroom:
#     def __init__(self):
#         self.car_companies = {
#             "Toyota": {
#                 "Corolla": {"Base": 20000, "Sport": 25000, "Luxury": 30000},
#                 "Camry": {"Base": 30000, "Sport": 35000, "Luxury": 40000}
#             },
#             "Honda": {
#                 "Civic": {"Base": 21000, "Sport": 26000, "Luxury": 31000},
#                 "Accord": {"Base": 32000, "Sport": 37000, "Luxury": 42000}
#             },
#             "Ford": {
#                 "Focus": {"Base": 18000, "Sport": 23000, "Luxury": 28000},
#                 "Fusion": {"Base": 27000, "Sport": 32000, "Luxury": 37000}
#             }
#         }
#         self.sgst = 0.09
#         self.cgst = 0.09

#     def car_company(self):
#         while True:
#             company = input("Please select a car company (Toyota, Honda, Ford): ")
#             if company in self.car_companies:
#                 self.selected_company = company
#                 break
#             else:
#                 print("Invalid company. Please reenter.")

#         while True:
#             print(f"Available models for {self.selected_company}: {list(self.car_companies[self.selected_company].keys())}")
#             model = input("Please select a car model: ")
#             if model in self.car_companies[self.selected_company]:
#                 self.selected_model = model
#                 break
#             else:
#                 print("Invalid model. Please reenter.")

#         while True:
#             print(f"Available variants for {self.selected_model}: {list(self.car_companies[self.selected_company][self.selected_model].keys())}")
#             variant = input("Please select a car variant: ")
#             if variant in self.car_companies[self.selected_company][self.selected_model]:
#                 self.selected_variant = variant
#                 break
#             else:
#                 print("Invalid variant. Please reenter.")

#         base_price = self.car_companies[self.selected_company][self.selected_model][self.selected_variant]
#         total_price = base_price + (base_price * self.sgst) + (base_price * self.cgst)
#         print(f"Total price for {self.selected_variant} {self.selected_model} from {self.selected_company} is: ${total_price:.2f}")

# showroom = CarShowroom()
# showroom.car_company()

#Finding The Next Greatest Array

# input : 14,2,16,4,3,5
