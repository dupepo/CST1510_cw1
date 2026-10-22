"""
RECORD CHECK  -  my version
===========================

Name  : Duaa Usman
Lane  : Cyber
Date  : 22.10.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== 
# CLASS
# 1. Define a class called Record.

class Record:
    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return the value as a percentage of the limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return the status based on the percentage."""
        percentage = self.percent()
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

r1 = Record("R-001", 80.0, 100.0)
print(r1.status())

# ==================================================================== 
# RECORDS
# 2. Create your records.

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 45.0, 100.0)]

for record in records:
    print(record.label, record.status())

# ==================================================================== 
# OUTPUT
# 3. Print a report for each record.

over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label      : {record.label}")
    print(f"  Value      : {record.value}")
    print(f"  Limit      : {record.limit}")
    print(f"  Percentage : {record.percent():.1f}%")
    print(f"  Status     : {record.status()}")

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {over_limit_count}")

