import ansi
import util
from run import select_quiz
from quizzes import quizzes


def edit_quiz():
	ansi.print_style( "\n== Edit Quiz ==\n", ansi.Fore.GREEN )
	quiz_index = select_quiz()
	quiz = quizzes[ quiz_index ]
	edit_quiz_single( quiz )

def edit_quiz_single( quiz ):
	undo_data = quiz.serialize()
	is_editing = True
	while is_editing:
		ansi.print_style( f"\n== Editing Quiz '{quiz.name}' ==\n", ansi.Fore.GREEN )
		options = [
			"Edit Name",
			"Edit Description",
			"Edit Topic",
			"Edit Questions",
			"Save Changes",
			"Undo Changes"
		]
		option = util.get_option( "Enter selection", options )
		if options[ option ] == "Edit Name":
			edit_quiz_name( quiz )
		elif options[ option ] == "Edit Description":
			edit_quiz_description( quiz )
		elif options[ option ] == "Edit Topic":
			edit_topic( quiz )
		elif options[ option ] == "Edit Questions":
			edit_questions( quiz )
		elif options[ option ] == "Save Changes":
			save_changes( quiz )
			is_editing = False
		elif options[ option ] == "Undo Changes":
			undo_changes( quiz, undo_data )
			is_editing = False

def edit_quiz_name( quiz ):
	print( quiz.name )
	quiz.name = util.get_text( "Enter new name: ", "Name cannot be blank" )

def edit_quiz_description( quiz ):
	print( quiz.description )
	quiz.description = util.get_text( "Enter new description: " )

def edit_topic( quiz ):
	print( quiz.topic )
	quiz.topic = util.get_text( "Enter new topic: " )

def edit_questions( quiz ):
	question_index = util.get_option( "Select question to edit", list( map( lambda q: q.text, quiz.questions ) ) )
	question = quiz.questions[ question_index ]
	print( f"\n{question.text}" )
	options = [
		( "Edit text", edit_text ),
		( "Edit answers", edit_answers ),
		( "Edit correct answer", edit_correct_answer ),
		( "Edit concepts", edit_concepts )
	]
	option = util.get_option( "Enter selection", list( map( lambda o: o[ 0 ], options ) ) )
	options[ option ]( question )

def edit_text( quiz, question ):
	print( question.text )
	text = util.get_text( "Enter new text (blank to delete): " )
	if text == "":
		for q in quiz.questions:
			if q.text == question.text:
				quiz.questions.remove( q )
	else:
		text = question.text

def edit_answers( question ):
	print( question.text )
	question.text = util.get_text( "Enter new text: ", "Text cannot be blank" )

def edit_correct_answer( question ):
	pass

def edit_concepts( question ):
	pass

def save_changes( quiz ):
	quiz.save()

def undo_changes( quiz, data ):
	quiz.load( data )