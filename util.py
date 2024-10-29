import os
import math
import ansi

def get_option( prompt, options, is_alpha = False ):
	if is_alpha:
		all_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		indices = []
		for i in range( 0, len( options ) ):
			indices.append( all_alpha[ i ] )
	else:
		indices = []
		for i in range( 1, len( options ) + 1 ):
			indices.append( str( i ) )
	print_columns( options, indices )
	is_valid = False
	while not is_valid:
		msg = (
			ansi.Fore.YELLOW +
			f"{prompt} ({indices[0]}-{indices[len(options)-1]}): " +
			ansi.Style.RESET_ALL
		)
		menu_option = input( msg )
		if menu_option != "":
			if not menu_option.isdigit():
				menu_option = menu_option.upper()
			if menu_option in indices:
				index = indices.index( menu_option )
				if index >= 0 and index < len( options ):
					return index
		ansi.print_style(
			"Invalid Selection",
			ansi.Fore.RED + ansi.Style.BOLD
		)

def get_text( prompt, err_msg = "" ):
	is_valid = False
	while not is_valid:
		value = input( prompt )
		if value == "" and err_msg != "":
			ansi.print_style(
				err_msg,
				ansi.Fore.RED + ansi.Style.BOLD
			)
		else:
			is_valid = True
	return value

def print_columns( options, indices ):
	if len( options ) <= 10:
		for i in range( 0, len( options ) ):
			if i < len( indices ):
				print( f"{indices[i]}. {options[i]}" )
			else:
				print( f"{options[i]}" )
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
					if index - 1 < len( indices ):
						option_text = f"{indices[index-1]}. {text}"
					else:
						option_text = f"{text}"
					padding = column_widths[ col ] - len( option_text )
					row_str += option_text + " " * padding
			print( row_str )
