
import os, sys
import ase.io as fio
import ase.db as db
from gocia.interface import Interface
from gocia.utils import visualize

# $ python plotBS.py asym-4l.vasp Ga3N3.vasp
# # Timing: 1.5786 s, ~10% slower than CPK
subsName = sys.argv[1]
surfName = sys.argv[2]
baseName = surfName.split('/')[-1].split('.')[0]

surf = Interface(
    tags = baseName,
    subAtoms = fio.read(subsName),
    allAtoms = fio.read(surfName),
    )
visualize.drawBSsurf(
    surf,
    pseudoBond=True,
    outName=baseName
    )
