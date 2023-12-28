# Create a function to split email
def main():
  try:
    print('Welcome to the Email Slicer')
    print(' ')
    
    # Take the User Input
    email_input = input('Enter your Email here: ')
    
    # Split into parts and assign to Variables
    (Username , Domain) = email_input.split('@')
    (Domain, Extension) = Domain.split('.')
    
    # Print results
    print('')
    print(f'Username: {Username}')
    print(f'Domain: {Domain}')
    print(f'Extension: {Extension}')
    
  except:
      print('Not a Valid gmail,try again')
# Call the function 
while True:
   main()
 