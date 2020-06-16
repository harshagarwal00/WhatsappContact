Reference
----------
Code reference: https://medium.com/@deavenditama/simple-whatsapp-automation-using-python3-and-selenium-77dad606284b
Appropritate Chromedriver downloaded from [Driver](http://chromedriver.storage.googleapis.com/index.html) 


Setup
----------
 - First of all, install [Python 3](https://www.python.org/downloads/) into your machine. I used python 3.7

 - Install PIP & install selenium:
   ```
	python3.7  get-pip.py		
	pip3.7 install selenium
   ```	

 - Install chrome version 84 [version of google chrome](https://www.google.com/chrome/beta/).
 


Configure the script
----------
``` 
 modify contacts (make sure to write exact and complete name of person)
 modify msg
```

#Run
```
source setup.sh
```

Running script (Currently only tested on MAC)
---------
After that run the script by runing 

```
python3.7 whatsapp_message.py
```
