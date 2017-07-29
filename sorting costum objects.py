from operator import attrgetter


class user:
    def __init__(self,x,y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    user('bucky',32),
    user('sally', 2),
    user('tunee', 353),
    user('brayan', 7),
    user('jodee', 96),
    user('amandoo', 20)
]

for user in users:
    print(user)

print('________________')
for user in sorted(users, key=attrgetter('user_id')):
    print(user)