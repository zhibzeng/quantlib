from contextlib import contextmanager
from itertools import starmap


class HTML:
    """用上下文管理器生成HTML文档

    Example
    -------
    ..  code-block:: python

        doc = HTML()
        with doc.html():
            with doc.head():
                doc.inline("titile", _text="Generated HTML")
            with doc.body():
                with doc.div(_class="container"):
                    with doc.div(_class="row"):
                        doc.inline("p", _text="paragraph")
        html = doc.render()
    """
    def __init__(self):
        self.docstring = []
        self.level = 0

    def text(self, txt):
        self.print(txt)

    def inline(self, tag, **kwargs):
        if "_class" in kwargs:
            kwargs["class"] = kwargs["_class"]
            del kwargs["_class"]
        try:
            text = kwargs["_text"]
            del kwargs["_text"]
        except KeyError:
            text = ""
        attributes = ' '.join(starmap(lambda k, v: "%s=%s" % (k, v), kwargs.items()))
        if attributes:
            self.print('<%s %s>%s</%s>' % (tag, attributes, text, tag))
        else:
            self.print('<%s>%s</%s>' % (tag, text, tag))

    def __getattr__(self, item):
        assert isinstance(item, str)
        @contextmanager
        def wrapped(**kwargs):
            if "_class" in kwargs:
                kwargs["class"] = kwargs["_class"]
                del kwargs["_class"]
            for k, v in kwargs.items():
                if isinstance(v, str):
                    kwargs[k] = '"%s"' % v
                else:
                    kwargs[k] = str(v)
            tag_name = item
            attributes = ' '.join(starmap(lambda k, v: "%s=%s" % (k, v), kwargs.items()))
            if attributes:
                self.print('<%s %s>' % (tag_name, attributes))
            else:
                self.print('<%s>' % tag_name)
            self.level += 1
            yield
            self.level -= 1
            self.print('</%s>' % tag_name)
        return wrapped

    def print(self, source):
        prefix = ' ' * (2 * self.level)
        self.docstring.append(prefix + source)

    def render(self):
        return "\n".join(self.docstring)
