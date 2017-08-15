from progressbar import ProgressBar, Bar, ETA, Percentage


__step = None


def get_step():
    global __step
    return __step


def probar(iterable):
    global __step
    if isinstance(iterable, range):
        total = (a.stop - a.start) / a.step
    elif hasattr(iterable, "__len__"):
        total = len(iterable)
    else:
        total = None
    __step = 0
    bar = ProgressBar(widgets=[Percentage(), Bar(), ETA()])
    bar.start(maxvalue=total)
    for data in iterable:
        bar.update(__step)
        yield data
        __step += 1
    bar.finish()
