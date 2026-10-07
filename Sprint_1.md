# Sprint 1

The goal for this sprint is to establish user stories and their respective acceptance criteria.

The first two of the user stories were created by Claude, along with their respective acceptance criteria. Screenshots are provided below, along with the corrections I made regarding incorrect conclusions and my reasoning for those corrections.

## 1. User Stories

**User Story Template:** As a &lt;role&gt;, I want &lt;goal&gt; [so that &lt;benefit&gt;]

| ID | User Story Name | User Story Description | Priority | Estimated effort (hours) |
|---|---|---|---|---|
| 1 | Choose a board size | As a player, I want to choose the board size (an odd number from 7 to 21) so that I can play a quicker or a more challenging game. | High | 3 |
| 2 | Choose the board type | As a player, I want to choose between the English, Hexagon, and Diamond board types so that I can play different board layouts. | Medium | 3 |
| 3 | Start a new game of the chosen board size and type | As a player, I want to be able to start a new game, so that I can play the game. | Medium | 2 |
| 4 | Make a move in a game | As a player, I want the ability to make moves within the game, so that I can progress in the game. | High | 4 |
| 5 | A game is over | As a player, I want to know when the game is over, so that I can celebrate when I win and play again. | Low | 4 |

## 2. Acceptance Criteria (AC)

