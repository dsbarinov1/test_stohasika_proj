import queue_ as qu

rooms = 10
days = 5
queue = qu.Queue(days=days, size=rooms)
print(queue.requests_served)
print(queue.spr)
print(queue.tac)
print(len(queue.tac))
print(len(queue.client_schedule))
print(queue.client_schedule)
# queue.draw_("tac")


'''for i in range(days):
    print(f"day N{i} number of free rooms: {queue.free_rooms_alt(i)}")
'''

# print(queue.profit)
