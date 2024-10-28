import os
import math
import ansi

def get_option( prompt, options ):
	print_columns( options )
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

def print_columns( options ):
	if len( options ) <= 10:
		for i in range( 0, len( options ) ):
			print( f"{i+1}. {options[i]}" )
	else:
		# Calculate the number of columns and rows
		cols = math.ceil( len( options ) / 10 )
		rows = math.ceil( len( options ) / cols )
		terminal_width = os.get_terminal_size().columns
		
		# Adjust rows if max_col_width is too small
		while True:
			max_col_width = terminal_width // cols - 6
			if max_col_width > 10 or cols == 1:
				break
			rows += 1
			cols = math.ceil( len( options ) / rows )
		
		# Get column widths
		index = 0
		columns = [ [] for _ in range( rows ) ]
		column_widths = [ 0 ] * cols
		
		for col in range( 0, cols ):
			for row in range( 0, rows ):
				if index >= len( options ):
					break
				option_text = options[ index ]
				# Truncate the option text if it exceeds the max width
				if len( option_text ) > max_col_width:
					option_text = option_text[ : max_col_width - 3 ] + "..."
				if len( option_text ) + 6 > column_widths[ col ]:
					column_widths[ col ] = len( option_text ) + 6
				columns[ row ].append( ( index + 1, option_text ) )
				index += 1
		
		# Print each row across columns
		for row in range( rows ):
			row_str = ""
			for col in range( cols ):
				if row < len( columns ) and col < len( columns[ row ] ):
					index, text = columns[ row ][ col ]
					option_text = f"{index}. {text}"
					padding = column_widths[ col ] - len( option_text )
					row_str += option_text + " " * padding
			print( row_str )
