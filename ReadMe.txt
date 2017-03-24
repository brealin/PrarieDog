1. Install Python 3.5
	Windows:
		default: C:\Users\[user]\AppData\Local\Programs\Python\Python35-32
		Add python to environment variables
2. Install PyAudio 0.2.10.py33
	Windows:
		if you need wheel package: 
			cmd window > pip install ..\PrarieDog\PyAudio-0.2.10-cp35-cp35m-win32.whl
	Debian/Ubuntu:
		Use the package manager to install PyAudio:
			sudo apt-get install python-pyaudio python3-pyaudio

		If the latest version of PyAudio is not available, install it using pip:
			pip install pyaudio
3. Run PrarieDog
	Windows:
		cmd window > python.exe ..\PrarieDog\Main.py