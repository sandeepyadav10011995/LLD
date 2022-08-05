"""
Employee Class Tests
"""
import unittest

from employee import Employee


NAME: str = "Sandeep"
EMPLOYEE_ID: int = 12345


class TestEmployeeComputePayout(unittest.TestCase):
    """ Test the compute_payout method of the Employee class. """

    def setUp(self) -> None:
        """ Set up test fixtures."""
        self.sandeep = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_return_a_float(self):
        """Whether payout returns a float."""
        self.assertIsInstance(self.sandeep.compute_payout(), float)

    def test_employee_payout_no_commission_no_hour(self):
        """Whether payout is correctly computed in case of no commission and no hours worked."""
        self.assertAlmostEqual(self.sandeep.compute_payout(), 1000.0)

    def test_employee_payout_no_commission(self):
        """Whether payout is correctly computed in case of no commission and no hours worked."""
        self.sandeep.hours_worked = 10.0
        self.assertAlmostEqual(self.sandeep.compute_payout(), 2000.0)

    def test_employee_payout_with_commission(self):
        """Whether payout is correctly computed in case of 10 contracts and 10 hours worked."""
        self.sandeep.hours_worked = 10.0
        self.sandeep.contracts_landed = 10
        self.assertAlmostEqual(self.sandeep.compute_payout(), 3000.0)

    def test_employee_payout_with_commission_disabled(self):
        """
        Whether payout is correctly computed in case of 10 contracts and 10 hours worked but commission is
        disabled.
        """
        self.sandeep.hours_worked = 10.0
        self.sandeep.contracts_landed = 10
        self.sandeep.has_commission = False
        self.assertAlmostEqual(self.sandeep.compute_payout(), 2000.0)


if __name__ == "__main__":
    unittest.main()
