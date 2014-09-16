FILENAME = 'School_Attendance_and_Enrollment_Statistics_by_District__2010-11_.csv'


def read_attendance_data():
    return read_data(FILENAME)


def read_data(filename):
    data = []

    for line in open(filename).readlines():
        values = line.strip().split(",")
        data.append(values)

    return data
