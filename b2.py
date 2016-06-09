from rx import Observable, Observer
from rx.internal import extensionmethod
from rx.subjects import Subject

in_ = '23432/XX428/X218-'


def dump(s):
    print()
    s.subscribe(print, print, print)


CHAR2NUM = {str(i): i for i in range(1, 9)}
CHAR2NUM['-'] = 0
CHAR2NUM['X'] = 10

s1 = Observable.from_(in_)

s1.window



s2 = s1.scan(lambda prev, x: 10 - prev if x == '/' else CHAR2NUM[x], 0)
s3 = s2.start_with(0).buffer_with_count(4, 1)
s4 = s3.map(lambda q: dict(s=q[0]+q[1], spare=q[1]+q[2], strike=q[1]+q[2]+q[2]))
