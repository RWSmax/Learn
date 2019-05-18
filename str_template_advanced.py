import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = """
delimiter: %%
Replaced: %with_underscore
Ignored: %notunderscored
"""

d={
    'with_underscore':'replaced',
    'notunderscored':'not replaced',
}

t = MyTemplate(template_text)
print('Modified ID pattern')
print(t.safe_substitute(d))
print('its regexp for _ in idpattern variable. So, notunderscored - ignored, WITH DELIMITER:',MyTemplate.delimiter)