import unittest
from cyclecount.engine import WarehouseCycleCountEngine, StockBinItem, BlindCountScan

class TestWarehouseCycleCount(unittest.TestCase):
    def test_class_a_strict_tolerance_breach(self):
        engine = WarehouseCycleCountEngine()

        # Class A item: 100 units expected at ₹5,000 each = ₹5,00,000 value. 0.5% tolerance = 0.5 units
        item = StockBinItem(
            item_code="CPU-INTEL-I9",
            warehouse_bin="BIN-A1-04",
            abc_classification="A",
            book_system_quantity=100.0,
            unit_cost_inr=5000.0
        )

        # Physical count found 98 units (2 units missing > 0.5 unit tolerance)
        scan = BlindCountScan(
            item_code="CPU-INTEL-I9",
            warehouse_bin="BIN-A1-04",
            physically_counted_qty=98.0,
            auditor_employee_id="AUD-09"
        )

        res = engine.audit_cycle_count(item, scan)
        self.assertEqual(res.variance_quantity, -2.0)
        self.assertEqual(res.variance_cost_impact_inr, 10000.0)
        self.assertFalse(res.is_variance_within_tolerance)
        self.assertTrue(res.requires_manager_write_off_approval)
        self.assertEqual(res.status, "MAJOR_SHRINKAGE_WRITE_OFF_REQUIRED")

if __name__ == "__main__":
    unittest.main()
