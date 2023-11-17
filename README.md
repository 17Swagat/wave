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




# ComponentFrame and Panels

This is the README file for the `ComponentFrame`, `SliderPanel`, and `OnOffSwitchPanel` classes. These components are part of a Python application built using the `customtkinter` library. The components provide a user interface for sliders and on/off switches with customizable styles.

## Table of Contents
- [Usage](#usage)
- [Component Structure](#component-structure)
- [License](#license)


## Usage

To use the `ComponentFrame`, `SliderPanel`, and `OnOffSwitchPanel` classes, follow these steps:

1. Import the required modules:

    ```python
    import customtkinter as ctk
    from appsettings import *
    ```

2. Create an instance of the desired component:

    ```python
    # Example for SliderPanel
    slider_panel = SliderPanel(parent, text, data_var, min_value, max_value)
    ```

    ```python
    # Example for OnOffSwitchPanel
    on_off_panel = OnOffSwitchPanel(parent, text, showVideo, showHandlandmarks, control_pc)
    ```

3. Use the component instance in your application.

## Component Structure

### `ComponentFrame` Class

The `ComponentFrame` class is a customized frame based on `customtkinter.CTkFrame`. It provides a consistent look for the components.

### `SliderPanel` Class

The `SliderPanel` class extends `ComponentFrame` and is designed to create a panel with a slider and corresponding numerical display.

#### Initialization

- Initializes the layout and sets up the slider and labels.

#### `update_text` Method

- Updates the numerical display based on the slider value.

### `OnOffSwitchPanel` Class

The `OnOffSwitchPanel` class extends `ComponentFrame` and creates a panel with on/off switches for various functionalities.

#### Initialization

- Initializes the layout and sets up on/off switches for webcam, hand landmarks, and PC control.

# Menu and Control Frames

This is the README file for the `Menu`, `ControlsFrame`, and `HelpFrame` classes. These classes are part of a Python application built using the `customtkinter` library. The components provide a menu structure, controls frame, and a help frame for the application.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Component Structure](#component-structure)
- [License](#license)

## Usage

To use the `Menu`, `ControlsFrame`, and `HelpFrame` classes, follow these steps:

1. Import the required modules:

    ```python
    import customtkinter as ctk
    from components import *
    ```

2. Create an instance of the `Menu` class:

    ```python
    menu = Menu(parent, mouse_smoothness, video_on_off, show_handlandmarks, pccontrol)
    ```

3. Use the menu instance in your application.

## Component Structure

### `Menu` Class

The `Menu` class extends `customtkinter.CTkTabview` and provides a tabbed menu structure for the application.

#### Initialization

- Initializes the menu with two tabs: 'Controls' and 'Help'.
- Sets up the `ControlsFrame` and `HelpFrame` as content for the respective tabs.

### `ControlsFrame` Class

The `ControlsFrame` class extends `customtkinter.CTkFrame` and creates a frame containing on/off switches, a slider, and a theme change option.

#### Initialization

- Initializes the layout and sets up on/off switches and sliders for controlling video, hand landmarks, and PC control.
- Adds a theme change option.

### `HelpFrame` Class

The `HelpFrame` class extends `customtkinter.CTkFrame` and creates a frame for displaying help-related content.

#### Initialization

- Initializes the layout with a red background (for illustration purposes).

## License

This project is licensed under the [MIT License](LICENSE).
