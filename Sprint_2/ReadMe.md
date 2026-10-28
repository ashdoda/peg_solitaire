**Sprint 2**

**Demonstration Video:**

[Video Link](https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d21808c4-2e32-40d5-8064-b4f100211117)

| **Feature** |   |   |
|---|---|---|
| 1 | Choose board size and type | ✓ |
| 2 | Start a new game of the chosen board size and type | ✓ |
| 3 | Making a move | ✓ |
| 4 | Checking the end of game | ✓ |
| 5 | Automated unit tests | ✓ |

**Summary of Source Code:**

| Source code file name | Production code or test code? | # lines of code |
|---|---|---|
| board.py | Production | 64 |
| game.py | Production | 61 |
| app.py | Production | 54 |
| App.jsx | Production | 143 |
| App.css | Production | 12 |
| test_api.py | Test | 32 |
| test_board.py | Test | 65 |
| test_game.py | Test | 92 |
|  | Total | 523 |

__init__.py (0 lines in each), main.jsx (10 lines), and index.css (111 lines) are not included. (main.jsx and index.css are vite’s generated started files.)

**Production Code vs User Stories/Acceptance Criteria:**

| **ID** | **User Story Name** | **User Story Description** | **Priority** | **Estimated effort (hours)** |
|---|---|---|---|---|
| 1 | Choose a board size | As a player, I want to choose the board size (an odd number from 7 to 21) so that I can play a quicker or a more challenging game. | Low | 1 |
| 2 | Choose the board type | As a player, I want to choose between the English, Hexagon, and Diamond board types so that I can play different board layouts. | Done | 0 |
| 3 | Start a new game of the chosen board size and type | As a player, I want to be able to start a new game, so that I can play the game. | Medium | 1 |
| 4 | Make a move in a game | As a player, I want the ability to make moves within the game, so that I can progress in the game. | High | 2 |
| 5 | A game is over | As a player, I want to know when the game is over, so that I can celebrate when I win and play again. | Medium | 1 |

