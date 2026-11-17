# Start reading the Python code

Open this folder in VS Code. Begin with these three files:

1. **pacmind/maze.py**: what is a cell, a wall and a legal move?
2. **pacmind/game.py**: read `GameState.step()` to see one complete tick.
3. **pacmind/search.py**: how does each strategy decide which node to expand next?

Then read **pacmind/traffic.py**, **pacmind/agents/ghost.py**, and **pacmind/agents/pacman.py**. The first prevents overlap, the second controls ghosts, and the third controls AI Pac-Man.

The full file map and plain-English walkthrough are in **docs/CODE_GUIDE.md**. The original TypeScript folder is a separate project; this version's source is in **pacmind/** rather than **src/**.

For example, this color is in `pacmind/ui/palette.py`:

```python
YELLOW = (255, 220, 85)  # Red, green, blue: Pac-Man's body and plan.
```

The actual body is drawn by `draw_pacman()` in `pacmind/ui/board.py`. Scoring values are in `pacmind/config.py`; `collect_pellet()` in `pacmind/game.py` applies them.

To run on Windows, install Python 3.12, extract the project and double-click **START_WINDOWS.bat**. To read the code, open the folder in VS Code.
