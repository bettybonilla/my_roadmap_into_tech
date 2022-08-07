def valentine(person1, person2):
  leading_whitespace = range(0,4)[::-1] +[0]+range(0,8)
  inside = [3,5,14,14] + range(0,15)[::-1][::2]
  layers = ["  ___    ___",r" /   \  /   \ ",r'/     \/     \ ','|             |']
  for i in range(5,12):
    layers.append(' ' * leading_whitespace[i] + '\\' + ' ' * inside[i] + '/')
  #inserts person1 into layers[4]
  temp = []
  for char in layers[3]: temp.append(char)
  temp[1:len(person1) + 1] = person1
  layers[3] = ''.join(temp)

  temp = []
  layers[4] = '|      +     |'

  # do that again for person2
  for char in layers[5]: 
    temp.append(char)

  temp[-len(person2)-1:-1] = person2
  layers[5] = ''.join(temp)

  print '\n'.join(layers)

valentine('Marc', 'Betty')