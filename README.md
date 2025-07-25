# 2048 Game Solver: AI Search Algorithms

A Python implementation of uninformed and informed search algorithms to solve a simplified version of the **2048 game**, developed as part of the *Artificial Intelligence* course (2024).

## Overview
The project solves a 2048-like puzzle where the goal is to reach a target number (`goal_number`) in the minimum number of moves. Unlike classic 2048:
- Numbers **do not need to be powers of 2** to merge.
- Merging happens when tiles move to the edge of the board (e.g., `[2, 4, 4, 2]` → `[2, 8, 2, 0]` after a left move).

## Features
- **Search Algorithms**:
  - Uninformed: BFS, DFS, IDS
  - Informed: GBFS, A*, IDA*
- **Game Modes**:
  - `Normal`: Merge any adjacent numbers.
  - `Advance`: Merge only identical numbers (like classic 2048).
- **Visualization**: Pretty-printed board states using `tabulate`.
