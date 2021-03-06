import os, sys
from ase.db import connect
from gocia.utils.dbio import get_traj

def opt_xtb_lbfgs(atoms):
    from xtb.ase.calculator import XTB
    from ase.optimize.lbfgs import LBFGS
    tmpAtoms = atoms.copy()
    tmpAtoms.calc = XTB(method='GFN1-xTB')
    geomOpt = LBFGS(tmpAtoms, maxstep=0.1,
	trajectory=None,
#	logfile=None
	)
    geomOpt.run(fmax=0.05, steps=400)
    return tmpAtoms


inpName = sys.argv[1]
oldDB = connect(inpName)
traj = get_traj(oldDB.select())

newDB = connect('out-'+inpName, append=False)
for i in range(len(traj)):
    print('Optimizing\t%i/%i'%(i+1, len(traj)))
    opt = opt_xtb_lbfgs(traj[i])
    newDB.write(opt, eV=opt.get_potential_energy(), mag=0)


