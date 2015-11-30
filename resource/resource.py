from abc import ABCMeta, abstractmethod


class Resource:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.data_start = 0
        self.data_length = 0
        self.data = ""

    @abstractmethod
    def unpack(self):
        raise NotImplementedError()


class EncryptedResource(Resource):
    def __init__(self, headers):
        self.filename_checksum = headers[0]
        self.encryption_key = headers[1]
        self.data_start = headers[2]
        self.data_length = headers[3]
        self.data_checksum = headers[4]

    def unpack(self):
        pass


class CompressedResource(Resource):
    def __init__(self, headers):
        self.filename_checksum1 = headers[0]
        self.filename_checksum2 = headers[1]
        self.data_start = headers[2]
        self.data_length = headers[3]
        self.data_checksum = headers[4]

    def unpack(self):
        pass


class MiniZResource(Resource):
    def __init__(self, headers):
        pass

    def unpack(self):
        pass

