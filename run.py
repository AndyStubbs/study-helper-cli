import random
import ansi
import util
from quizzes import select_quiz, quizzes

def run_quiz():
	quiz_index = select_quiz()
	start_quiz( quizzes[ quiz_index ] )

def start_quiz( quiz ):
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
