thickness = int(input())
c = 'T'

# Top bar
for i in range((thickness)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillar
for i in range(thickness + 5):
    print((c*thickness).center(thickness*6))