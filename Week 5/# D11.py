# D11

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        if self.value > self.limit:
            return "Exceeded"
        else:
            return "Within limit"


def load_records(path):
    records = []

    with open(path, 'r') as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records


with open('final.txt', 'w') as x:
    x.write('R-001,87,100\n')
    x.write('R-002,120,100\n')
    x.write('R-003,45,100\n')


records = load_records("final.txt")

for record in records:
    print(record.label, record.status())
