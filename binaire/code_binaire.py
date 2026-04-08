from .bit import Bit

class CodeBinaire:
    def __init__(self, bit: Bit, *bits: Bit):
        self._bits = [bit] + list(bits)

    @property
    def bits(self):
        return tuple(self._bits)

    def ajouter(self, bit: Bit):
        self._bits.append(bit)

    def __len__(self):
        return len(self._bits)

    def __add__(self, autre):
        if not isinstance(autre, CodeBinaire):
            raise TypeError("L'objet à ajouter doit être une instance de CodeBinaire.")
        return CodeBinaire(*self._bits, *autre._bits)

    def __getitem__(self, item):
        if isinstance(item, slice):
            sliced_bits = self._bits[item]
            if sliced_bits:
                return CodeBinaire(*sliced_bits)
            return None
        return self._bits[item]

    def __setitem__(self, key, value):
        temp_bits = self._bits.copy()

        if isinstance(key, slice):
            if isinstance(value, CodeBinaire):
                temp_bits[key] = value._bits
            else:
                temp_bits[key] = list(value)
        else:
            temp_bits[key] = value

        self._bits = temp_bits

    def __delitem__(self, key):
        temp_bits = self._bits.copy()
        del temp_bits[key]
        self._bits = temp_bits

    def __iter__(self):
        return iter(self._bits)

    def __eq__(self, autre):
        if not isinstance(autre, CodeBinaire):
            return False
        return self._bits == autre._bits

    def __str__(self):
        return "".join(str(b) for b in self._bits)

    def __repr__(self):
        args = ", ".join(repr(b) for b in self._bits)
        return f"CodeBinaire({args})"