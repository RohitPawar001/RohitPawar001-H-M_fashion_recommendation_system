def remove_null_bytes(filename):
    with open(filename, 'rb') as file:
        content = file.read()
    
    # Remove null bytes
    content = content.replace(b'\x00', b'')
    
    with open(filename, 'wb') as file:
        file.write(content)

# Example usage
remove_null_bytes('D:\\software\\python_vs\\H_and_M_recommendation_system\\main.py')
print("succesfu")
