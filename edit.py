import ansi
import util
import create
from run import select_quiz
from quizzes import quizzes


def edit_quiz():
	if len( quizzes ) == 0:
		ansi.print_style( f"No quizzes to edit", ansi.Fore.RED2 )
		return
	ansi.print_style( "\n== Edit Quiz ==\n", ansi.Fore.GREEN )
	quiz_index = select_quiz()
	quiz = quizzes[ quiz_index ]
	edit_quiz_single( quiz )

def edit_quiz_single( quiz ):
	undo_data = quiz.serialize()
	is_editing = True
	while is_editing:
		delete_quiz_text = f"{ansi.Fore.RED2}Delete Quiz{ansi.Fore.RESET}"
		ansi.print_style( f"\n== Editing Quiz ==\n", ansi.Fore.GREEN )
		print( f"{ansi.Fore.YELLOW2}Name:{ansi.Fore.RESET} {quiz.name}" )
		print( f"{ansi.Fore.YELLOW2}Description:{ansi.Fore.RESET} {quiz.description}" )
		print( f"{ansi.Fore.YELLOW2}Topic:{ansi.Fore.RESET} {quiz.topic}" )
		print( f"{ansi.Fore.YELLOW2}Questions:{ansi.Fore.RESET} {len(quiz.questions)}\n" )
		options = [
			"Edit Name",
			"Edit Description",
			"Edit Topic",
			"Edit Questions",
			"Save Changes",
			"Undo Changes",
			delete_quiz_text
		]
		option = util.get_option( "Enter selection", options )
		print()
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
		elif options[ option ] == delete_quiz_text:
			delete_quiz( quiz )
			is_editing = False

def edit_quiz_name( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Name:{ansi.Fore.RESET} {quiz.name}" )
	quiz.name = util.get_text( "Enter new name: ", "Name cannot be blank" )

def edit_quiz_description( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Description:{ansi.Fore.RESET} {quiz.description}" )
	quiz.description = util.get_text( "Enter new description: " )

def edit_topic( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Topic:{ansi.Fore.RESET} {quiz.topic}" )
	quiz.topic = util.get_text( "Enter new topic: " )

def edit_questions( quiz ):
	create_new_question_text = f"{ansi.Fore.GREEN}Create new question{ansi.Fore.RESET}"
	questions = list( map( lambda q: q.text, quiz.questions ) )
	questions.append( create_new_question_text )
	questions.append( f"{ansi.Fore.RED2}Cancel{ansi.Fore.RESET}" )
	question_index = util.get_option( "Select question to edit", questions )
	print()
	if questions[ question_index ] == create_new_question_text:
		create_new_question( quiz )
		return
	if question_index >= len( quiz.questions ):
		return
	question = quiz.questions[ question_index ]
	print( f"{ansi.Fore.YELLOW2}Edit Question: {ansi.Fore.RESET} {question.text}" )
	options = [
		"Edit text",
		"Edit answers",
		"Edit correct answer",
		"Edit concepts",
		f"{ansi.Fore.RED2}Cancel{ansi.Fore.RESET}"
	]
	option = util.get_option( "Enter selection", options )
	print()
	if options[ option ] == "Edit question text":
		edit_text( quiz, question_index )
	elif options[ option ] == "Edit answers":
		edit_answers( question )
	elif options[ option ] == "Edit correct answer":
		edit_correct_answer( question )
	elif options[ option ] == "Edit concepts":
		edit_concepts( question )

def edit_text( quiz, question_index ):
	question = quiz.questions[ question_index ]
	print( f"{ansi.Fore.YELLOW2}Edit Text:{ansi.Fore.RESET} {question.text}" )
	text = util.get_text( "Enter new text (blank to delete): " )
	if text == "":
		del quiz.questions[ question_index ]
	else:
		text = question.text

def edit_answers( question ):
	ansi.print_style( f"Edit answers", ansi.Fore.YELLOW2 )
	answers = question.answers[ : ]
	answers.append( f"{ansi.Fore.RED2}Cancel{ansi.Fore.RESET}" )
	answer_index = util.get_option( "Select answer to edit", answers )
	print()
	if answer_index <= len( question.answers ):
		return
	new_answer = util.get_text( "Enter new answer (blank to delete): " )
	if new_answer == "":
		question.answers.remove( answer_index )
	elif new_answer < len( question.answers ):
		question.answers[ answer_index ] = new_answer

def edit_correct_answer( question ):
	ansi.print_style( f"Edit correct answer", ansi.Fore.YELLOW2 )
	answers = question.answers[ : ]
	answers.append( f"{ansi.Fore.RED2}Cancel{ansi.Fore.RESET}" )
	correct_answer = util.get_option( "Select correct answer", answers )
	print()
	if correct_answer < len( question.answers ):
		question.correct_answer = correct_answer

def edit_concepts( question ):
	pass

def create_new_question( quiz ):
	question = create.create_new_question()
	if question != None:
		quiz.questions.append( question )

def save_changes( quiz ):
	quiz.save()

def undo_changes( quiz, data ):
	quiz.load( data )

def delete_quiz( quiz ):
	quiz.delete()
	quizzes.remove( quiz )
