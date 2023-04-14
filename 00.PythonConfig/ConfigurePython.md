# When, Where, and How To Install Python?
- ***Whenever*** you decide to start your journey in any branch of the IT industry! ⌚
- In ***any environment*** you enjoy (GNU Linux, Windows, macOS, and even Android)! 🖥️💻📱
- It's ***easy***, let me show you: 😊
    1. [Python-Offical-Website-Downloads](https://www.python.org/downloads/) 🐍
    2. Find the environment you want to use Python in it and follow the instructions... Thats it! 🤷‍♂️
---
## Anaconda Distribution
*It is still Python but with extra stuff!*  
- Long story short it's Python plus powerful scientific computing and data science libraries! 🐍➕🧑‍🔬
- Easy to install and work with but not my concern! 😒
---
## Can I we have our own Python isolated environments with its own Python interpreter and packages?

**Of course, we can!** 🤩

Let me show you how: 😎

1. Ask Python gently to create an virtual environment wherever you want: 🤫  
**Unix based**  
`python -m venv wow`  
**Windows**  
`py -m venv wow`   
***USE THE PROPER NAME FOR YOUR 'venv'!**
2. Activate the environment: 🎬  
**Unix based**  
`source wow/bin/activate`  
**Windows**  
`.\wow\Scripts\activate`
3. Install what you need: 🫵  
**Unix based + Windows**  
`pip install Faker`
4. Enjoy your **venv** (isolated virtual environment) as long as you need: 🤯   
**Unix based**  
`Python`  
**Windows**  
`py`  
**(You are in the Python realm! 🐍😍)**  
`from faker import Faker`    
`fake = Faker()`  
`fake.name()`  
`fake.address()`  
`fake.text()`  
`exit()`  
5. Deactivate the **venv** do other stuff: 🍔🍟🛹  
**Unix based + Windows**  
`deactivate`  
6. Share your script and venv config: 😊  
**Unix based + Windows**  
Create  a file with **'.py'** extension start your journey as a Python developer!  
*In the same '01.PythonBasics' section there is a directory named 'letsBeFake', open it, please.!*
---
***Like any software, keep your 'pip' up to date!*** 📅  
**Unix based**  
`python -m pip install --upgrade pip`  
**Windows**  
`py -m pip install --upgrade pip`  
