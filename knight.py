""" knight"""

def Enter(x):
  while True:
    try:
      int(x)
      if int(x) > 0:
        break
      else:
        print('cannot be less than zero or equals zero')
        return Enter(input('try again >'))  
    except ValueError:
      print('entered not numbers')
      return Enter(input('try again >'))
  return int(x)    


uprightStart = Enter(input('Upright Start >'))
horizontallyStart  = Enter(input('Horizontally Start >'))
print('-'*20)
uprightFinish = Enter(input('Upright Finish >'))
horizontallyFinish = Enter(input('Horizontally Finish >'))

if abs(uprightStart-uprightFinish) == abs(horizontallyStart-horizontallyFinish) or uprightStart == uprightFinish or horizontallyStart == horizontallyFinish or abs(uprightStart-uprightFinish)+abs(horizontallyStart-horizontallyFinish) > 3:
  print('NO')
else:
  print('YES')
input()

