import signal
import sys
import os

import ansi
from quiz import Quiz
import util
from create import create_quiz
from edit import edit_quiz
from run import run_quiz
from quizzes import quizzes


def main():
	load_quizzes()
	print()
	ansi.print_style( "Study Helper 1.0", ansi.Fore.CYAN )
	print( "Press Ctrl+C to exit at anytime\n" )
	signal.signal( signal.SIGINT, handle_quit )
	display_menu()

def handle_quit( sig, frame ):
	print( "\nGoodbye." )
	sys.exit( 0 )

def display_menu():
	menu = [
		( "Run Quiz", "-r", run_quiz ),
		( "Create Quiz", "-c", create_quiz ),
		( "Edit Quiz", "-e", edit_quiz )
	]
	menu_options = list( map( lambda m: m[ 0 ], menu ) )
	ansi.print_style( "\n== Main Menu ==\n", ansi.Fore.GREEN )
	option = util.get_option( "Enter selection", menu_options )
	menu[ option ][ 2 ]()

def load_quizzes():
	prefix = "quiz-"
	postfix = ".json"
	quiz_dir = "quizzes"
	files = os.listdir( quiz_dir )
	for file in files:
		if file.startswith( prefix ) and file.endswith( postfix ):
			file_path = os.path.join( quiz_dir, file )
			try:
				quiz = Quiz()
				quiz.load_from_file( file_path )
				quizzes.append( quiz )
			except Exception as ex:
				ansi.print_style( ex, ansi.Fore.RED2 )

if __name__ == '__main__':
	main()
