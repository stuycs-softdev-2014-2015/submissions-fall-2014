FILENAME = 'School_Attendance_and_Enrollment_Statistics_by_District__2010-11_.csv'


def read_attendance_data():
    return read_data(FILENAME)


def read_data(filename):
    data = []

    for line in open(filename).readlines():
        values = line.strip().split(",")
        data.append(values)

    data.pop(0)

    for entry in data:
        entry[1] = float(entry[1].split("%")[0])
        entry[2] = int(entry[2])

    return data


def sort_data(data, order):
    if order.split("-")[0] == "attendance":
        sort_column = 1
    elif order.split("-")[0] == "enrollment":
        sort_column = 2
    else:
        return data

    lookup_dict = {entry[sort_column]: data.index(entry) for entry in data}
    sorted_keys = sorted(lookup_dict.keys())

    if order.split("-")[1] == "desc":
        sorted_keys.reverse()

    return [data[lookup_dict[key]] for key in sorted_keys]


def find_facts(data):
    return {'enrollment-high': findMax(data), 'enrollment-low': findMin(data),
            'attendance-high': findMaxPercent(data),
            'attendance-low': findMinPercent(data)}


def findMax(l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) - 1)
    return max(new)


def findMin(l):
    new = []
    for i in l:
        new.append(int(i[2]))
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return min(new)


def findMaxPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return max(new)


def findMinPercent(l):
    new = []
    for i in l:
        new.append(i[1])
    new.pop(len(new) - 1)
    new.pop(len(new) - 1)
    return min(new)
