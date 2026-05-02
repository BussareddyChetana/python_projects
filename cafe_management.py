print("WELCOME TO MY PYTHON CAFE")
print("HI MAM")
menu={
  "pizza":100,
  "Burger":150,
  "Mocktail":200,
  "pasta":300,
  "shakes":250
}
print('pizza:100\nBurger:150\nMocktail:200\npasta:300\nshakes:250')
order_item=input("Enter your item: ")
order_total=0
if order_item in menu:
  order_total+=menu[order_item]
  order=input("Do you want anything else(Yes/No): ")
  if order=="Yes":
    order_item2=input("Enter your second item: ")
    if order_item2 in menu:
      order_total+=menu[order_item2]
      print(f'Your order value:{order_total}')
  else:
    print(f'Your order value:{order_total}')
else:
  print("You entered a wrong item")

