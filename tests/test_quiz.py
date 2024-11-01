import unittest
import os
from quiz import Quiz, Question


class TestQuiz( unittest.TestCase ):
	def test_load_file_not_found( self ):
		quiz = Quiz()
		with self.assertRaises( FileNotFoundError ) as context:
			quiz.load_from_file( "no-file.json" )
	
	def test_load_invalid_format( self ):
		current_dir = os.path.dirname( __file__ )
		filename = os.path.join( current_dir, "data/quiz-bad-01.json" )
		quiz = Quiz()
		with self.assertRaises( ValueError ) as context:
			quiz.load_from_file( filename )
		self.assertEqual(
			str( context.exception ),
			f"Invalid JSON format."
		)
	
	def test_load_missing_key( self ):
		current_dir = os.path.dirname( __file__ )
		files = [
			( "name", "data/quiz-bad-02.json" ),
			( "description", "data/quiz-bad-03.json" ),
			( "questions", "data/quiz-bad-04.json" ),
		]
		for ( key, name ) in files:
			filename = os.path.join( current_dir, name )
			quiz = Quiz()
			with self.assertRaises( ValueError ) as context:
				quiz.load_from_file( filename )
			self.assertEqual(
				str( context.exception ),
				f"Missing required {key}."
			)
	
	def test_load_text_blank( self ):
		current_dir = os.path.dirname( __file__ )
		filename = os.path.join( current_dir, "data/quiz-bad-20.json" )
		quiz = Quiz()
		with self.assertRaises( ValueError ) as context:
			quiz.load_from_file( filename )
		self.assertEqual(
			str( context.exception ),
			f"Field name cannot be blank."
		)

	def test_load_invalid_key_format( self ):
		current_dir = os.path.dirname( __file__ )
		files = [
			( "name", "data/quiz-bad-05.json" ),
			( "description", "data/quiz-bad-06.json" ),
			( "questions", "data/quiz-bad-07.json" ),
			( "topic", "data/quiz-bad-26.json" )
		]
		for ( key, name ) in files:
			filename = os.path.join( current_dir, name )
			quiz = Quiz()
			with self.assertRaises( ValueError ) as context:
				quiz.load_from_file( filename )
			self.assertEqual(
				str( context.exception ),
				f"Invalid format for {key}."
			)
	
	def test_load_missing_key_in_question( self ):
		current_dir = os.path.dirname( __file__ )
		files = [
			( "text", "data/quiz-bad-08.json" ),
			( "answers", "data/quiz-bad-09.json" ),
			( "correct_answer", "data/quiz-bad-10.json" )
		]
		for ( key, name ) in files:
			filename = os.path.join( current_dir, name )
			quiz = Quiz()
			with self.assertRaises( ValueError ) as context:
				quiz.load_from_file( filename )
			self.assertEqual(
				str( context.exception ),
				f"Missing required {key} in question."
			)
	
	def test_load_invalid_key_format_in_question( self ):
		current_dir = os.path.dirname( __file__ )
		files = [
			( "text", "data/quiz-bad-11.json", "." ),
			( "answers", "data/quiz-bad-12.json", " 'Test question?'." ),
			( "answers", "data/quiz-bad-13.json", " 'Test question?'." ),
			( "correct_answer", "data/quiz-bad-14.json", " 'Test question?'." ),
			( "answer", "data/quiz-bad-15.json", " 'Test question?'." ),
			( "correct_answer", "data/quiz-bad-16.json", " 'Test question?'." ),
			( "correct_answer", "data/quiz-bad-17.json", " 'Test question?'." ),
			( "correct_answer", "data/quiz-bad-18.json", " 'Test question?'." ),
			( "answer", "data/quiz-bad-19.json", " 'Test question?'." ),
			( "answer", "data/quiz-bad-22.json", " 'Test question?'." ),
			( "concepts", "data/quiz-bad-23.json", " 'Test question?'." ),
			( "concept", "data/quiz-bad-24.json", " 'Test question?'." ),
			( "concept", "data/quiz-bad-25.json", " 'Test question?'." )
		]
		for ( key, name, end ) in files:
			filename = os.path.join( current_dir, name )
			quiz = Quiz()
			with self.assertRaises( ValueError ) as context:
				quiz.load_from_file( filename )
			self.assertEqual(
				str( context.exception ),
				f"Invalid format for {key} in question{end}"
			)
	
	def test_load_missing_text_in_question( self ):
		current_dir = os.path.dirname( __file__ )
		filename = os.path.join( current_dir, "data/quiz-bad-21.json" )
		quiz = Quiz()
		with self.assertRaises( ValueError ) as context:
			quiz.load_from_file( filename )
		self.assertEqual(
			str( context.exception ),
			f"Question text must not be blank."
		)
	
	def test_load_quiz( self ):
		current_dir = os.path.dirname( __file__ )
		filename = os.path.join( current_dir, "data/quiz-good-01.json" )
		quiz = Quiz()
		quiz.load_from_file( filename )
		
		# Checks
		self.assertEqual( "test", quiz.name )
		self.assertEqual( "test description", quiz.description )
		self.assertEqual( 4, len( quiz.questions ) )
		self.assertEqual( "Test question 1?", quiz.questions[ 0 ].text )
		self.assertEqual( 4, len( quiz.questions[ 1 ].answers ) )
		self.assertEqual( "2", quiz.questions[ 2 ].answers[ 1 ] )
		self.assertEqual( 3, quiz.questions[ 3 ].correct_answer )
		self.assertEqual( "4", quiz.questions[ 3 ].answers[ 3 ] )
	
	def test_load_quiz2( self ):
		current_dir = os.path.dirname( __file__ )
		filename = os.path.join( current_dir, "data/quiz-good-02.json" )
		quiz = Quiz()
		quiz.load_from_file( filename )
		
		# Checks
		self.assertEqual( "test 2", quiz.name )
		self.assertEqual( "", quiz.description )
		self.assertEqual( 3, len( quiz.questions ) )
		self.assertEqual( "Test", quiz.topic )
		self.assertEqual( "D", quiz.questions[ 1 ].concepts[ 1 ] )
	
	def test_00_save_quiz( self ):
		# Get pathnames
		current_dir = os.path.dirname( __file__ )
		quiz_dir = os.path.join( current_dir, "quizzes" )
		
		# Create a blank quiz
		quiz1 = Quiz()
		quiz1.name = "Blank Quiz"
		quiz1.save( "tests/quizzes" )
		
		# Create a quiz with some questions
		quiz2 = Quiz()
		quiz2.name = "Quiz With Data"
		quiz2.description = "Test Description"
		quiz2.topic = "Topic"
		question1 = Question()
		question1.text = "What is 1+1?"
		question1.answers = [ "1", "2", "3", "4" ]
		question1.correct_answer = 1
		question1.concepts.append( "Addition" )
		quiz2.questions.append( question1 )
		question2 = Question()
		question2.text = "What is 2+2?"
		question2.answers = [ "2", "3", "4", "5" ]
		question2.correct_answer = 2
		question2.concepts.append( "Addition" )
		quiz2.questions.append( question2 )
		question3 = Question()
		question3.text = "What is 2-1?"
		question3.answers = [ "1", "2", "3", "4" ]
		question3.correct_answer = 2
		question3.concepts.append( "Subtraction" )
		question3.concepts.append( "Minus" )
		quiz2.questions.append( question3 )
		quiz2.save( "tests/quizzes" )
		
		# Check quiz1
		quiz1_path = os.path.join( quiz_dir, "quiz-0001.json" )
		self.assertTrue( os.path.exists( quiz1_path ) )
		quizCheck1 = Quiz()
		quizCheck1.load_from_file( quiz1_path )
		self.assertEqual( quiz1.name, quizCheck1.name )
		self.assertEqual( quiz1.description, quizCheck1.description )
		self.assertEqual( len( quiz1.questions ), len( quizCheck1.questions ) )
		
		# Check quiz2
		quiz2_path = os.path.join( quiz_dir, "quiz-0002.json" )
		self.assertTrue( os.path.exists( quiz2_path ) )
		quizCheck2 = Quiz()
		quizCheck2.load_from_file( quiz2_path )
		self.assertEqual( quiz2.name, quizCheck2.name )
		self.assertEqual( quiz2.description, quizCheck2.description )
		self.assertEqual( quiz2.topic, quizCheck2.topic )
		self.assertEqual( len( quiz2.questions ), len( quizCheck2.questions ) )
		self.assertEqual( 1, quizCheck2.questions[ 0 ].correct_answer )
		self.assertEqual( "What is 2+2?", quizCheck2.questions[ 1 ].text )
		self.assertEqual( len( quiz2.questions[ 1 ].concepts ), len( quizCheck2.questions[ 1 ].concepts ) )
		self.assertEqual( "Addition", quizCheck2.questions[ 0 ].concepts[ 0 ] )

	def test_01_edit_and_save_quiz( self ):

		# Get pathnames
		current_dir = os.path.dirname( __file__ )
		quiz_dir = os.path.join( current_dir, "quizzes" )

		# Create initial quiz
		quiz1 = Quiz()
		quiz1.name = "Blank Quiz 3"
		quiz1.save( "tests/quizzes" )
		quiz_path = os.path.join( quiz_dir, quiz1.filename )

		# Load the same quiz from file
		quiz2 = Quiz()
		quiz2.load_from_file( quiz_path )

		# Make sure the quiz loads
		self.assertEqual( quiz1.name, quiz2.name )

		# Make a change and save it again
		quiz2.name = "Blank Quiz 3 - Updated"
		quiz2.save( "tests/quizzes" )

		# Load it again
		quiz3 = Quiz()
		quiz3.load_from_file( quiz_path )

		# Make sure the changed data was saved
		self.assertEqual( quiz3.name, quiz2.name )
