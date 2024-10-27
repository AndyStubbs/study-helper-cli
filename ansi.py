import os
import sys

# Foreground color codes
class Fore:
	BLACK    = "\033[30m"
	RED      = "\033[31m"
	GREEN    = "\033[32m"
	YELLOW   = "\033[33m"
	BLUE     = "\033[34m"
	MAGENTA  = "\033[35m"
	CYAN     = "\033[36m"
	WHITE    = "\033[37m"
	RESET    = "\033[39m"
	BLACK2   = "\033[90m"
	RED2     = "\033[91m"
	GREEN2   = "\033[92m"
	YELLOW2  = "\033[93m"
	BLUE2    = "\033[94m"
	MAGENTA2 = "\033[95m"
	CYAN2    = "\033[96m"
	WHITE2   = "\033[97m"
	RESET    = "\033[39m"

# Background color codes
class Back:
	BLACK   = "\033[40m"
	RED     = "\033[41m"
	GREEN   = "\033[42m"
	YELLOW  = "\033[43m"
	BLUE    = "\033[44m"
	MAGENTA = "\033[45m"
	CYAN    = "\033[46m"
	WHITE   = "\033[47m"
	RESET   = "\033[49m"

# Text style codes
class Style:
	RESET_ALL  = "\033[0m"
	BOLD       = "\033[1m"
	DIM        = "\033[2m"
	UNDERLINED = "\033[4m"
	INVERTED   = "\033[7m"
	HIDDEN     = "\033[8m"
	RESET_BOLD = "\033[21m"
	RESET_DIM  = "\033[22m"
	RESET_UNDERLINED = "\033[24m"
	RESET_INVERTED   = "\033[27m"
	RESET_HIDDEN     = "\033[28m"

is_color_supported = None

def print_style( msg, color ):
	"""
	Print styled text if it is supported.
	"""
	global is_color_supported
	if is_color_supported is None:
		is_color_supported = check_color_support()
	if is_color_supported:
		print( f"{color}{msg}{Style.RESET_ALL}" )
	else:
		print( msg )

def check_color_support():
	"""
	Checks if the terminal supports ANSI color codes.
	If not it attempts to enable virtual terminal mode.
	"""
	# Check if the output is a terminal
	if not sys.stdout.isatty():
		return False

	if os.name == "nt":
		if "WT_SESSION" in os.environ or "ANSICON" in os.environ:
			return True
		return is_virtual_terminal_enabled()
	else:
		return True

def is_virtual_terminal_enabled():
	"""
	Attempt to enable virtual terminal for additional ANSI support in
	windows.
	"""
	# Attempt to enable Virtual Terminal Processing in Windows
	try:
		import ctypes
		kernel32 = ctypes.windll.kernel32
		handle = kernel32.GetStdHandle( -11 )

		# Enable Virtual Terminal Processing
		mode = ctypes.c_uint32()
		if kernel32.GetConsoleMode( handle, ctypes.byref( mode ) ):
			if not ( mode.value & 0x0004 ):
				# 0x0004 is the flag for ENABLE_VIRTUAL_TERMINAL_PROCESSING
				kernel32.SetConsoleMode( handle, mode.value | 0x0004 )
			return True
	except Exception:
		return False