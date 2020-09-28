month=int(input())
dic={31:[1,3,5,7,8,10,12],30:[4,6,9,11]}
if month <=0 or month >12:
  print("Error")
elif month==2:
  print('28')
else:
  for x in dic:
    if month in dic[x]:
      print(x)
