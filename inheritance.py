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
