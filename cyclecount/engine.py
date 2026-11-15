"""Perpetual Warehouse ABC Cycle Counting, Blind Barcode Audit & Shrinkage Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class StockBinItem:
    item_code: str
    warehouse_bin: str
    abc_classification: str  # A, B, C
    book_system_quantity: float
    unit_cost_inr: float


@dataclass
class BlindCountScan:
    item_code: str
    warehouse_bin: str
    physically_counted_qty: float
    auditor_employee_id: str


@dataclass
class DiscrepancyAuditReport:
    item_code: str
    warehouse_bin: str
    book_qty: float
    physical_qty: float
    variance_quantity: float
    variance_cost_impact_inr: float
    is_variance_within_tolerance: bool
    requires_manager_write_off_approval: bool
    status: str  # ACCURATE, MINOR_TOLERANCE_ACCEPTED, MAJOR_SHRINKAGE_WRITE_OFF_REQUIRED


class WarehouseCycleCountEngine:
    """Automates continuous warehouse cycle counting without shutting down operations."""

    # Percentage tolerance thresholds
    TOLERANCE_PCT_CLASS_A = 0.5   # 0.5% tolerance on high-value items
    TOLERANCE_PCT_CLASS_B = 1.0   # 1.0% tolerance
    TOLERANCE_PCT_CLASS_C = 2.5   # 2.5% tolerance on bulk fasteners/cables

    def audit_cycle_count(
        self,
        system_bin: StockBinItem,
        scan: BlindCountScan
    ) -> DiscrepancyAuditReport:
        variance_qty = round(scan.physically_counted_qty - system_bin.book_system_quantity, 2)
        variance_cost = round(abs(variance_qty) * system_bin.unit_cost_inr, 2)

        tol_pct = {
            "A": self.TOLERANCE_PCT_CLASS_A,
            "B": self.TOLERANCE_PCT_CLASS_B,
            "C": self.TOLERANCE_PCT_CLASS_C
        }.get(system_bin.abc_classification, 1.0)

        max_allowed_variance_qty = (system_bin.book_system_quantity * tol_pct) / 100.0

        if variance_qty == 0.0:
            status = "ACCURATE"
            within_tol = True
            req_approval = False
        elif abs(variance_qty) <= max_allowed_variance_qty:
            status = "MINOR_TOLERANCE_ACCEPTED"
            within_tol = True
            req_approval = False
        else:
            status = "MAJOR_SHRINKAGE_WRITE_OFF_REQUIRED"
            within_tol = False
            req_approval = True

        return DiscrepancyAuditReport(
            item_code=system_bin.item_code,
            warehouse_bin=system_bin.warehouse_bin,
            book_qty=system_bin.book_system_quantity,
            physical_qty=scan.physically_counted_qty,
            variance_quantity=variance_qty,
            variance_cost_impact_inr=variance_cost,
            is_variance_within_tolerance=within_tol,
            requires_manager_write_off_approval=req_approval,
            status=status
        )
