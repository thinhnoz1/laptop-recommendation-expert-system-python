# import json
# with open('data.json', 'w') as outfile:
#     json.dump({
#     "age":100,
#     "name":"mkyong.com",
#     "messages":["msg 1","msg 2","msg 3"]
#      }, outfile)

def test(bool):
    clock = 0
    if (bool == True):
        clock = 10
    else:
        clock = 5
    return clock

print(test(False))