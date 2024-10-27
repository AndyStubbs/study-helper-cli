from util import get_option


def main():
	print( "\nStudy Helper 1.0\n" )
	display_menu()


def display_menu():
	option = get_option( "Enter selection: ", menu )
	option[ 2 ]()


def run_quiz():
	print( "Running Quiz" )


def create_quiz():
	print( "Creating Quiz" )
	


def edit_quiz():
	print( "Editing Quiz" )


menu = [
	( "Run Quiz", "-r", run_quiz ),
	( "Create Quiz", "-c", create_quiz ),
	( "Edit Quiz", "-e", edit_quiz )
]


if __name__ == '__main__':
	main()
