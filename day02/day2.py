
def testReport(report):
    safe = True
    increasing = True
    # print(report)
    for i in range(1, len(report)):
        # The first time, establish if this is increasing or decreasing. 
        if i==1:
            increasing = (report[i-1] < report[i])
            # print(increasing)
        # If it's changed increasing or decreasing, no longer safe.
        # if the previous number is more than three away, no longer safe.
        # If the previous number is the same, no longer safe. 
        if (increasing != (report[i-1] < report[i]) or (abs(report[i-1] - report[i]) > 3) or (report[i-1] == report[i])):
            safe = False
    return safe

def trialUnsafeReportWithDampener(report):
    safe = False
    # If the report is unsafe, for each element in the array, try and remove it and retest.
    for i in range(0, len(report)):
        # [:] for a copy, instead of passing a reference
        dampenedReport = report[:]
        del dampenedReport[i]
        safe = testReport(dampenedReport)
        if safe:
            return True
    return False


reports = []

with open('day2.txt', 'r') as file:
    for line in file:
        # The following line takes one line of the file, converts it to an array of ints, 
        # and appends it to the larger 'reports' array to create 
        # a two-dimensional array of reports and levels
        reports.append(list(map(int, line.strip().split(' '))))

totalSafeReports = 0
for report in reports:
    safe = testReport(report=report)
    # print("First test:" + str(safe))
    if not safe:
        safe = trialUnsafeReportWithDampener(report=report)
        # print("Dampened: " + str(safe))
    if safe: 
        totalSafeReports = totalSafeReports + 1

print(totalSafeReports)

