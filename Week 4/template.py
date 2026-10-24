"""
RECORD CHECK  -  my version
===========================

Name  : Duaa Usman
Lane  : Cyber
Date  : 15.10.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== 
# FUNCTIONS

# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Calculate the difference, percentage, and status"""
    difference = value - limit
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print the record check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Used       : {value}")
    print(f"Total      : {limit}")
    print(f"Difference : {difference}")
    print(f"Percentage : {percent:.1f}%")
    print(f"Status     : {status}")
    print("=" * 34)

label = input("Enter name/hostname/IP: ")
value = float(input("Enter value: "))
limit = float(input("Enter total: "))

difference, percent, status = check_record(value, limit)

print_report(label, value, limit, difference, percent, status)

# ====================================================================== 
# STORE

# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}

records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 90.0, "limit": 100.0}]   


# =============================================================== 
# PROCESS + OUTPUT

# 3. Loop over records. For each one, call check_record and print_report.

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"])

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status)
