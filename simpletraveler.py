import random
#Bidimensional Random route building
route = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
              [0,0],[0,0],[0,0],[0,0]]
for i in range(10):
     for j in range(2):
          x = random.randint(1, 10)
          route[i][j] = x
print(route)
#Remove duplicated coordenates func
#Finding linear short interroute
#Finding metatype for decision problem