import json


class Question():
	def __init__( self ):
		self.text = ""
		self.answers = []
		self.correct_answer = -1
	
	def load( self, data ):
		# Check for required question keys
		all_keys = [ "text", "answers", "correct_answer" ]
		for key in all_keys:
			if key not in data:
				raise ValueError( f"Missing required {key} in question." )
		if not isinstance( data[ "text" ], str ):
			raise ValueError( "Invalid format for text in question." )
		if data[ "text" ] == "":
			raise ValueError( "Question text must not be blank." )
		self.text = data[ "text" ]
		
		# Validate Answers
		if (
			not isinstance( data[ "answers" ], list ) or
			len( data[ "answers" ] ) == 0
		):
			raise ValueError(
				f"Invalid format for answers in question '{self.text}'."
			)
		self.answers = []
		for answer in data[ "answers" ]:
			if isinstance( answer, str ):
				self.answers.append( answer )
			else:
				raise ValueError(
					f"Invalid format for answer in question '{self.text}'."
				)
		
		# Validate correct answer
		if (
			not isinstance( data[ "correct_answer" ], int ) or
			data[ "correct_answer" ] < 0 or
			data[ "correct_answer" ] >= len( self.answers )
		):
			raise ValueError(
				f"Invalid format for correct_answer in question '{self.text}'."
			)
		self.correct_answer = data[ "correct_answer" ]


class Quiz():
	def __init__( self ):
		self.name = ""
		self.description = ""
		self.questions = []
	
	def load_from_file( self, filename ):
		with open( filename, "r" ) as file:
			data = json.load( file )
		self.load( data )
	
	def load( self, data ):
		# Check if the data is a dictionary
		if not isinstance( data, dict ):
			raise ValueError( "Invalid JSON format." )

		# Check for required keys
		all_keys = [ "name", "description", "questions" ]
		for key in all_keys:
			if key not in data:
				raise ValueError( f"Missing required {key}." )

		# Load name
		if not isinstance( data[ "name" ], str ):
			raise ValueError( "Invalid format for name." )
		if data[ "name" ] == "":
			raise ValueError( "Field name cannot be blank." )
		self.name = data[ "name" ]

		# Load description
		if not isinstance( data[ "description" ], str ):
			raise ValueError( f"Invalid format for description." )
		self.description = data[ "description" ]

		# Load questions
		if not isinstance( data[ "questions" ], list ):
			raise ValueError( "Invalid format for questions." )

		for q in data[ "questions" ]:
			question = Question()
			question.load( q )
			self.questions.append( question )