| **User Story ID and Name** | **AC**<br>**ID** | **Description of Acceptance Criterion** | **Class(es)** | **Methods** | **Status (completed, to-do, in-progress)** | **Notes** |
|---|---|---|---|---|---|---|
| 1. Choose a board size | 1.1 | **Default size.**<br>Given the game has just launched,<br>When the main screen is displayed,<br>Then the board size field shows 7. | APP<br>__init__ | useState(“7”)<br>size=7 | Done |  |
|  | 1.2 | **Valid size.**<br>Given the game screen is displayed,<br>When I enter an odd whole number from 7 to 21 (for example 9) and press New Game,<br>Then a board of size 9 is displayed. | Board, Game, App | Board.__init__, Game.new_game, app.parse_size, app.new_game | Done |  |
|  | 1.3 | **Even size rejected.**<br>Given the game screen is displayed,<br>When I enter an even number (for example 8) and press New Game,<br>Then an error message says the size must be an odd number from 7 to 21, and the current board is unchanged. | Board, Game, App | Board.__init__ raises ValueError(SIZE_ERROR); app.new_game returns HTTP 400; App.newGame shows the message | Done | Game.new_game builds the new board first, so the current board is unchanged |
|  | 1.4 | **Out-of-range size rejected.**<br>Given the game screen is displayed,<br>When I enter an odd number outside the range (for example 5 or 23) and press New Game,<br>Then the same error message appears and the current board is unchanged. | Board, Game, App | Board.__init__ raises ValueError(SIZE_ERROR); app.new_game returns HTTP 400; App.newGame shows the message | Done |  |
|  | 1.5 | **Invalid input rejected.**<br>Given the game screen is displayed,<br>When I leave the size field empty or enter non-numeric text and press New Game,<br>Then the same error message appears and the current board is unchanged. | Board, App (Flask) | App.parse_size (digits only), Board.__init__ | Done |  |
|  | 1.6 | **Change applies on New Game.**<br>Given a game is in progress,<br>When I change the size value without pressing New Game,<br>Then the board on screen and the game state do not change. | App | Separate sizeText and game state; only newGame() replaces game | Done |  |
|  | 1.7 | **Largest board fits.**<br>Given the application window is at least 1280x720 pixels and the size is 21,<br>When I press New Game,<br>Then all cells of the board are visible without scrolling. |  |  | To-Do | Still needs to be completed |
|  | 1.8 | **Malicious or unexpected input.**<br>Given the game screen is displayed,<br>When I enter unexpected input in the size field (for example 9.5, 1e3, a very long string, or &lt;script&gt;alert(1)&lt;/script&gt;) and press New Game,<br>Then the input is rejected with the standard error message, the current board is unchanged, and the application does not crash. | Board, Flask | App.parse_size, Board.__init__ | Done | Anything that not a whole odd number between 7 & 21 is rejected |
| 2. Choose the board type | 2.1 | **Default type.**<br>Given the game has just launched,<br>When the main screen is displayed,<br>Then English is selected. | App | useState(“english”) | Done |  |
|  | 2.2 | **Single selection.**<br>Given the game screen is displayed,<br>When I select a board type,<br>Then exactly one type is selected and the others are deselected. | App | Radio group name=”boardType” | Done |  |
|  | 2.3 | **Selected type is used.**<br>Given a valid size is entered,<br>When I select Hexagon (or Diamond) and press New Game,<br>Then a board of that type is displayed at the chosen size. | Game, EnglishBoard, HexagonBoard, DiamondBoard | Game.BOARD_TYPES, Game.new_game, each _is_valid_cell | Done | Hexagon is approx. and based off of a square grid |
|  | 2.4 | **Change applies on New Game.**<br>Given a game is in progress,<br>When I select a different board type without pressing New Game,<br>Then the board on screen and the game state do not change. | App | boardType state vs game state | Done |  |
|  | 2.5 | **Size and type are independent.**<br>Given the size and type are selected,<br>When I change one of them,<br>Then the other keeps its value. | App | Separate sizeText and boardType state | Done |  |
| 3. Start a new game of the chosen board size and type | 3.1 | **Player selects new game.**<br>Given the board’s current positions,<br>When the player selects new game,<br>Then the board resets current board to ready state. | Game, Board, App | Game.new_game, Board._build_grid, app.new_game, App.newGame | Done |  |
|  | 3.2 | **Confirm board is in ready state.**<br>Given the board’s current state,<br>When the player starts a new game<br>And the board is filled,<br>Then flash a banner stating ready to play. |  |  | To-Do | Banner addition |
|  | 3.3 | **Remove banner.**<br>Given ready to play banner is displayed,<br>When two seconds has hit,<br>Then remove banner. |  |  | To-Do | Banner addition |
| 4. Make a move in a game | 4.1 | **Player picks up a peg.**<br>Given player has picked up a peg,<br>When player moves mouse,<br>Then peg follows the mouse. | App | App.handlecellClick, Selected state | To-Do | Click to select but pegs do not follow mouse |
|  | 4.2 | **Valid orthogonal jump.**<br>Given the player has picked up a peg,<br>When the peg is set down in an empty hole two cells away, directly up, down, left, or right,<br>And the cell between them holds a peg,<br>Then the peg stays in the empty hole,<br>And the jumped peg is removed,<br>And the total peg count decreases by one. | Game, Board, App | Game.make_move, Game._is_valid_move, Board.set_cell, Board.peg_count, app.move (POST /api/move), App.handleCellClick | Done |  |
|  | 4.3 | **Valid diagonal jump.**<br>Given the player has picked up a peg,<br>When the peg is set down in an empty hole two cells away on a diagonal,<br>And the cell between them holds a peg,<br>Then the peg stays in the empty hole,<br>And the jumped peg is removed,<br>And the total peg count decreases by one. | Game, Board, App | Game.make_move, Game._is_valid_move, Board.set_cell, Board.peg_count, app.move (POST /api/move), App.handleCellClick | Done |  |
|  | 4.4 | **Destination is occupied.**<br>Given the player has picked up a peg,<br>When the peg is set down on a hole that already holds a peg,<br>Then the move is rejected,<br>And the board returns to its state before the move. | Game | Game._is_valid_move | Done | Destination must be empty. UI shows “invalid move” |
|  | 4.5 | **No peg to jump.**<br>Given the player has picked up a peg,<br>When the peg is set down in an empty hole two cells away,<br>And the cell between them is an empty hole,<br>Then the move is rejected,<br>And the board returns to its state before the move. | Game | Game._is_valid_move | Done | UI shows “invalid move” |
|  | 4.6 | **Wrong distance or direction.**<br>Given the player has picked up a peg,<br>When the peg is set down in an empty hole that is not exactly two cells away in a straight line (for example one cell away, three cells away, or a knight's move away),<br>Then the move is rejected,<br>And the board returns to its state before the move. | Game | Game._is_valid_move | Done | UI shows “invalid move” |
|  | 4.7 | **Peg set down outside the board.**<br>Given the player has picked up a peg,<br>When the peg is set down outside the board, including empty areas inside the grid that are not part of the chosen board type,<br>Then the move is rejected,<br>And the board returns to its state before the move. | Game | Game._is_valid_move | Done | UI shows “invalid move” |
| 5. A game is over | 5.1 | **Player’s move is complete.**<br>Given player has made a valid move,<br>When peg is set,<br>Then check board for other pegs. | Game, Flask | Game.has_valid_moves, Game.is_game_over, app.state | Done |  |
|  | 5.2 | **Exactly one peg on board.**<br>Given only one peg on the board,<br>When check board has completed,<br>Then player wins game,<br>And display message with option to restart game. | Game, App | Game.get_result returns "win" | Done | Restart via the New Game button |
|  | 5.3 | **Only two pegs on board.**<br>Given only two pegs on board<br>And no other moves can be made,<br>When check board has completed,<br>Then player has partial win.<br>And display message with option to restart game. | Game, App | Game.get_result returns "partial win" | Done |  |
|  | 5.4 | **No other plays left.**<br>Given no other valid plays on board<br>And more than two pegs left,<br>When check board has completed,<br>Then player loses.<br>And display message with option to restart game. | Game, App | Game.get_result returns "loss" | Done |  |
|  | 5.5 | **Game over**<br>Given displayed message,<br>When banner timer hits five seconds,<br>Then change board to default. |  |  | To-Do | No timer/banner |

**Tests vs User Stories/Acceptance Criteria**

**Automated Test:**

| **User Story ID and Name** | **AC ID** | **Class Name(s) of the Test Code** | **Method Name(s) of the Test Code** | **Status (Pass/Fail/In Progress)** |
|---|---|---|---|---|
| 1. Choose a board size | 1.2 | TestBoardSizeValidation; TestApi | test_valid_odd_size_is_accepted [7, 9, 15, 21]; test_new_game_returns_board | Pass |
|  | 1.3 | TestBoardSizeValidation; TestNewGame; TestApi | test_even_size_is_rejected [8, 10, 20]; test_invalid_size_leaves_current_game_unchanged; test_bad_size_returns_400_and_keeps_game | Pass |
|  | 1.4 | TestBoardSizeValidation | test_out_of_range_odd_size_is_rejected [-7, 1, 5, 23, 101] | Pass |
|  | 1.5 | TestBoardSizeValidation | test_non_integer_float_is_rejected; test_string_is_rejected [9, abc]; test_none_is_rejected; test_empty_string_is_rejected | Pass |
|  | 1.8 | TestBoardSizeValidation | test_non_integer_float_is_rejected; test_string_is_rejected [abc] | Pass (partial; see 4.2) |
| 2. Choose the board type | 2.3 | TestNewGame; TestApi | test_new_game_has_only_center_empty [english, hexagon, diamond]; test_new_game_returns_board (diamond) | Pass |
| 3. Start a new game of the chosen board size and type | 3.1 | TestNewGame; TestEnglishBoard | test_new_game_has_only_center_empty; test_peg_count_on_new_board; test_center_is_empty | Pass |
| 4. Make a move in a game | 4.2 | TestMakeMove; TestApi | test_valid_orthogonal_jump; test_valid_and_invalid_move | Pass |
|  | 4.3 | TestMakeMove | test_valid_diagonal_jump | Pass |
|  | 4.4 | TestMakeMove | test_destination_occupied_is_rejected | Pass |
|  | 4.5 | TestMakeMove | test_no_peg_to_jump_is_rejected | Pass |
|  | 4.6 | TestMakeMove | test_wrong_distance_is_rejected | Pass |
|  | 4.7 | TestMakeMove; TestEnglishBoard | test_off_board_is_rejected; test_corner_is_not_part_of_board | Pass |
| 5. A game is over | 5.1 | TestGameOver | test_new_game_is_not_over | Pass |
|  | 5.2 | TestGameOver | test_one_peg_is_a_win | Pass |
|  | 5.3 | TestGameOver | test_two_pegs_no_moves_is_partial_win | Pass |
|  | 5.4 | TestGameOver | test_three_pegs_no_moves_is_a_loss | Pass |

**Manual tests:**

| **User Story ID and Name** | **AC ID** | **Test Case Input** | **Test Oracle (Expected Output)** | **Notes** |
|---|---|---|---|---|
| 1. Choose a board size | 1.1 | Launch the app | Size field shows 7; 7x7 English board displayed |  |
|  | 1.6 | In a game, change the size field to 9 without pressing New Game | Board and game state unchanged |  |
|  | 1.8 | Enter &lt;script&gt;alert(1)&lt;/script&gt;, 1e3, and a 200-character string, press New Game | Error message shown, board unchanged, no crash |  |
| 2. Choose the board type | 2.1 | Launch the app | English radio selected |  |
|  | 2.2 | Click Hexagon, then Diamond | Only the last one clicked is selected |  |
|  | 2.4 | In a game, select Diamond without pressing New Game | Board unchanged |  |
|  | 2.5 | Set size 9, then change the board type | Size field still shows 9 |  |
| 5. A game is over | 5.1-5.4 | Play a 7x7 English game until no moves remain | Game-over message matches pegs left (1 win, 2 partial win, 3+ loss) |  |

**Other Automated Testing Used During Development:**

| **Test Input** | **Expected Result** | **Class Name of the Test Code** | **Method Name of the Test Code** |
|---|---|---|---|
| Board type "triangle" | ValueError | TestNewGame | test_invalid_board_type_rejected |
| HexagonBoard(7) | 32 pegs | TestBoardShapes | test_hexagon_has_32_pegs_at_size_7 |
| DiamondBoard(7) | 24 pegs | TestBoardShapes | test_diamond_has_24_pegs_at_size_7 |
| Cell (0, 2) on a size-7 board | Hexagon: peg; Diamond: invalid | TestBoardShapes | test_hexagon_differs_from_diamond |

**LLM Testing Screenshots:**

Claude used for LLM.

![LLM screenshot 1](<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/d33a948d-16a7-4229-bf38-9c1461562d98" />)

![LLM screenshot 2](<img width="975" height="923" alt="image" src="https://github.com/user-attachments/assets/0de29bf5-9a41-417b-87c6-53edfdc34607" />)

While building out the test claude suggested this prompt:

“I’m writing pytest tests for a Python Board class whose constructor takes a size. Valid sizes are odd integers from 7 to 21. Anything else should raise ValueError with the message “Size must be an odd number from 7 to 21”. Write pytest tests covering: a valid size, an even size, an out-of-range odd size, a non-integer like 9.5, a string, None, and an empty value. Use a class TestBoardSizeValidation and import EnglishBoard from game.board.”

![LLM screenshot 3](<img width="975" height="1227" alt="image" src="https://github.com/user-attachments/assets/a3f86a8a-cb08-4772-9fb8-ee097f6a13d9" />)

![LLM screenshot 4](<img width="974" height="440" alt="image" src="https://github.com/user-attachments/assets/e53e8ea2-6804-4d80-b4cd-ddc1413c92f5" />)

![LLM screenshot 5](<img width="975" height="533" alt="image" src="https://github.com/user-attachments/assets/10b236bb-7b36-4223-8b5f-ec373e02c8c9" />)

Some back and forth on the testing until all tests eventually passed:

![LLM screenshot 6](<img width="974" height="389" alt="image" src="https://github.com/user-attachments/assets/78fa5776-e3f9-47f7-ab91-d3144d14f9f0" />)
