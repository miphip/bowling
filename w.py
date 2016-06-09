from rx import Observable
from rx.subjects import Subject

w_count = 0


def on_window(w):
    global w_count
    i = w_count
    w_count += 1
    w_name = 'w%d' % i
    w.subscribe(
        lambda v: print(w_name, v),
        lambda ex: print(w_name, ex),
        lambda: print(w_name, 'completed'))


source = Observable.interval(1000)
closer = Subject()

s = source.window(lambda: closer)

s.subscribe(on_window,
            lambda ex: print('source', ex),
            lambda: print('source completed'))

in_ = input('')
while in_ != 'exit':
    closer.on_next(0)
    in_ = input('')
