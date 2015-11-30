class Archive(object):
    def __init__(self, path):
        self.path = path
        self.home = os.path.dirname(self.path)
        self.filename = os.path.basename(self.path)
        self.name = self.filename[:-2]
        dprint(" - Loading archive:", self.name)
        self.resources = []
        self.headers = []
        self.inspect()
        self.create_resources()

    def inspect(self):
        self.file_bytes = open(self.path, 'rb').read()
        header = struct.unpack("<7sBih", self.file_bytes[0:14])
        self.signature = header[0].decode('ascii')
        dprint("    - Signature:", self.signature)
        if self.signature == "ARCH000":
            dprint("        - Signature OK")
        else:
            dprint("    - Bad Signature")
            exit(1)
        self.archive_type = header[1]
        dprint("    - Archive type:", ARCHIVE_TYPES[self.archive_type])
        self.offset = header[2]
        dprint("    - Offset:", str(self.offset))
        self.record_count = header[3]
        dprint("    - Record count:", str(self.record_count))
        self.size = len(self.file_bytes)
        dprint("    - Size:", str(len(self.file_bytes)))

    def create_resources(self):
        self.header_bytes = self.file_bytes[self.offset:]
        h = struct.iter_unpack("<IIIII", self.header_bytes)

        for header in h:
            self.headers.append(header)

        dprint("    - Headers:", str(len(self.headers)))
        if len(self.headers) == self.record_count:
            dprint("        - Headers OK")
        else:
            print("    - Header read malfunctioned")
            exit(1)

        for index, header in enumerate(self.headers):
            if self.archive_type == 0:
                self.resources.append(EncryptedResource(self.headers[index]))
            elif self.archive_type == 1:
                self.resources.append(CompressedResource(self.headers[index]))
            else:
                self.resources.append(MiniZResource(self.headers[index]))
