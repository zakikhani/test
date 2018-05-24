# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.WaitForString("HAR-BDF-C651>")
	crt.Screen.Send(chr(13))
	crt.Screen.Send("en" + chr(13))
	crt.Screen.WaitForString("password: ")
	crt.Screen.Send("Jigargeo1@" + chr(13))

Main()
