import re


class FragmentMeta(type):
    registry = []
    default = None

    def __new__(cls, name, bases, namespace, **kwds):
        marker_pattern = namespace.pop('marker_pattern', None)
        default = namespace.pop('default', False)
        accepts_breaks = namespace.pop('accepts_breaks', False)

        result = type.__new__(cls, name, bases, namespace)
        result.accepts_breaks = property(lambda self: accepts_breaks)
        if marker_pattern:
            marker_re = re.compile(marker_pattern)
            result.isendmarker = staticmethod(lambda line: marker_re.match(line) is not None)
            cls.registry.append((marker_re, result))
        elif not accepts_breaks:
            marker_re = re.compile('^\s*\n$')
            result.isendmarker = staticmethod(lambda line: marker_re.match(line) is not None)
        else:
            result.isendmarker = staticmethod(lambda line: False)
        if default:
            cls.default = result
        return result

    @classmethod
    def make(cls, line):
        for marker_pattern, result in cls.registry:
            match = marker_pattern.match(line)
            if match:
                return result(*match.groups())
        return cls.default(line)


class Fragment(object):
    def __init__(self):
        self.acc = []
        self.text = ''

    def append(self, line):
        self.acc.append(line)

    def finalize(self):
        self.text = ''.join(self.acc)
        del self.acc
        return self

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class TextFragment(Fragment, metaclass=FragmentMeta):
    default = True

    def __init__(self, line):
        super().__init__()
        self.append(line)


class CodeFragment(Fragment, metaclass=FragmentMeta):
    marker_pattern = '^```(.*)$'
    accepts_breaks = True

    def __init__(self, language):
        super().__init__()
        self.language = language

    def __repr__(self):
        return '```{0}\n{1}```'.format(self.language, super().__repr__())
