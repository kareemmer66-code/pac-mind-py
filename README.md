# PAC-MIND — Python AI Search Lab

A complete local **Python desktop game** with readable, commented source. This edition rebuilds the PAC-MIND browser project using **Pygame Community Edition** while retaining Main Game, AI Pac-Man, four search-driven ghosts, Search Lab, and the separate Minimax/Alpha-Beta AI Duel.

Use **Python 3.12** for the simplest setup. The source targets Python 3.10 or newer. No API key, backend, database or model download is needed. Initial dependency installation needs internet access. After installation the game runs locally.

## Start on Windows

1. Install Python 3.12 from https://www.python.org/downloads/. Enable **Add Python to PATH** if the installer offers it.
2. Right-click the ZIP and choose **Extract All**. Open the extracted `pacmind-python` folder.
3. Double-click **START_WINDOWS.bat**.

The launcher creates a `.venv` inside the project, installs the pinned Pygame dependency and opens the game window. On later launches it reuses that environment. Keep the folder extracted; launching files from inside a ZIP will not set up the project correctly.

You can also open a terminal in the folder and run:

```bat
py launcher.py
```

If the Python launcher command is unavailable, use `python launcher.py`.

## Manual installation

Windows Command Prompt or PowerShell:

```bat
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pacmind
```

Linux/macOS:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pacmind
```

These direct interpreter commands avoid needing to activate a shell environment. Pygame CE supplies the `pygame` import used in the code.

## Controls and modes

**Main Game:** Arrow keys or WASD move Pac-Man. A turn is buffered until legal. Space/P pauses or resumes; R restarts; I switches Human/AI control. Click Start to begin, and use the control panel to select AI Autoplay. Each ghost's algorithm button cycles through BFS, DFS, UCS, Greedy and A*. Clicking a ghost's name selects it for inspection. AI Overlay shows its real stored search snapshot. Player plan shows the beam search's last predicted route.

Collect every pellet to finish. Regular pellets award 10, power pellets 50, and catching a frightened ghost 200. You start with three lives. Power lasts 46 simulation ticks, about six seconds. A life loss preserves score/pellet progress; restarting resets them. A surviving AI run continues automatically. Ghosts reserve their space and replan or wait when blocked; they cannot share cells or swap through one another.

**Search Lab:** Choose a map and algorithm using the cycling buttons. Click Set START/GOAL and then a corridor to edit endpoints. S/G also selects which endpoint to edit, and Arrow keys move that endpoint through legal corridors. Run, Play/Pause, Step, Reset trace, Result and speed buttons control the actual recorded trace. Compare all uses identical inputs for all five algorithms and reports real costs, counts and measured search time, excluding playback.

**AI Duel:** A separate alternating-turn arena. Yellow is MAX; pink is MIN. Set depth from 1–6 plies, compare both solvers, reveal their trees, and apply the chosen move. Click tree nodes to collapse/expand descendants and use the mouse wheel to scroll. Selecting a node also shows its recorded alpha/beta updates. PRUNED counts skipped immediate child branches. Minimax and Alpha-Beta use the same state, depth, evaluation and move order.

**Global:** F1/F2/F3 switches modes. Leaving a running Main Game pauses it. Tab/Shift+Tab moves button focus and Enter activates the focused button. Sidebar toggles reduce motion and enable original synthesized sound. The X window button exits. Resizing preserves the maze aspect ratio.

Preferences and best score are saved on a normal exit in `%APPDATA%\pacmind-python\preferences.json` on Windows, or `~/.config/pacmind-python/preferences.json` on other systems. Storage failure is harmless.

## Read and change the source

Start with **START_READING.md** and **docs/CODE_GUIDE.md**. The actual commented code is under **pacmind/**. Open the extracted folder in VS Code; the launcher opens the game, while VS Code displays the source.

| Change or study | File |
|---|---|
| Timing, lives and points | `pacmind/config.py` |
| Pac-Man yellow and other colors | `pacmind/ui/palette.py` |
| Pac-Man/ghost artwork and animations | `pacmind/ui/board.py` |
| Movement, scoring and collisions | `pacmind/game.py` |
| Why ghosts cannot overlap | `pacmind/traffic.py` |
| BFS, DFS, UCS, Greedy and A* | `pacmind/search.py` |
| Ghost targets, flee, respawn and replanning | `pacmind/agents/ghost.py` |
| AI Pac-Man | `pacmind/agents/pacman.py` and its helper modules |
| Minimax and Alpha-Beta | `pacmind/minimax.py` |
| Separate turn-based rules | `pacmind/duel.py` |

The core has no Pygame imports. You can study and test classical AI without running a graphics window. The Python port retains the original layer boundaries while replacing React/Phaser/Vite with Python/Pygame. Original requirements remain unchanged under `docs/original/`; **docs/PYTHON_PORT.md** explains the technology changes.

## Tests and code checks

After installing requirements, run:

```sh
python -m unittest discover -s tests -v
```

This includes complete unassisted AI runs on both maps and SDL event/render integration tests. The suite uses a dummy video/audio driver for UI tests so it can run without opening a window. It does not force the normal application to use dummy video.

For development checks, also install `requirements-dev.txt` into your environment:

```sh
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m compileall -q pacmind launcher.py tools tests
```

Use your `.venv` interpreter in place of `python` when the environment is not activated. `python launcher.py --check` sets up and verifies dependencies without opening the window.

`tools/verify_desktop.py` drives real application buttons, compares algorithms and records screenshots/metrics. The exact command used in the Linux validation is in **docs/FINAL_REPORT.md**. The `--frames`, `--screenshot` and `--no-save` entry-point options support development smoke tests.

## Academic assumptions and practical limits

This is classical search AI. BFS uses a queue, DFS a stack, UCS g, Greedy h and A* g+h. All maze steps are cardinal and unit cost, so Manhattan is admissible and consistent. DFS and Greedy have no shortest-path guarantee. AI Pac-Man uses bounded beam search, eight ticks ahead with width ten, simulating real game copies; it has no general win guarantee for arbitrary maps/algorithm assignments. The separate AI Duel supplies the alternating turns required for Minimax.

The traffic policy keeps ghost cells distinct and prevents swaps, but narrow custom corridors may cause waiting or deadlock. It is not a complete multi-agent pathfinding solver. Decorative glow can touch. All search plans are snapshots of their planning problem.

Two original game maps are supplied. Optional DLS/IDS/bidirectional algorithms remain outside this edition. The synchronous AI planner can cause frame-time spikes on slower computers. Pygame provides custom graphics rather than browser DOM accessibility; keyboard focus and reduced motion are implemented, but screen-reader semantics are more limited. Native Windows execution and physical audio listening were not performed on the Linux validation machine.

See **docs/FINAL_REPORT.md** for actual verification results, **docs/AI_COMPLETION.json**, **docs/DESKTOP_EVALUATION.json** and **docs/screenshots/** for observations. This archive contains Python source, not a prebuilt Windows EXE.
