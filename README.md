# Wave Application

The Wave application, a graphical user interface (GUI) program built using Python. The Wave application provides functionality related to computer vision, webcam control, and menu settings.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Application Structure](#application-structure)
- [License](#license)

## Dependencies

Before running the Wave application, ensure you have the dependencies as specified in the `requirements.txt` file

## Installation

To install the required dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

Make sure you have [pip](https://pip.pypa.io/en/stable/installation/) installed before running the above command.

## Usage

To use the Wave application, follow these steps:

1. Import the required modules:

    ```python
    import customtkinter as ctk
    from appsettings import *
    from menu import Menu
    from vid_nd_control import WebCamView
    from appsettings import *
    ```

2. Create an instance of the `App` class:

    ```python
    if __name__ == '__main__':
        App()
    ```

3. Run the application.

## Application Structure

### `App` Class

The `App` class is the main class of the Wave application. It inherits from `customtkinter.CTk` and initializes the GUI, layout, and various settings.

#### Initialization

- Initializes `customtkinter.CTk` settings.
- Sets the window size and title.
- Configures the layout of the application.

#### Layout

- Configures the layout using the `columnconfigure` and `rowconfigure` methods.

#### Computer Vision and Webcam Control

- Initializes and sets up the `WebCamView` class for computer vision and webcam control.

#### Menu

- Initializes and sets up the `Menu` class for handling menu settings.

#### Main Loop

- Runs the main event loop using `self.mainloop()`.

#### Parameter Initialization

- Initializes Tkinter variables for video control, hand landmark recognition, PC control, and mouse smoothness.

### `init_parameters` Method

- Initializes Tkinter variables for the application.
