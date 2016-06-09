from rx.subjects import Subject

from dumper import Dumper

left = Subject()
right = Subject()
left_duration_selectors = {}
right_duration_selectors = {}


def left_duration_selector(v):
    s = Subject()
    left_duration_selectors[v] = s
    return s


def right_duration_selector(v):
    s = Subject()
    right_duration_selectors[v] = s
    return s


def result_selector(left_v, r_obs):
    #right_values = []
    #r_obs.subscribe(lambda v: right_values.append(v))
    return left_v, r_obs


def result_dumper(pair):
    pair[1].subscribe(Dumper('result left=%s' % pair[0]))


left \
    .group_join(right,
                left_duration_selector,
                right_duration_selector,
                result_selector) \
    .subscribe(result_dumper)

in_ = input('')
while in_ != 'exit':
    parts = in_.split()
    if parts[0] == 'l':
        left.on_next(parts[1])
    if parts[0] == 'r':
        right.on_next(parts[1])
    if parts[0] == 'lds':
        left_duration_selectors[parts[1]].on_completed()
    if parts[0] == 'rds':
        right_duration_selectors[parts[1]].on_completed()
    in_ = input('')
left.on_completed()
