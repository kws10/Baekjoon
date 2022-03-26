x,y,w,h = map(int,input().split())

width = w-x
height = h-y

if width<height:
   if width>x:
      print(x)
   else:
      print(width)
      print(width)
else:
   if height>y:
      print(y)
   else:
      print(height)
