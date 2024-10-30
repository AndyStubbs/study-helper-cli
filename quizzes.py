import os
import ansi
import util
from quiz import Quiz


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

def select_quiz():
	ansi.print_style( "\n== Select Quiz ==\n", ansi.Fore.GREEN )
	quiz_list = list( map(
		lambda q: q.name + f" ({len(q.questions)} questions)",
		quizzes
	) )
	quiz_index = util.get_option( "Select quiz", quiz_list )
	return quiz_index

quizzes = []