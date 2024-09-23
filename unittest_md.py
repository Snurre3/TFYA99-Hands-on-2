import sys, unittest
from md import calcenergy
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                            symbol="Cu",
                            size=(3, 3, 3),
                            pbc=True)
        atoms.calc = EMT()
        length = len(atoms)
        epot, ekin, temp, etot = calcenergy(atoms)

        self.assertAlmostEqual(ekin, atoms.get_kinetic_energy()/length)
        self.assertAlmostEqual(epot, atoms.get_potential_energy()/length)
        self.assertAlmostEqual(etot, (atoms.get_potential_energy() + atoms.get_kinetic_energy())/length)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())