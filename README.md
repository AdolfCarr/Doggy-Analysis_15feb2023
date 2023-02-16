# Doggy-Analysis_15feb2023
#### This is a simple analysis for a group of dogs whose neighbours are my classmates. The python code was runned in an virtual enviroment in Visual Studio Code. ####

***To create the virtual enviroment in Visual Studio Code follow the next instructions:***

1. Open your project in Visual Studio Code.

2. Open the built-in terminal by pressing `Ctrl+Shift+`` (backtick), or by going to the "Terminal" menu and selecting "New Terminal".

3. In the terminal, navigate to your project directory using the cd command. 
For example, if your project is located in C:\Projects\myproject, you can type cd C:\Projects\myproject and press Enter.

4. Once you're in your project directory, you can create a virtual environment using the following command:

```
python -m venv myVirtualEnviroment
```

This will create a new virtual environment in a folder named **myVirtualEnviroment** within your project directory. 
Note that you can replace .venv with any other name you prefer for your virtual environment.

5. To activate the virtual environment in windows, type the following command in the terminal:

```
myVirtualEnviroment\Scripts\activate
```

After running this command, you should see the name of your virtual environment in the terminal prompt, indicating that it's currently active.

Note that you'll need to activate the virtual environment in each new terminal session before running any commands that require it.

That's it! You now have a new virtual environment set up in Visual Studio Code. You can install any necessary dependencies within the virtual environment using pip. 
When you're done working in the virtual environment, you can deactivate it using the deactivate command.

> Important: in order to run this practice you need to install: scipy, numpy matplotlib, pandas.

***How to run the practice?***

To run a Python file inside a virtual environment, you'll need to activate the virtual environment in your terminal first, and then run the Python file using the Python executable that's installed in the virtual environment.

Here are the steps to follow:

1. Open your project in Visual Studio Code.

2. Open the built-in terminal by pressing `Ctrl+Shift+`` (backtick), or by going to the "Terminal" menu and selecting "New Terminal".

3. Activate your virtual environment in the terminal using the command:

```
myVirtualEnviroment\Scripts\activate
```

4. Once the virtual environment is activated, you can run your Python file using the following command:

```
python path/to/your/file.py
```

Replace path/to/your/file.py with the actual path to your Python file. 
For example, if your file is located in the project directory and is named my_script.py, you can run it using the command:

```
python my_script.py
```

This will run your Python file using the Python executable that's installed in the virtual environment.

Note that if your Python file has any dependencies, make sure that they're installed in the virtual environment before running the file. 
You can install dependencies using pip while the virtual environment is activated.

That's it! You should now be able to run your Python file inside your virtual environment.

***How to install dependencies on this virtual enviroment?***

To run a Python file inside a virtual environment, you'll need to activate the virtual environment in your terminal first, and then run the Python file using the Python executable that's installed in the virtual environment.

Here are the steps to follow:

1. Open your project in Visual Studio Code.

2. Open the built-in terminal by pressing `Ctrl+Shift+`` (backtick), or by going to the "Terminal" menu and selecting "New Terminal".

3. Activate your virtual environment in the terminal using the command:

```
myVirtualEnviroment\Scripts\activate
```
4. Once the virtual environment is activated, you can install numpy using the following command:

```
pip install numpy
```

This command will download and install TensorFlow and all its dependencies in your virtual environment.

5. After the installation is complete, you can test that numpy is installed correctly by opening a Python shell within your virtual environment, and importing numpy using the following command:

```
import numpy as np
```

If there are no error messages, numpy has been successfully installed in your virtual environment.

That's it! You should now be able to use numpy within your virtual environment. Remember to activate the virtual environment in your terminal each time you want to use numpy or any other package installed in the virtual environment.

