import signal
import sys
import os
import random

import ansi
from quiz import Quiz, Question
import util


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
	menu_options = list( map( lambda m: m[ 0 ], menu ) )
	ansi.print_style( "\n== Main Menu ==\n", ansi.Fore.GREEN )
	option = util.get_option( "Enter selection", menu_options )
	menu[ option ][ 2 ]()

def load_quizzes():
	global quizzes
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

def select_quiz():
	global quizzes
	ansi.print_style( "\n== Select Quiz ==\n", ansi.Fore.GREEN )
	quiz_list = list( map(
		lambda q: q.name + f" ({len(q.questions)} questions)",
		quizzes
	) )
	quiz_index = util.get_option( "Select quiz", quiz_list )
	
	run_quiz( quizzes[ quiz_index ] )

def run_quiz( quiz ):
	ansi.print_style( f"\n== {quiz.name} ==\n", ansi.Fore.GREEN )
	if quiz.description != "":
		print( quiz.description )
	for question in quiz.questions:
		print()
		print( question.text )
		answers =  question.answers[ : ]
		random.shuffle( answers )
		answer = util.get_option( "Select answer", answers, True )
		if answers[ answer ] == question.answers[ question.correct_answer ]:
			ansi.print_style( "Correct!", ansi.Fore.GREEN + ansi.Style.BOLD )
		else:
			ansi.print_style( "Wrong!", ansi.Fore.RED2 + ansi.Style.BOLD )

def create_quiz():
	ansi.print_style( "\n== Creating Quiz ==\n", ansi.Fore.GREEN )
	quiz = Quiz()
	quiz.name = util.get_text( "Enter quiz name: ", "Name cannot be blank." )
	quiz.description = util.get_text( "Enter quiz description: " )
	
	question_text = "not blank"
	print( "Enter blank question text to stop" )
	while question_text != "":

		# Get the question text
		question_text = util.get_text( "Enter question text: " )
		if question_text != "":
			question = Question()
			question.text = question_text

			# Get the answer
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

				# Get the correct answer
				ansi.print_style( question.text, ansi.Fore.WHITE2 )
				question.correct_answer = util.get_option(
					"Enter correct answer", question.answers
				)

				# Get the concepts
				ansi.print_style( "Enter concepts; leave blank to skip.", ansi.Fore.WHITE2 )
				concept_text = "not blank"
				while concept_text != "":
					concept_text = util.get_text( "Enter concept: " )
					if concept_text != "":
						question.concepts.append( concept_text )

				# Add the question
				quiz.questions.append( question )
		print()
	print( f"Quiz: {quiz.name} created with {len(quiz.questions)} questions." )
	quiz.save()


def edit_quiz():
	print( "Editing Quiz" )

quizzes = []
menu = [
	( "Select Quiz", "-s", select_quiz ),
	( "Create Quiz", "-c", create_quiz ),
	( "Edit Quiz", "-e", edit_quiz )
]

if __name__ == '__main__':
	main()
