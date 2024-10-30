import os
import unittest
from tests.test_quiz import TestQuiz

if __name__ == "__main__":
	# Remove any existing test quizzes
	current_dir = os.path.dirname( __file__ )
	quiz_dir = os.path.join( current_dir, "tests/quizzes" )
	files = os.listdir( quiz_dir )
	for file in files:
		file_path = os.path.join( quiz_dir, file )
		if os.path.isfile( file_path ):
			os.remove( file_path )
	
	# Run tests
	unittest.main()