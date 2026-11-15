# ERPNext Perpetual Warehouse Cycle Count & Shrinkage Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![WMS](https://img.shields.io/badge/Logistics-Perpetual%20Cycle%20Count-blue.svg)](https://frappe.io)

Eliminates disruptive annual warehouse shutdowns through continuous ABC velocity blind cycle counting, tolerance enforcement, and stock shrinkage write-off reconciliation.

## Features
- **Blind Counting Scan:** Auditors verify physical stock via mobile barcode scanning without viewing book inventory balances.
- **ABC Tolerance Matrix:** Automatically accepts minor tolerances for Class C goods while enforcing strict limits on Class A assets.
- **Automated Stock Reconciliation:** Triggers supervisor approval workflows and write-off journals for shrinkage breaches.

## Tests
```bash
python3 -m unittest discover tests
```
