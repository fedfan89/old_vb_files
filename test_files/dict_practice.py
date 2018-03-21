class Paul():
	def __init__(self, breakfast='eggs', lunch='remos'):
		print('You have made an instance of the Paul class')
		self.breakfast=breakfast
		self.lunch=lunch
		self.dinner= 'sushi'
		self.snack = 'peanuts'

	def throwaway(self):
		print('Wuddup Billy?')
		return(self)

	def __breakfast_time__(self):
		print('Your breakfast is ready!')
		return('Hi Paul')
monday = Paul()
tuesday = Paul('bacon', 'thai')
wednesday = Paul(lunch= 'sandwich', breakfast = 'coffee')

monday.snack2 = 'grilled cheese'
monday.dinner = 'vegetarian meal'
print(monday, type(monday), monday.__dict__)
monday.throwaway().throwaway().throwaway().throwaway().throwaway().throwaway()

