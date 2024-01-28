# always use curly brackets with dictionary
# define key value pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# print(monthConversions["Oct"])

# print(monthConversions.get("Oct"))

print(monthConversions.get("Luv", "Not a valid key"))