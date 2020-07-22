from crccheck.crc import ALLCRCCLASSES

head = """\
Supported CRCs
==============

+-------------------------+-----------------+-----------+----------------------------+----------------------+---------------+----------------+----------------------+------------------------+---------------------------+
|  CRC Name               | Class           | Bit width | Poly                       | Initvalue            | Reflect input | Reflect output | XOR output           | Check                  | Residue                   |
+=========================+=================+===========+============================+======================+===============+================+======================+========================+===========================+
"""

template = """\
| {c._crcname: <23} | {c.__name__: <15} | {c._width!s: <9} | 0x{c._poly: <24} | 0x{c._initvalue: <18x} | {c._reflect_input!s: <13} | {c._reflect_output!s: <14} | 0x{c._xor_output: <18x} | 0x{c._check_result: <20x} | 0x{c._residue: <23x} |
+-------------------------+-----------------+-----------+----------------------------+----------------------+---------------+----------------+----------------------+------------------------+---------------------------+
"""

for c in ALLCRCCLASSES:
    c._crcname = c.__doc__.splitlines()[0]

print(head, end='')
print("".join(template.format(c=c) for c in ALLCRCCLASSES))
