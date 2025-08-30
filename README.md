# ⚽ Player Record Function

A command-line script that demonstrates a flexible Python function for displaying a soccer player's name and goal count. The script includes robust input handling for user-provided data.

## Features

* **Flexible Function**: The `record()` function uses optional parameters with default values (`player='<unknown>'`, `goals=0`), so it can be called in multiple ways.
* **Input Sanitization**: The script checks if the goal input is a valid number; if not, it defaults to 0. It also handles cases where the player's name is left blank.
* **Well-Documented**: Includes a docstring to explain the function's purpose, which can be viewed with `help()`.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `player_record.py`).
3.  Run the script from your terminal:
    ```sh
    python player_record.py
    ```
4.  The program will prompt you for a player's name and their goal count.

### Example 1: Full Input

```sh
> python player_record.py
Player Name:
Ronaldo
Goals Scored:
800
The player Ronaldo scored 800 goals
```

### Example 2: Blank Name

```sh
> python player_record.py
Player Name:

Goals Scored:
50
The player <unknown> scored 50 goals
```

### Example 3: Non-Numeric Goals

```sh
> python player_record.py
Player Name:
Messi
Goals Scored:
a lot
The player Messi scored 0 goals
```
