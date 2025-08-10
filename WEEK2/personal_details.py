
class PersonalDetails:
	def __init__(self, name, age, address):
		self.details = [name, age, address]

	def display_details(self):
		print("\nPersonal Details:")
		print(f"Name: {self.details[0]}")
		print(f"Age: {self.details[1]}")
		print(f"Address: {self.details[2]}")

	def add_years(self, years):
		self.details[1] += years

	def display_updated(self):
		print(f"\nUpdated Info: {self.details[0]} will be {self.details[1]} years old and lives at {self.details[2]}.")


def get_valid_number(prompt):
	while True:
		value = input(prompt)
		try:
			return int(value)
		except ValueError:
			print("Please enter a valid number.")

def main():
	name = input("Enter your name: ")
	age = get_valid_number("Enter your age: ")
	address = input("Enter your address: ")
	person = PersonalDetails(name, age, address)
	person.display_details()
	years_to_add = get_valid_number("\nHow many years would you like to add to your age? ")
	person.add_years(years_to_add)
	person.display_updated()

if __name__ == "__main__":
	main()
