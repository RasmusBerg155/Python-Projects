# Model an organisation of employees, management and board of directors in 3 sets.Model an organisation of employees, management and board of directors in 3 sets.
# Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
# Management: Tine, Trunte, Rane
# Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

directors = ["Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"]
management = ["Tine", "Trunte", "Rane"]
employees = ["Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"]

# who in the board of directors is not an employee?
print(list(sorted(set(directors) - set(employees))))

# who in the board of directors is also an employee?
print(list(set(directors) & set(employees)))

# how many of the management is also member of the board?
print(len(list(set(directors) & set(management))))

# All members of the managent also an employee?
result = all(elem in employees for elem in management)

if result:
    print(result)
else:
    print(result)

# All members of the management also in the board?
result = all(elem in directors for elem in management)

if result:
    print(result)
else:
    print(result)

# Who is an employee, member of the management, and a member of the board?
print(list(set(directors) & set(management) & set(employees)))

# Who of the employee is neither a memeber or the board or management?
print(list(sorted(set(employees) - set(management) - set(directors))))

# 2. Using a list comprehension create a list of tuples from the following datastructure 
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
myTuple = [('a', 'b', 'c'), ('Alpha', 'Beta', 'Gamma')]

for n in myTuple:
    print (n[0])
# Or another solution with zip function
print(list(zip(*myTuple))[0])

# From these 2 sets:
s1 = {'a', 'e', 'i', 'o', 'u', 'y'}
s2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
# Of the 2 sets create a: Union
s = s1.union(s2)
# Sorted virker ikke på dansk så æøå er forkert rækkefølge
print(sorted(s))
 
# Of the 2 sets create a: Symmetric Difference
s = s1.symmetric_difference(s2)
print(s)

# Of the 2 sets create a: Difference
# s1 will show "set()" because it had no additionel numbers from s2
print(s1.difference(s2))
print(s2.difference(s1))

# Of the 2 sets create a: Disjoint
# As of now our sets are not disjoints, and we can check this with:
s= s1.isdisjoint(s2)
# or for subsets 
s = s1.issubset(s2)
# Lets create and print the disjoint, this solves it although im not sure that was the solution Claus was looking for
print(sorted(list(set(s1) & set(s2))))

# Date Decoder
# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
# Create a dict suitable for decoding month names to numbers.
# Create a function which uses string operations to split the date into 3 items using the "-" character.
# Translate the month, correct the year to include all of the digits.
# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
def convert(convert_date):
    date_list = []

    dict = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12
    }

    input_split = convert_date.split('-')

    #Year
    if int(input_split[2]) >= 0:
        year = '20' + input_split[2]
    else:
        year = '19' + input_split[2]
    date_list.append(year)

    #Month
    month = dict[input_split[1].upper()]
    date_list.append(month)

    #Day
    day = input_split[0]
    date_list.append(day)

    date_list = [str(item) for item in date_list]
    return date_list

def Convert():
    user_input = input('Enter a date formatted as "DD-MMM-YY" \n')
    print(','.join((convert(user_input))))

Convert()