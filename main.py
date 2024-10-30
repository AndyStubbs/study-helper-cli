import signal
import sys

import ansi
from quiz import Quiz
import util
from create import create_quiz
from edit import edit_quiz
from run import run_quiz
from quizzes import load_quizzes


def main():
	load_quizzes()
	print()
	ansi.print_style( "Study Helper 1.0", ansi.Fore.CYAN )
	print( "Press Ctrl+C to exit at anytime" )
	signal.signal( signal.SIGINT, handle_quit )
	display_menu()

def handle_quit( sig, frame ):
	end()

def end():
	print( "\nGoodbye." )
	sys.exit( 0 )

def display_menu():
	while True:
		print()
		menu = [
			( "Run Quiz", "-r", run_quiz ),
			( "Create Quiz", "-c", create_quiz ),
			( "Edit Quiz", "-e", edit_quiz ),
			( "Quit", "", end )
		]
		menu_options = list( map( lambda m: m[ 0 ], menu ) )
		ansi.print_style( "\n== Main Menu ==\n", ansi.Fore.GREEN )
		option = util.get_option( "Enter selection", menu_options )
		menu[ option ][ 2 ]()

if __name__ == '__main__':
	main()
