def concatenate_list_data(values):
    result = ''  
    for value in values:
        result +=str(value)

    return result  # Return the concatenated string.

# Call the concatenate_list_data function with a list of numbers and print the result.
print(concatenate_list_data([1, 5, 12, 2]))