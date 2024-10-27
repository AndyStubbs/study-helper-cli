import shutil


size = shutil.get_terminal_size()
width = size.columns
height = size.lines


def get_option( prompt, options ):
	terminal_size = shutil.get_terminal_size()

	print_options( options )

	is_valid = False
	while not is_valid:
		menu_option = input( prompt )
		if menu_option.isdigit():
			index = int( menu_option )
			if index > 0 and index < len( options ) + 1:
				return options[ index - 1 ]
		print( "invalid selection" )



# Print the options justified by the screen length
def print_options( options ):
	terminal_size = shutil.get_terminal_size()

	# Default padding for options
	pad_left = 3
	pad_right = 3

	# If the options are double digits the add padding
	if len( options ) >= 10:
		num_len = 5
	else:
		num_len = 4

	# Get the maximum length of the option text - including padding
	max_length = 0
	for i in range( 0, len( options ) ):
		option_len = len( options[ i ][ 0 ] )
		total_len = pad_left + num_len + pad_right + option_len
		if total_len > terminal_size.columns:
			option_len = terminal_size.columns - ( pad_left + num_len + pad_right )
		if option_len > max_length:
			max_length = option_len

	print_line( "*-*" )
	# Print the options justified to the maximum length
	for i in range( 0, len( options ) ):
		
		# Get the number part
		num_part = " " * pad_left + f"{i + 1} - "

		# Get the option part
		option_part = options[ i ][ 0 ]
		if len( option_part ) > max_length:
			option_part = option_part[ :max_length - 3 ] + "..."

		# Pad the output
		padding = ( terminal_size.columns - max_length ) // 2
		print_b( " " * padding + num_part + option_part )


def print_line( border = "*─*" ):
	line = border[ 1 ] * ( width - 2 )
	print( f"{border[0]}{line}{border[2]}" )


def print_b( msg, border_left = "│", border_right = "│" ):
	padded_msg = msg.center( width - 2 )
	print( f"{border_left}{padded_msg}{border_right}" )