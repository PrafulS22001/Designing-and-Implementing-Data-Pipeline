# Week 1

This folder contains the basic start to Filehandling and serialization. It contains 5 folders where it is shown in step by step on how it works. 
___

## 📁 Description of Folders

Below you can expand each section to see what the folder contains and what the files do.

---

<details>
<summary><strong>File-Handling</strong></summary>

**Path:** `./File-Handling/` <br>
**Contains:**  
- `file.py`

**Description:**  
This folder contains one file that has a brief introduction to the general file-handling.<br>
In this task, there is a single class "Test" and know the difference between single and double underscore.<br>
- **file.py** <br>
file.py has the following aspect: <br>
    • Proprties <br>
        o __x : int <br>

Returning None and printing x from class Test and knowing the way to print __x from the function. 

</details>

---

<details>
<summary><strong>Deserialization</strong></summary>

**Path:** `./Deserialization/` <br>
**Contains:**  
- `file_handler.py`
- `inventory.csv`
- `item.py`
- `main.py`

**Description:**  
- **file_handler.py** <br>
    - Write object-oriented main program
    - Define FileHandler class
         - filepath: str
         - read(self) -> list[str] # rows
    - Use FileHandler in main program to read inventory.csv
    - Print file content into the console

Count should be initialized to 0 value inside the constructor. addCount method should increment the __count property. getCount method returns the count value. zeroCount method modifies the count value back to 0. <br>
- **main.py**<br>
Import file_handler and item class into the main function 
    - Write object-oriented main program
    - Define FileHandler class
         - filepath: str
         - read(self) -> list[str] # rows
    - Use FileHandler in main program to read inventory.csv
    - Print file content into the console


</details>

---

<details>
<summary><strong>Serialization</strong></summary>

**Path:** `./serialization/`
**Contains:**  
- `file_handler.py`
- `inventory.csv`
- `item.py`
- `main.py`

**Description:**  
- **temperature_converter.py** <br>
This file should have a single class called TemperatureConverter with the following aspects: <br>
    • Properties:<br>

        o __temperature: float <br>

    • Methods: <br>

        o setTemperature(temp: float) -> None<br>
        o toCelsius() -> float<br>
        o toFahrenheit() -> float<br>
        o toKelvin() -> float<br>

The __temperature property should be initialized to 0.0 inside the constructor. The setTemperature method should set the __temperature property. The toCelsius, toFahrenheit, and toKelvin methods should convert the temperature to Celsius, Fahrenheit,
and Kelvin, respectively. <br>
- **main.py** <br>
This file imports the TemperatureConverter class from the temperature_converter.py file and creates an object from it. 
</details>

---

<details>
<summary><strong>writeToFile</strong></summary>

**Path:** `./writeToFile/`  
**Contains:**  
- `construction_example.py`
- `Example_lib.py`
- `Example_main.py`
- `oop1.py`
- `oop2.py`
- `sodaBottle.py`

**Description:**  
This folder contains small Python examples that demonstrate core programming and OOP concepts.

</details>

---

<details>
<summary><strong>Inventory</strong></summary>

**Path:** `./Understanding/`  
**Contains:**  
- `construction_example.py`
- `Example_lib.py`
- `Example_main.py`
- `oop1.py`
- `oop2.py`
- `sodaBottle.py`

**Description:**  
This folder contains small Python examples that demonstrate core programming and OOP concepts.

</details>

---