my_dict = {"a": 1, "b": 2, "c": 3}

# Iterate over keys
print("Keys:")
for key in my_dict:
    print(key)

# Iterate over values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


output_setup = {'SpaceClaim': [True, '_spaceclaim'],
                'Xfoil/xflr5': [True, '_xfoil_xflr'],
                'PTC Creo': [True, '_Creo'],
                }

for key, value in output_setup.items():
    print(f"{key}: {[i for i in value]}")