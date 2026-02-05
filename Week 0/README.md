# Week 0 

This folder contains the basic introduction to OOP and understanding the basic structure. Week 0 is filled with trial files where I am starting to mess around and figure out the possibilities of constrution and libraries.
___

## 📁 Description of Folders

Below you can expand each section to see what the folder contains and what the files do.

---

<details>
<summary><strong>Coin_Acceptor</strong></summary>

**Path:** `./coin_acceptor/`
**Contains:**  
- `coin_acceptor.py`
- `main3.py`
- `main4.py`

**Description:**  
Coin acceptor purpose is to count the amount of inserted coins.<br>
In this task, create class “CoinAcceptor”, initialize object from it and use the object with commands from the main program.<br>
- **coin_acceptor.py** <br>
Coin acceptor should have following aspects:<br>
    • Properties <br>
        o __amount: int <br>
        o __value: float <br>
    • Methods
        o insertCoin() -> None <br>
        o getAmount() -> int <br>
        o returnCoins() -> int <br>

Returning coins should return the amount of coins. <br>
- **main3.py** <br>
Imports the “CoinAcceptor” class from the “coin_acceptor.py” file and creates one object from it. Main program flow can be seen
from the example run below.

- **main4.py** <br>

</details>

---

<details>
<summary><strong>Counter</strong></summary>

**Path:** `./counter/`
**Contains:**  
- `Counter.py`
- `main.py`

**Description:**  
- **counter.py** <br>
Should have only one class called “Counter”, with following aspects: <br>
    - Properties<br>
        o __count: int
    -  Methods
        o addCount() -> None <br>
        o getCount() -> int <br>
        o zeroCount() -> None <br>

Count should be initialized to 0 value inside the constructor. addCount method should increment the __count property. getCount method returns the count value. zeroCount method modifies the count value back to 0. <br>
- **main.py**<br>
Imports the “Counter” class from the “counter.py” file and creates one object from it. Main program prompts continuously the
user for one of the following actions:
    1. Add count
    2. Get count
    3. Zero count
    4. Exit program

</details>

---

<details>
<summary><strong>Temp-converter</strong></summary>

**Path:** `./temp-converter/`
**Contains:**  
- `main2.py`
- `temperature_converter.py`

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
<summary><strong>Understanding</strong></summary>

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