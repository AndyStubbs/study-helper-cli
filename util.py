import ansi

def get_option( prompt, options ):
	for i in range( 0, len( options ) ):
		print( f"{i+1}. {options[i]}" )
	
	is_valid = False
	while not is_valid:
		msg = (
			ansi.Fore.YELLOW +
			f"{prompt} (1-{len(options)}): " +
			ansi.Style.RESET_ALL
		)
		menu_option = input( msg )
		if menu_option.isdigit():
			index = int( menu_option )
			if index > 0 and index < len( options ) + 1:
				return index - 1
		ansi.print_style(
			"Invalid Selection",
			ansi.Fore.RED + ansi.Style.BOLD
		)

def get_text( prompt, err_msg = "" ):
	is_valid = False
	while not is_valid:
		value = input( prompt )
		if value == "" and err_msg != "":
			print( err_msg )
		else:
			is_valid = True
	return value

