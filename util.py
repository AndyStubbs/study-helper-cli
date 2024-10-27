import shutil

def get_option( prompt, options ):
	terminal_size = shutil.get_terminal_size()

	for i in range( 0, len( options ) ):
		print( f"{i+1}. {options[i][0]}" )
	
	is_valid = False
	while not is_valid:
		menu_option = input( prompt )
		if menu_option.isdigit():
			index = int( menu_option )
			if index > 0 and index < len( options ) + 1:
				return options[ index - 1 ]
		print( "invalid selection" )
