# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "cyclecount"
app_title = "Erpnext Warehouse Cycle Count Audit"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Warehouse Cycle Count Audit - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/cyclecount/css/cyclecount.bundle.css"
app_include_js = "/assets/cyclecount/js/cyclecount.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Warehouse Cycle Count Audit Entry": {
        "validate": "cyclecount.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "cyclecount.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "cyclecount.tasks.hourly_sync"
    ],
    "daily": [
        "cyclecount.tasks.daily_reconciliation"
    ],
    "weekly": [
        "cyclecount.tasks.weekly_digest"
    ]
}
