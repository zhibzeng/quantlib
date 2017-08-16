import tensorboard as tb
import tensorboard.embedding as te
from ..common.settings import CONFIG
from . import get_step


__writer = None


def get_writer():
    global __writer
    if __writer is None:
        __writer = tb.SummaryWriter(CONFIG.get("TB_LOGDIR", "."))
    return __writer


def add_histogram(name, value):
    step = get_step()
    writer = get_writer()
    writer.add_histogram(name, value, step)
    return value


def add_scalar(name, value):
    step = get_step()
    writer = get_writer()
    writer.add_scalar(name, value, step)
    return value


def add_text(name, value):
    step = get_step()
    writer = get_writer()
    writer.add_text(name, value, step)
    return value


def add_image(name, value):
    step = get_step()
    writer = get_writer()
    writer.add_image(name, value, step)
    return value


def add_embedding(mat, metadata=None, label_img=None):
    writer = get_writer()
    path = writer.file_writer.get_logdir()
    te.add_embedding(mat, path, metadata, label_img)
    return mat
