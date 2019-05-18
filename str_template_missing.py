import string

values = {'var': 'test'}

t = string.Template("$var is here but $missing is not provided.")
try:
    print('substitute():', t.substitute(values))
except KeyError as err:
    print('Error:', str(err))
print('safe_substitute():', t.safe_substitute(values))
