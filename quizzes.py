import ansi
import util

def select_quiz():
	ansi.print_style( "\n== Select Quiz ==\n", ansi.Fore.GREEN )
	quiz_list = list( map(
		lambda q: q.name + f" ({len(q.questions)} questions)",
		quizzes
	) )
	quiz_index = util.get_option( "Select quiz", quiz_list )
	return quiz_index

quizzes = []