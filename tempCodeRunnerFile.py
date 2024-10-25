
data = {
    "Zip Code": ["33050", "33040", "33045", "29401", "29577", "32034", "32951", "32940", "33706", "29928"],
    "City": ["Marathon", "Key West", "Islamorada", "Charleston", "Myrtle Beach", "Fernandina Beach", "Melbourne Beach", "Vero Beach", "St. Petersburg", "Hilton Head Island"],
    "State": ["FL", "FL", "FL", "SC", "SC", "FL", "FL", "FL", "FL", "SC"],
    "Number of Hurricane Landfalls (1950-2020)": [14, 13, 12, 11, 10, 9, 9, 8, 8, 7]
}

df = pd.DataFrame(data)
print(df) #this isnt priting?