def next_item():
    yield "first"
    yield "second"


for c in next_item():
    print(c)
