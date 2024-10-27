# flash-card-project
The Flash Card App is a simple, interactive tool designed to help users memorize French words. It uses a dynamic learning system that focuses on unfamiliar words to improve retention over time.

## Overview

This project utilizes Tkinter to create a flash card application where users can practice French vocabulary.

### Key Components
* Tkinter: Used to build the user interface.
* Window: The main application window that hosts all components.
* Flash Card: Displays a French word or its meaning.
* Buttons:
    * Check Mark: Marks the word as known.
    * Cross Mark: Flips the card to show the word’s meaning and adds it to the to_learn list.


### Features
* Word Memorization: Practice and memorize French words efficiently.
* Dynamic Learning: Unfamiliar words are reviewed multiple times until mastered.
* Persistent Progress: When reopening the app, it focuses on previously unlearned words.
* Simple UI: Intuitive interface built with Tkinter.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/flash-card-project.git
   cd flash-card-project

2. **Running the Application**:
   ```bash
   python main.py

### Interface
* Click Check Mark
<img width="594" alt="Screenshot 2024-10-27 at 5 54 16 PM" src="https://github.com/user-attachments/assets/6766252e-71bf-4156-a5bc-d8827a9c9caf">

* Click Cross Mark
<img width="594" alt="Screenshot 2024-10-27 at 5 54 28 PM" src="https://github.com/user-attachments/assets/2a1128c6-69aa-4d0f-beea-23465bfc0519">

The application presents a French word on each card. You can either:
* Click the Check Mark to pass the word if you know it.
* Click the Cross Mark to see the meaning and add the word to the to_learn list.
When reopening the app, only unfamiliar words from the previous session will be displayed.

## Instructions
* Learn Words: A French word appears on each flash card.
* Flip the Card: Click the cross mark to flip the card and see the meaning.
* Track Progress: Unfamiliar words are added to the to_learn list for future review.
* Restart Focus: On restarting the app, the focus remains on words that are still unfamiliar.

## Future Improvements
* Add more languages for broader learning options.
* Include a progress tracking feature to show overall mastery.

## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
