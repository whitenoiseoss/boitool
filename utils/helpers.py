DEBUG = True
HEADER = """

  BoITool v0.1a by whitenoise

"""
GOODBYE = """

  Goodbye!

"""
ARCHIVE_TYPES = {
    0: 'Encrypted',
    1: 'Compressed',
    2: 'MiniZ'
}
COMMAND_PROMPT = "[BoITool] > "


def dprint(*args):
    if DEBUG:
        print(' '.join(args))

def errprint(*args):
    print("\n[ERROR] ", end="")
    print(' '.join(args))
    print("\n")


class ArchiveType(Enum):
    ENCRYPTED=0
    COMPRESSED=1
    MINIZ=2


class FileType(Enum):
    pass


class RecordType(Enum):
    pass

