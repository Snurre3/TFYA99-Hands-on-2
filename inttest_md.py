import md
import sys, unittest
from asap3 import Trajectory

md.run_md()

traj = Trajectory("cu.traj")

class MdTests(unittest.TestCase):
    def test_traj(self):
        self.assertNotEqual(len(traj), 0)
        
        
        
if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())

