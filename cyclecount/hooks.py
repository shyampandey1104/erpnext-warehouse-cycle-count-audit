# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "cyclecount"
app_title = "Erpnext Warehouse Cycle Count Audit"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Warehouse Cycle Count Audit for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/cyclecount/css/cyclecount.bundle.css"
app_include_js = "/assets/cyclecount/js/cyclecount.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "cyclecount.engine.on_document_submit",
        "on_cancel": "cyclecount.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "cyclecount.engine.daily_scheduled_sync"
    ]
}
