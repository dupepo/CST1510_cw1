"""
RECORD CHECK  -  my version
===========================

Name  : Duaa Usman
Lane  : Cyber 
Date  : 08.10.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent, warning_at=90):
     if percent >= 100:
        return "OVER LIMIT"
     elif percent >= warning_at:
        return "WARNING"
     else:
        return "OK"

print(status_of(95))         

label = input("Enter name/hostname/IP: ")     
value = float(input("Enter value: "))     
limit = float(input("Enter total: "))     

difference = value - limit   
percent = (value / limit) * 100     
status = status_of(percent)        

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Used : {value}")
print(f"Total : {limit}")
print(f"Status : {status}")

print("=" * 34)
