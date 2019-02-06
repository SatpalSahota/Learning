sandwich_orders = ['pastrami', 'tuna mayo',
                   'pastrami', 'pastrami' 'cheese salad', 'ham salad']

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making = sandwich_orders.pop()
    finished_sandwiches.append(making)

for sandwich in finished_sandwiches:
    print("Your " + sandwich.title() + " is ready!")