| User Story | AC ID | Description of Acceptance Criterion | Status |
|---|---|---|---|
| 1. Choose a board size | 1.1 | **Default size.**<br>Given the game has just launched,<br>When the main screen is displayed,<br>Then the board size field shows 7. | To-Do |
| 1. Choose a board size | 1.2 | **Valid size.**<br>Given the game screen is displayed,<br>When I enter an odd whole number from 7 to 21 (for example 9) and press New Game,<br>Then a board of size 9 is displayed. | To-Do |
| 1. Choose a board size | 1.3 | **Even size rejected.**<br>Given the game screen is displayed,<br>When I enter an even number (for example 8) and press New Game,<br>Then an error message says the size must be an odd number from 7 to 21, and the current board is unchanged. | To-Do |
| 1. Choose a board size | 1.4 | **Out-of-range size rejected.**<br>Given the game screen is displayed,<br>When I enter an odd number outside the range (for example 5 or 23) and press New Game,<br>Then the same error message appears and the current board is unchanged. | To-Do |
| 1. Choose a board size | 1.5 | **Invalid input rejected.**<br>Given the game screen is displayed,<br>When I leave the size field empty or enter non-numeric text and press New Game,<br>Then the same error message appears and the current board is unchanged. | To-Do |
| 1. Choose a board size | 1.6 | **Change applies on New Game.**<br>Given a game is in progress,<br>When I change the size value without pressing New Game,<br>Then the board on screen and the game state do not change. | To-Do |
| 1. Choose a board size | 1.7 | **Largest board fits.**<br>Given the application window is at least 1280x720 pixels and the size is 21,<br>When I press New Game,<br>Then all cells of the board are visible without scrolling. | To-Do |
| 1. Choose a board size | 1.8 | **Malicious or unexpected input.**<br>Given the game screen is displayed,<br>When I enter unexpected input in the size field (for example 9.5, 1e3, a very long string, or &lt;script&gt;alert(1)&lt;/script&gt;) and press New Game,<br>Then the input is rejected with the standard error message, the current board is unchanged, and the application does not crash. | To-Do |
| 2. Choose the board type | 2.1 | **Default type.**<br>Given the game has just launched,<br>When the main screen is displayed,<br>Then English is selected. | To-Do |
| 2. Choose the board type | 2.2 | **Single selection.**<br>Given the game screen is displayed,<br>When I select a board type,<br>Then exactly one type is selected and the others are deselected. | To-Do |
| 2. Choose the board type | 2.3 | **Selected type is used.**<br>Given a valid size is entered,<br>When I select Hexagon (or Diamond) and press New Game,<br>Then a board of that type is displayed at the chosen size. | To-Do |
| 2. Choose the board type | 2.4 | **Change applies on New Game.**<br>Given a game is in progress,<br>When I select a different board type without pressing New Game,<br>Then the board on screen and the game state do not change. | To-Do |
| 2. Choose the board type | 2.5 | **Size and type are independent.**<br>Given the size and type are selected,<br>When I change one of them,<br>Then the other keeps its value. | To-Do |
| 3. Start a new game of the chosen board size and type | 3.1 | **Player selects new game.**<br>Given the board’s current positions,<br>When the player selects new game,<br>Then the board resets current board to ready state. | To-Do |
| 3. Start a new game of the chosen board size and type | 3.2 | **Confirm board is in ready state.**<br>Given the board’s current state,<br>When the player starts a new game<br>And the board is filled,<br>Then flash a banner stating ready to play. | To-Do |
| 3. Start a new game of the chosen board size and type | 3.3 | **Remove banner.**<br>Given ready to play banner is displayed,<br>When two seconds has hit,<br>Then remove banner. | To-Do |
| 4. Make a move in a game | 4.1 | **Player picks up a peg.**<br>Given player has picked up a peg,<br>When player moves mouse,<br>Then peg follows the mouse. | To-Do |
| 4. Make a move in a game | 4.2 | **Valid orthogonal jump.
Given the player has picked up a peg,
When the peg is set down in an empty hole two cells away, directly up, down, left, or right,
And the cell between them holds a peg,
Then the peg stays in the empty hole,
And the jumped peg is removed,
And the total peg count decreases by one.**<br> | To-Do |
| 4. Make a move in a game | 4.3 | **Valid diagonal jump.
Given the player has picked up a peg,
When the peg is set down in an empty hole two cells away on a diagonal,
And the cell between them holds a peg,
Then the peg stays in the empty hole,
And the jumped peg is removed,
And the total peg count decreases by one.**<br> | To-Do |
| 4. Make a move in a game | 4.4 | **Destination is occupied.
Given the player has picked up a peg,
When the peg is set down on a hole that already holds a peg,
Then the move is rejected,
And the board returns to its state before the move.**<br> | To-Do |
| 4. Make a move in a game | 4.5 | **No peg to jump.
Given the player has picked up a peg,
When the peg is set down in an empty hole two cells away,
And the cell between them is an empty hole,
Then the move is rejected,
And the board returns to its state before the move.**<br> |  |
| 4. Make a move in a game | 4.6 | **Wrong distance or direction.
Given the player has picked up a peg,
When the peg is set down in an empty hole that is not exactly two cells away in a straight line (for example one cell away, three cells away, or a knight's move away),
Then the move is rejected,
And the board returns to its state before the move.**<br> |  |
| 4. Make a move in a game | 4.7 | **Peg set down outside the board.
Given the player has picked up a peg,
When the peg is set down outside the board, including empty areas inside the grid that are not part of the chosen board type,
Then the move is rejected,
And the board returns to its state before the move.**<br> |  |
| 5. A game is over | 5.1 | **Player’s move is complete.**<br>Given player has made a valid move,<br>When peg is set,<br>Then check board for other pegs. | To-Do |
| 5. A game is over | 5.2 | **Exactly one peg on board.**<br>Given only one peg on the board,<br>When check board has completed,<br>Then player wins game,<br>And display message with option to restart game. | To-Do |
| 5. A game is over | 5.3 | **Only two pegs on board.**<br>Given only two pegs on board<br>And no other moves can be made,<br>When check board has completed,<br>Then player has partial win.<br>And display message with option to restart game. | To-Do |
| 5. A game is over | 5.4 | **No other plays left.**<br>Given no other valid plays on board<br>And more than two pegs left,<br>When check board has completed,<br>Then player loses.<br>And display message with option to restart game. | To-Do |
| 5. A game is over | 5.5 | **Game over**<br>Given displayed message,<br>When banner timer hits five seconds,<br>Then change board to default. | To-Do |

## 3. Notes and LLM Screenshots

Changed priority level of 2 to medium. Otherwise, the output seems decent and reasonable. I did make some minor edits to the layout to match the slides and some language edits.

During the process of having Claude turn the word document into a markdown it called out that instead of naming each type of move I cut a corner using the terms “Valid move” and “invalid move”. I made a request for Claude to make the acceptance criteria for that as well.

<img width="428" height="417" alt="image" src="https://github.com/user-attachments/assets/dd9384bc-3660-495d-8780-1ddda0cb78be" />
<img width="426" height="424" alt="image" src="https://github.com/user-attachments/assets/979a5b40-ef9a-40d2-b027-1152ec6e075a" />
<img width="435" height="497" alt="image" src="https://github.com/user-attachments/assets/05ccc986-f42f-4678-97ff-e48a42152ed6" />
<img width="437" height="494" alt="image" src="https://github.com/user-attachments/assets/56b81dd3-3609-4adc-887a-4805a39087f1" />
<img width="427" height="463" alt="image" src="https://github.com/user-attachments/assets/4e728c17-dfbf-49ec-a2c6-25a791838e8b" />
<img width="418" height="455" alt="image" src="https://github.com/user-attachments/assets/580ac106-a267-43a3-9bb2-03ce35eb935c" />
<img width="418" height="372" alt="image" src="https://github.com/user-attachments/assets/82099ddd-ae70-4cc1-8fc8-88d149a9ff7e" />
<img width="332" height="368" alt="image" src="https://github.com/user-attachments/assets/fe8f648e-8d51-42ce-84f7-66ade6571b9f" />
<img width="428" height="457" alt="image" src="https://github.com/user-attachments/assets/11ace9c2-8c32-4a1a-9384-3c830ad92b73" />
<img width="391" height="456" alt="image" src="https://github.com/user-attachments/assets/4129a339-4161-497f-907d-3bce329c9cf2" />
<img width="428" height="484" alt="image" src="https://github.com/user-attachments/assets/623d31a0-5bfa-4f6b-872f-b39f68623acc" />
<img width="469" height="464" alt="image" src="https://github.com/user-attachments/assets/8c7704df-bb04-4d54-ac16-d5a02fc37311" />
<img width="525" height="588" alt="image" src="https://github.com/user-attachments/assets/d27ccdf0-b9d4-4174-aaa6-d10d4ea24ba1" />


