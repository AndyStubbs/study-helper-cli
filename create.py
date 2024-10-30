import ansi
from quiz import Quiz, Question
from quizzes import quizzes
import util


def create_quiz():
	ansi.print_style( "\n== Creating Quiz ==\n", ansi.Fore.GREEN )
	quiz = Quiz()

	# Get the quiz name
	quiz.name = util.get_text( "Enter quiz name: ", "Name cannot be blank." )
	quiz.description = util.get_text( "Enter quiz description (blank to skip): " )
	
	# Get the quiz topic
	quiz.topic = util.get_text( "Enter quiz topic (blank to skip): " )
	
	# Get the questions"
	while True:
		question = create_new_question()
		print()
		if question == None:
			break
		else:
			quiz.questions.append( question )

	print( f"Quiz: {quiz.name} created with {len(quiz.questions)} questions." )
	quiz.save()
	quizzes.append( quiz )


def create_new_question():
	# Get the question text
	question_text = util.get_text( "Enter question text (blank to stop): " )
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
			return None
		else:
			print()

			# Get the correct answer
			ansi.print_style( question.text, ansi.Fore.WHITE2 )
			question.correct_answer = util.get_option(
				"Enter correct answer", question.answers
			)

			# Get the concepts
			concept_text = "not blank"
			while concept_text != "":
				concept_text = util.get_text( "Enter concept (blank to skip/stop): " )
				if concept_text != "":
					question.concepts.append( concept_text )
		return question
	return None