def hashFunction(key, table_size):
    hashValue = sum(ord(char) for char in key ) % table_size
    return hashValue

#Example usage 1
key = "Kimani"
table_size = 25
hashValue = hashFunction(key, table_size)
print(f"Hash Value for '{key}': {hashValue}")

#Example usage 2
key = input("Enter the key: ")
table_size = 25
hashValue = hashFunction(key, table_size)
print(f"Hash Value for '{key}': {hashValue}")
