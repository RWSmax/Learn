import string

values = {'var': 'test'}
print('*' * 40)


temp = string.Template("""
Variable            : $var
Escape             : $$
Variable in text    : ${var}iable {var}iable
""")
print('TEMPLATE:', temp.substitute(values))
print('*' * 40)


s = """
Variable: %(var)s
Escape: %%
Variable in text: $(var)iable
"""
print('INTERPOLATION:', s % values)
print('*' * 40)


s = """
Variable: {var}
Escape: {{}}
Variable in text: {var}iable
"""
print('FORMAT:', s.format(**values))
print('*' * 40)