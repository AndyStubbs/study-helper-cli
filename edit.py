import ansi
import util
import create
from quizzes import quizzes, select_quiz


def edit_quiz():
	if len( quizzes ) == 0:
		ansi.print_style( f"No quizzes to edit", ansi.Fore.RED2 )
		return
	ansi.print_style( "\n== Edit Quiz ==\n", ansi.Fore.GREEN )
	quiz_index = select_quiz()
	if quiz_index >= len( quizzes ):
		return
	quiz = quizzes[ quiz_index ]
	edit_quiz_single( quiz )

def edit_quiz_single( quiz ):
	undo_data = quiz.serialize()
	is_editing = True
	while is_editing:
		delete_quiz_text = f"{ansi.Fore.RED2}Delete Quiz{ansi.Fore.RESET}"
		save_changes_text = f"{ansi.Fore.GREEN}Save Changes{ansi.Fore.RESET}"
		undo_changes_text = f"{ansi.Fore.MAGENTA2}Back (Undo){ansi.Fore.RESET}"
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
			save_changes_text,
			undo_changes_text,
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
		elif options[ option ] == save_changes_text:
			save_changes( quiz )
			is_editing = False
		elif options[ option ] == undo_changes_text:
			undo_changes( quiz, undo_data )
			is_editing = False
		elif options[ option ] == delete_quiz_text:
			delete_quiz( quiz )
			is_editing = False

def edit_quiz_name( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Name:{ansi.Fore.RESET} {quiz.name}" )
	name = util.get_text( "Enter new name (blank to cancel): " )
	if name != "":
		quiz.name = name

def edit_quiz_description( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Description:{ansi.Fore.RESET} {quiz.description}" )
	quiz.description = util.get_text( "Enter new description: " )

def edit_topic( quiz ):
	print( f"{ansi.Fore.YELLOW2}Edit Topic:{ansi.Fore.RESET} {quiz.topic}" )
	quiz.topic = util.get_text( "Enter new topic: " )

def edit_questions( quiz ):
	ansi.print_style( f"Editing Questions", ansi.Fore.YELLOW2 )
	create_new_question_text = f"{ansi.Fore.GREEN}Create new question{ansi.Fore.RESET}"
	questions = list( map( lambda q: q.text, quiz.questions ) )
	questions.append( create_new_question_text )
	questions.append( f"{ansi.Fore.MAGENTA2}Back{ansi.Fore.RESET}" )
	question_index = util.get_option( "Select question to edit", questions )
	print()
	if questions[ question_index ] == create_new_question_text:
		create_new_question( quiz )
		return
	if question_index >= len( quiz.questions ):
		print("Go Back")
		return
	question = quiz.questions[ question_index ]
	print( f"{ansi.Fore.YELLOW2}Edit Question: {ansi.Fore.RESET} {question.text}" )
	options = [
		"Edit question text",
		"Edit answers",
		"Edit correct answer",
		"Edit concepts",
		f"{ansi.Fore.MAGENTA2}Back{ansi.Fore.RESET}"
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
	while True:
		ansi.print_style( f"Edit answers", ansi.Fore.YELLOW2 )
		answers = question.answers[ : ]
		add_new_answer_text = f"{ansi.Fore.GREEN}Add new answers{ansi.Fore.RESET}"
		back_answer_text = f"{ansi.Fore.RED}Back{ansi.Fore.RESET}"
		answers.append( add_new_answer_text )
		answers.append( back_answer_text )
		answer_index = util.get_option( "Select answer to edit", answers )
		print()
		if answers[ answer_index ] == add_new_answer_text:
			create.create_new_answers( question )
			continue
		elif answers[ answer_index ] == back_answer_text:
			return
		print( f"{ansi.Fore.YELLOW2}Edit Answer:{ansi.Fore.RESET} {answers[answer_index]}" )
		new_answer = util.get_text( "Enter updated answer (blank to delete): " )
		if new_answer == "":
			question.answers.remove( answers[ answer_index ] )
		else:
			question.answers[ answer_index ] = new_answer

def edit_correct_answer( question ):
	ansi.print_style( f"Edit correct answer", ansi.Fore.YELLOW2 )
	answers = question.answers[ : ]
	answers.append( f"{ansi.Fore.MAGENTA2}Back{ansi.Fore.RESET}" )
	correct_answer = util.get_option( "Select correct answer", answers )
	print()
	if correct_answer < len( question.answers ):
		question.correct_answer = correct_answer

def edit_concepts( question ):
	while True:
		ansi.print_style( f"Edit concepts", ansi.Fore.YELLOW2 )
		concepts = question.concepts[ : ]
		add_new_concept_text = f"{ansi.Fore.GREEN}Add new concepts{ansi.Fore.RESET}"
		back_concept_text = f"{ansi.Fore.MAGENTA2}Back{ansi.Fore.RESET}"
		concepts.append( add_new_concept_text )
		concepts.append( back_concept_text )
		concept_index = util.get_option( "Select a concept to edit", concepts )
		print()
		if concepts[ concept_index ] == add_new_concept_text:
			create.create_new_concepts( question )
			continue
		elif concepts[ concept_index ] == back_concept_text:
			return
		print( f"{ansi.Fore.YELLOW2}Edit Concept:{ansi.Fore.RESET} {concepts[concept_index]}" )
		new_concept = util.get_text( "Enter updated concept (blank to delete): " )
		if new_concept == "":
			question.concepts.remove( concepts[ concept_index ] )
		else:
			question.concepts[ concept_index ] = new_concept

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
