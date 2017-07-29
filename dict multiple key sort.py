from operator import itemgetter

users =[
    {'first_name': 'andi', 'last_name': ' ado'},
    {'first_name': 'aadv', 'last_name': ' fsoite'},
    {'first_name': 'adsuuu', 'last_name': 'odidu'},
    {'first_name': 'toeri', 'last_name': ' zminom'},
    {'first_name': 'ovre', 'last_name': ' ovmri'},
    {'first_name': 'oapvesr', 'last_name': ' dsouv'},
    {'first_name': 'ocsaf', 'last_name': ' puteo'},
    {'first_name': 'urekga', 'last_name': ' tretyi'}

]

for x in sorted(users, key=itemgetter('first_name')):
    print(x)
    print('____________________')

for x in sorted(users, key=itemgetter('first_name','last_name')):
    print(x)