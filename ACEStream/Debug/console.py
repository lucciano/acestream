#Embedded file name: ACEStream\Debug\console.pyo
import sys

class SafePrintStream:

    def __init__(self, stream):
        self._stream = stream

    def write(self, arg):
        try:
            self._stream.write(arg.encode('ASCII', 'backslashreplace'))
        except Exception as e:
            try:
                s = u'{%s}' % repr(arg)
                self._stream.write(s)
            except:
                self._stream.write('ACEStreamConsole: ERROR printing\n')
                self._stream.write(repr(e))
                self._stream.write('\n')

    def flush(self):
        self._stream.flush()

    def fileno(self):       
        return self._stream.fileno()


class SafeLinePrintStream:

    def __init__(self, stream):
        self._stream = stream
        self._parts = []

    def write(self, arg):
        self._parts.append(arg.encode('ASCII', 'backslashreplace'))
        if arg == '\n':
            self._stream.write(''.join(self._parts))
            self._parts = []

    def flush(self):
        self._stream.write(''.join(self._parts))
        self._parts = []
        self._stream.flush()


sys.stderr = SafePrintStream(sys.stderr)
sys.stdout = sys.stderr
