class A:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

inputs = input().split()
code, place, time = inputs

a1 = A(code, place, time)

print('secret code : {}'.format(a1.code))
print('meeting point : {}'.format(a1.place))
print('time : {}'.format(a1.time))