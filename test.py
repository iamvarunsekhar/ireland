import parkpart as pt


# Test case 1. When there is no space available 
print('Test case 1 - No space available')
n=2000
pt.simulate_parking(n)
print('Test case 1: Success\n\n\n')

# Test case 2. When there space available only on left
print('Test case 2 - Space on left')
n=2000
pt.simulate_parking(n,'left')
print('Test case 2: Success\n\n\n')

# Test case 3. When there is space available only on right
print('Test case 3 - Space on right')
n=2000
pt.simulate_parking(n,'right')
print('Test case 3: Success\n\n\n')

# Test case 4. When there is space available on both sides
print('Test case 4 - Space on both sides')
n=20
pt.simulate_parking(n)
print('Test case 4: Success\n\n\n')


