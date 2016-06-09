from rx import Observable, Observer

in_ = '23432/XX428/X218-'


def dump(s):
    print()
    s.subscribe(print, print, print)


CHAR2NUM = {str(i): i for i in range(1, 9)}
CHAR2NUM['-'] = 0
CHAR2NUM['X'] = 10

s1 = Observable.from_(in_)
s2 = s1.scan(lambda prev, x: 10 - prev if x == '/' else CHAR2NUM[x], 0)
s3 = s2.start_with(0).buffer_with_count(4, 1)
s4 = s3.map(lambda q: dict(s=q[0]+q[1], spare=q[1]+q[2], strike=q[1]+q[2]+q[2]))

#s4 = s1.zip(s3, lambda ch, quad: (ch, quad))
def calc(ch, prev, cur, next, nextnext):
    if ch == 'X':
        return Observable.from_([cur + next + nextnext])
    if ch == '/':
        return Observable.from_([cur + next])


#s5 = s4.flat_map(lambda x: calc(x[0], x[1][0], x[1][1], x[1][2], x[1][3]))

#dump(s5)
#dump(s1.zip(s4, lambda a, b: (a,b)))

f_in = s1
frame_result = f_in.sca

frame_results = Observable.from_([5,7,20,24,16,6,20,13,3,8])

frame_sums = frame_results.scan(lambda acc, x: acc + x)
#dump(frame_sums)

end_result = frame_sums.last()
dump(end_result)
