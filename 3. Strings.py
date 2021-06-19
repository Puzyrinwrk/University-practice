# Task_1
# Write a simple function which removes dots and double quotes from input text.
# Function signature: def remove_dots_quotas(text)

# Task_2
# Write a function to surround single line string with border constructed by number-signs '#' (on left and right extra space added)
# Result is three-line string
# Example: some string converted to
# ###############
# #   string    #
# ###############
# Function signature: def border_string(s)

# Task_3
# Write an inverse function for border fuction from previous task
# Example:
# ##############
# #   string   #
# ##############
# converted to string
# Remember: this function is inversion for border_string. So, unborder_string(border_string("any string")) should be equal to "any string". Pay attention to trailing spaces.
# Function signature: def unborder_string(s)

# Task_4
# Write a function to normalize person's name:
# 1) name starts with optional honorific (Mr Mrs Miss Lord Lady Sir Sire Dr Professor and others)  followed by first name, optional middle names, ends with last name
# 2) unneeded spaces should be removed
# 3) honorific should be capitalized
# Example: "  sir Arthur     Conan   Doyle " normalized to "Sir Arthur Conan Doyle"
# Function signature: def normalize_name(s)


# Task_1
a = "hi.."""


def remove_dots_quotas(text: str) -> str:
    return text.replace('"', '').replace('.', '')


print(remove_dots_quotas(a))


# Task_2
def border_string(s):
    sl = len(s) + 4
    return '#' * sl + '\n# ' + s + ' #\n' + '#' * sl


print((border_string('blah blah blah')))


# Task_3
def unborder_string(s):
    sl = int((len(s) - 2) / 3 + 3)
    return s[sl:-sl]


print(unborder_string(border_string('blah blah blah')))


# Task_4
def normalize_name(s):
    return ' '.join(s.split()).title()


name = input()
print(normalize_name(name))
