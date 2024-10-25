calls = 0

def count_calls(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(name1):
    tuple = len(name1), name1.upper(), name1.lower()
    print(tuple)

@count_calls
def is_contains(name2, list_):
     flag = True
     if name2.lower() in [x.lower() for x in list_]:
         flag = True
     else:
         flag = False
     print(flag)

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])

print(calls)