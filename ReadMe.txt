1. Install Python 3.5
	default: C:\Users\[user]\AppData\Local\Programs\Python\Python35-32
	Add python to environment variables
2. Install PyAudio 0.2.10.py33
	wheel package: cmd window > pip install ..\PrarieDog\PyAudio-0.2.10-cp35-cp35m-win32.whl

	Linux:
		sudo apt-get install python-pyaudio
		
3. Modify member.config to include a distinct [ip]:[port] for each group member to connect (including self)
	(eg):
		192.168.1.6:8000
		192.168.1.7:8001

4. Run PrarieDog
	cmd window > python.exe ..\PrarieDog\Main.py
