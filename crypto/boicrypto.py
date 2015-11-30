class BoICrypto(object):
    def __init__(self):
        pass

    def hash1(self, string):
        ret = 0x1505
        ba = bytearray(string, 'ascii')
        for i in range(0, len(string)):
            b = ba[i]
            if b <= 0x19:
                b += 0x20
            if b == 0x5c:
                b = 0x2f
            ret = ((ret << 5) + ret) + b

        return ret
