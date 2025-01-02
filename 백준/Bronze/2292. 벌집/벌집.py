n=int(input())

room=1
layer=1

while n>room:
    room+=6*layer
    layer+=1
print(layer)