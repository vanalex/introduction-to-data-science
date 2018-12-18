import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile));

length = len(mpg);
print('print data ===>', mpg[:3]);

print('print data length ===>', length);

print('print data headers ===>', mpg[0].keys());

average_cty_fuel = sum(float(d['cty']) for d in mpg) / length;
print('average cty fuel =>', average_cty_fuel);

average_hwy_fuel = sum(float(d['hwy']) for d in mpg) / length;
print('average hwy fuel =>', average_hwy_fuel);

cylinders = set(d['cyl'] for d in mpg)
print('cylinders =>', cylinders);

CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key= lambda x: x[0]);
print('grouping the cars by number of cylinder, and finding the average cty mpg for each group ==>', CtyMpgByCyl);

vehicle_class = set(d['class'] for d in mpg)
print('vehicle classes ==>', vehicle_class);

HwyMpgByClass = []

for t in vehicle_class: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
print('the average hwy mpg for each class of vehicle ==> ',HwyMpgByClass);
