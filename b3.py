from dumper import Dumper
from rx import Observable, Observer
from rx.internal import extensionmethod
from rx.subjects import Subject

in_ = '23432/XX428/X21X71'



Observable.from_(in_) \
    .flat_map(lambda q: Observable.range(1, 2) if q == 'X' else Observable.just(q)) \
    .buffer_with_count(2) \
    .map(lambda x, i: i) \
    .take(10) \
    .subscribe(Dumper('s'))
