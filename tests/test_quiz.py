import unittest
import os
from quiz import Quiz


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
			( "questions", "data/quiz-bad-07.json" )
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
			( "correct_answer", "data/quiz-bad-10.json" ),
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

