"""Explicit byte interpretations. No IDA imports and no byte or semantic changes."""
from dataclasses import dataclass


@dataclass(frozen=True)
class IntegerFormat:
    width: int
    radix: int = 16
    signed: bool = False
    tagged: bool = False

    @property
    def name(self):
        return 'iosd_helper_be%d_%s_v1' % (self.width*8, 'ptr' if self.tagged else
                                         'signed' if self.signed else 'hex' if self.radix == 16 else 'dec')

    @property
    def label(self):
        return 'iosd: BE%d %s' % (self.width*8, 'tagged pointer (clear bit 63)' if self.tagged else
                                  'signed decimal' if self.signed else 'hex' if self.radix == 16 else 'unsigned decimal')

    def render(self, raw):
        if self.width not in (2, 4, 8) or len(raw) != self.width:
            raise ValueError('Select the exact 16/32/64-bit width; no implicit truncation')
        if self.tagged and (self.width != 8 or self.signed):
            raise ValueError('Tagged pointer decoding requires an unsigned 64-bit value')
        value = int.from_bytes(raw, 'big', signed=self.signed)
        if self.tagged:
            return 'IOSD_BE64_PTR(0x%016X)' % (value & 0x7fffffffffffffff)
        text = ('0x%0*X' % (self.width*2, value)) if self.radix == 16 else str(value)
        return 'BE%d%s(%s)' % (self.width*8, 's' if self.signed else '', text)


FORMATS = tuple(IntegerFormat(width, radix, signed) for width in (2, 4, 8)
                for radix, signed in ((16, False), (10, False), (10, True))) + (IntegerFormat(8, tagged=True),)


def literal_bytes(value, width, byteorder):
    """Reconstruct bytes of a user-selected C/assembly constant at its explicit width."""
    if width not in (2, 4, 8) or byteorder not in ('little', 'big'):
        raise ValueError('Unsupported width or byte order')
    mask = (1 << (width*8))-1
    # A cnumber can be sign-extended to 64 bits. Do not silently narrow other values.
    if value < -(1 << (width*8-1)) or (value > mask and
            (value | mask != (1 << 64)-1 or not value & (1 << (width*8-1)))):
        raise ValueError('Constant does not fit the selected width')
    return (value & mask).to_bytes(width, byteorder)


def append_notes(lines, notes, anchor_indices):
    """Append notes only to lines carrying the selected ctree item anchor, never text-match literals."""
    result = []
    for line in lines:
        matches = [notes[index] for index in dict.fromkeys(anchor_indices(line)) if index in notes]
        result.append(line + (' // iosd-view: ' + '; '.join(matches) if matches else ''))
    return result


def code_mask(text, in_block=False):
    """Visible C line mask: exclude strings, character literals and comments."""
    mask = [True]*len(text);i = 0;quote = None
    while i < len(text):
        if in_block:
            mask[i] = False
            if text.startswith('*/', i):
                mask[i:i+2] = [False, False];i += 2;in_block = False
            else:i += 1
        elif quote:
            mask[i] = False
            if text[i] == '\\' and i+1 < len(text):mask[i+1] = False;i += 2
            else:
                if text[i] == quote:quote = None
                i += 1
        elif text.startswith('//', i):
            mask[i:] = [False]*(len(text)-i);break
        elif text.startswith('/*', i):
            mask[i:i+2] = [False, False];in_block = True;i += 2
        elif text[i] in ('"', "'"):
            quote = text[i];mask[i] = False;i += 1
        else:i += 1
    return mask, in_block
