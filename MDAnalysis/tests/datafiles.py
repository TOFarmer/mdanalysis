"""
Location of data files for the MDAnalysis unit tests
====================================================

Real MD simulation data are stored in the ``data/`` sub
directory. Use as ::

  from MDAnalysis.tests.datafiles import *

"""
__all__ = ["PSF", "DCD",                        # CHARMM
           "PDB_small",                         # PDB
           "PDB", "GRO", "XTC", "TRR", "TPR",   # Gromacs
           "XYZ", "XYZ_bz2" ,                   # XYZ
           "CRD",                               # CRD
           "PRM", "TRJ", "TRJ_bz2",             # Amber (no periodic box)
           "PRMpbc", "TRJpbc_bz2",              # Amber (periodic box)
           ]

from pkg_resources import resource_filename

PSF = resource_filename(__name__, 'data/adk.psf')
DCD = resource_filename(__name__, 'data/adk_dims.dcd')
DCD_empty = resource_filename(__name__, 'data/empty.dcd')
CRD = resource_filename(__name__, 'data/adk_open.crd')

PDB_small = resource_filename(__name__, 'data/adk_open.pdb')

GRO = resource_filename(__name__, 'data/adk_oplsaa.gro')
PDB = resource_filename(__name__, 'data/adk_oplsaa.pdb')
XTC = resource_filename(__name__, 'data/adk_oplsaa.xtc')
TRR = resource_filename(__name__, 'data/adk_oplsaa.trr')
TPR = resource_filename(__name__, 'data/adk_oplsaa.tpr')

XYZ_psf = resource_filename(__name__, 'data/2r9r-1b.psf')
XYZ_bz2 = resource_filename(__name__, 'data/2r9r-1b.xyz.bz2')
XYZ = resource_filename(__name__, 'data/2r9r-1b.xyz')

PRM = resource_filename(__name__, 'data/ache.prmtop')
TRJ = resource_filename(__name__, 'data/ache.mdcrd')
TRJ_bz2 = resource_filename(__name__, 'data/ache.mdcrd.bz2')

PRMpbc = resource_filename(__name__, 'data/capped-ala.prmtop')
TRJpbc_bz2 = resource_filename(__name__, 'data/capped-ala.mdcrd.bz2')
