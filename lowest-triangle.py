def lowestTriangle(base, area):
    if ((2*area) % base) == 0:
        return (2*area) / base
    else:
        return ((2*area) / base) + 1

base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)