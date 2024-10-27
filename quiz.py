import json

class Question():
	def __init__( self ):
		self.text = ""
		self.answers = []
		self.correct_answer = -1
	
	def load( self, data ):
		# Check for required question keys
		if 'text' not in q or 'answers' not in q or 'correct_answer' not in q:
			raise ValueError(
				f"Missing required question keys in JSON file '{filename}'."
			)
		question.text = q['text']
		question.answers = q['answers']
		question.correct_answer = q['correct_answer']


class Quiz():
	def __init__( self ):
		self.name = ""
		self.description = ""
		self.questions = []
	
	def load( self, filename ):
		try:
			with open( filename, "r" ) as file:
				data = json.load( file )
				
				# Check if the data is a dictionary
				if not isinstance( data, dict ):
					raise ValueError( f"Invalid JSON format for file '{filename}'." )

				# Check for required keys
				all_keys = [ "name", "description", "questions" ]
				for key in all_keys:
					if key not in data:
						raise ValueError( f"Missing required {key} in JSON file '{filename}'." )

				# Load basic quiz info
				self.name = data[ "name" ]
				self.description = data[ "description" ]

				# Load questions
				if not isinstance( data[ "questions" ], list ):
					raise ValueError( f"'questions' must be a list in JSON file '{filename}'." )

				for q in data[ "questions" ]:
					if not isinstance( q, dict ):
						raise ValueError(
							f"Each question must be a dictionary in JSON file '{filename}'."
						)

					question = Question()
					question.text = q['text']
					question.answers = q['answers']
					question.correct_answer = q['correct_answer']

					# Basic validation of answers
					if not isinstance( question.answers, list ) or len( question.answers ) == 0:
						raise ValueError(
							f"Invalid answers format for question '{question.text}'."
						)
					
					# Validate correct_answer index
					if not isinstance( question.correct_answer, int ) or not ( 0 <= question.correct_answer < len( question.answers ) ):
						raise ValueError( f"Invalid correct answer index for question '{question.text}'." )

					self.questions.append( question )
		except Exception as e:
			raise Exception( f"Error loading quiz from file '{filename}': {str(e)}" )
