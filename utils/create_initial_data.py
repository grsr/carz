import sqlite3
con = sqlite3.connect('cars.sqlite3')
cur = con.cursor()
cur.execute('SELECT * FROM car')
cols = """car
variant
img_url
average_mpg
co2_emissions_combined
co2_tax_band
road_tax_year_1
road_tax_annual
insurance_group
warranty_duration
engine_size
fuel
gearbox
top_speed
tank_range
nought_to_sixty
max_power
max_torque
body_type
length
width
height
seats
luggage_capacity_seats_up
luggage_capacity_seats_down
price""".split('\n')

colnames = ','.join(cols)

template = "INSERT INTO picker_car ({0}) VALUES ({1});"

def quote(s):
    if s is None:
        return 'NULL'
    else:
        return "'"+s.replace("'", "")+"'"

def check_units(val, units):
    if not val:
        return 'NULL'
    elif units in val:
        return n(val.split(' ')[0])
    else:
        raise Exception("unrecognised units: for {0}, looking for {1}".format(val, units))

def n(v):
    if not v or v == '-':
        return 'NULL'
    else:
        return v

for row in cur.fetchall():
    vals = []
    vals.extend([quote(c) for c in row[1:4]])
    vals[1] = 'NULL' if 'choose a make' in vals[1] else vals[1] 
    vals.append(n(row[4]))
    vals.append(check_units(row[5], "g/km"))
    vals.append(quote(row[6]))
    vals.extend([n(c) for c in row[7:10]])
    vals.append(check_units(row[10], "months"))
    vals.append(n(row[11]))
    vals.append(quote(row[12]))
    vals.append(quote(row[13]))
    vals.append(check_units(row[14], "mph"))
    vals.append(check_units(row[15], "miles"))
    vals.append(check_units(row[16], "secs"))
    vals.append(quote(row[17]))
    vals.append(check_units(row[18], "Nm"))
    vals.append(quote(row[19]))
    vals.extend([n(c) for c in row[20:24]])
    vals.append(check_units(row[24], "litres"))
    vals.append(check_units(row[25], "litres"))
    vals.append(n(row[26]))

    vals = [v.replace(',', '') for v in vals]

    data = ','.join(vals)

    try:
        print(template.format(colnames, data))
    except UnicodeEncodeError:
        pass
