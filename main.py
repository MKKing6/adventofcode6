input = open("input.txt").readlines()

# product = 1

# time = input[0].split(":")[1].split()
# distance = input[1].split(":")[1].split()

# for race in range(len(time)):
#   win = 0
#   for hold in range(int(time[race])):
#     if (hold + 1) * (int(time[race]) - (hold + 1)) > int(distance[race]):
#       win += 1
#   product *= win
# print(product)

time = "".join(input[0].split(":")[1].split())
distance = "".join(input[1].split(":")[1].split())

win = 0
for hold in range(int(time)):
  if (hold + 1) * (int(time) - (hold + 1)) > int(distance):
    win += 1
print(win)