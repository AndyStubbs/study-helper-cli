import random
import ansi
import util
from quizzes import select_quiz, quizzes

def run_quiz():
	if len( quizzes ) == 0:
		ansi.print_style( f"No quizzes to run", ansi.Fore.RED2 )
		return
	quiz_index = select_quiz()
	if quiz_index >= len( quizzes ):
		return
	start_quiz( quizzes[ quiz_index ] )

def start_quiz( quiz ):
	ansi.print_style( f"\n== {quiz.name} ==\n", ansi.Fore.GREEN )
	if quiz.description != "":
		print( quiz.description )
	if len( quiz.questions ) == 0:
		ansi.print_style( f"No questions in quiz", ansi.Fore.RED2 )
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
