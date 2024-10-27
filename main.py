import signal
import sys

import ansi
from quiz import Quiz, Question
import util


def main():
	print()
	ansi.print_style( "Study Helper 1.0", ansi.Fore.CYAN )
	print( "Press Ctrl+C to exit at anytime\n" )
	signal.signal( signal.SIGINT, handle_quit )
	display_menu()

def handle_quit( sig, frame ):
	print( "\nGoodbye." )
	sys.exit( 0 )

def display_menu():
	menu_options = list( map( lambda m: m[ 0 ], menu ) )
	ansi.print_style( "\n== Main Menu ==\n", ansi.Fore.GREEN )
	option = util.get_option( "Enter selection", menu_options )
	menu[ option ][ 2 ]()

def run_quiz():
	print( "Running Quiz" )

def create_quiz():
	ansi.print_style( "\n== Creating Quiz ==\n", ansi.Fore.GREEN )
	quiz = Quiz()
	quiz.name = util.get_text( "Enter quiz name: ", "Name cannot be blank." )
	quiz.description = util.get_text( "Enter quiz description: " )
	
	question_text = "not blank"
	print( "Enter blank question text to stop" )
	while question_text != "":
		question_text = util.get_text( "Enter question text: " )
		if question_text != "":
			question = Question()
			question.text = question_text
			answer_text = "not blank"
			ansi.print_style( "Enter blank answer to stop.", ansi.Fore.WHITE2 )
			while answer_text != "":
				answer_text = util.get_text( "Enter answer: " )
				if answer_text != "":
					question.answers.append( answer_text )
			if len( question.answers ) == 0:
				ansi.print_style(
					"No answers entered; question not saved.",
					ansi.Fore.RED2
				)
			else:
				print()
				ansi.print_style( question.text, ansi.Fore.WHITE2 )
				question.correct_answer = util.get_option(
					"Enter correct answer", question.answers
				)
				quiz.questions.append( question )
		print()
	print( f"Quiz: {quiz.name} created with {len(quiz.questions)} questions." )
	quiz.save()


def edit_quiz():
	print( "Editing Quiz" )


menu = [
	( "Run Quiz", "-r", run_quiz ),
	( "Create Quiz", "-c", create_quiz ),
	( "Edit Quiz", "-e", edit_quiz )
]

if __name__ == '__main__':
	main()
