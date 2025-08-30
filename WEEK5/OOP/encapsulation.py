class Student:
	def __init__(self, name, age, passport_number):
		self.name = name  # public
		self._age = age   # protected
		self.__grade = 'A'  # private
		self.__passport_number = passport_number  # private

	def get_grade(self):
		return self.__grade
	def get_passport_number(self):
		return self.__passport_number


# New class to demonstrate accessibility
class StudentInspector:
	def __init__(self, student):
		self.student = student

	def inspect(self):
		print("Inspector accessing public name:", self.student.name)
		print("Inspector accessing protected age:", self.student._age)
		# The following line would raise AttributeError if uncommented:
		# print("Inspector accessing private grade:", self.student.__grade)
		# Correct way to access private:
		print("Inspector accessing private grade via method:", self.student.get_grade())
		print("Inspector accessing private passport via method:", self.student.get_passport_number())

s = Student('Philip', 26, 'P123456789')

def main():
	s = Student('Philip', 26, 'P123456789')
	s.name         # accessible
	s._age        # discouraged
	s.get_grade() # correct way
	s.get_passport_number() # correct way

	# Try to access private attributes directly and catch errors
	try:
		print(s.__grade)
	except AttributeError as e:
		print("Error accessing __grade:", e)

	try:
		print(s.__passport_number)
	except AttributeError as e:
		print("Error accessing __passport_number:", e)

	# New class to demonstrate accessibility
	inspector = StudentInspector(s)
	inspector.inspect()

if __name__ == "__main__":
	main()