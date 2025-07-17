# Contributing to CuMind

Welcome to the **Carleton University AI Society (CUAIS)** CuMind project! Every
function has comprehensive docstrings with everything you need to implement it.

## Development

**The docstrings contain ALL the information you need!** Each function includes:

- **Args**: What parameters to expect
- **Returns**: What to return and in what format
- **Implementation**: Step-by-step guidance on what to build
- **Developer**: Your name goes here when you implement it
- **Branch**: Branch name for this feature

For example:

```python
def select_action(self, observation: np.ndarray, training: bool = True) -> int:
  """Select action using MCTS search from current observation.

  Args:
    observation: Current game state observation
    training: If True, sample from action probabilities; if False, take best action

  Returns:
    Selected action index

  Implementation:
    - Convert observation to tensor and run network.initial_inference()
    - Use MCTS to search and get action probabilities
    - Sample action if training, else take argmax
  """
  # Branch: feature/mcts-action-selection
  raise NotImplementedError("select_action needs to be implemented")
```

**💡 Pro Tip**: Read documentation (mostly PyTorch), do your own research, use
tools like ChatGPT and Copilot to help if you're struggling. Do not push
anything you aren't sure about. Questions in the coders-corner channel are
always welcomed!

## Branch Naming

Use these patterns for branch names:

- `feature/description` — New features
- `internal/description` — Refactoring or internal changes
- `bugfix/description` — Bug fixes
- `dev` — Development branch (anyone can push, but force-push is not allowed)
- `master` — Protected branch (read-only)

**Examples:**

- `feature/add-atari-support`
- `internal/refactor-mcts`
- `bugfix/fix-reward-scaling`
- `my-feature` (not allowed)
- `fix-bug` (not allowed)

## Development Workflow

Follow these logical steps to contribute effectively:

### 1. Set Up Your Environment

- Clone the repository using SSH (recommended) or HTTPS:

  ```bash
  # SSH (recommended)
  git clone git@github.com:carletonai/cumind.git

  # HTTPS (requires personal access token to push)
  git clone https://github.com/carletonai/cumind.git

  cd cumind
  uv sync
  ```

- See:
  - [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
  - [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### 2. Sync Your Local Repository

Before starting any work, make sure your local repository is up to date:

```bash
git fetch
git pull dev
```

### 3. Find a Function to Implement

- Search for unimplemented functions:
  ```bash
  grep -r "NotImplementedError" src/ --include="*.py"
  ```
- Review available branches for ongoing work:
  ```bash
  git branch -a
  git branch -a | grep "feature/"
  ```

### 4. Finding & Using Branches

- **Check for existing feature branches:**
  ```bash
  git branch -a | grep "feature/mcts-action"
  ```
  If a relevant branch exists, check it out and pull the latest changes:
  ```bash
  git checkout feature/mcts-action-selection
  git pull origin feature/mcts-action-selection
  ```
- **Create a new branch if needed:**
  ```bash
  git checkout -b feature/describe-your-feature
  ```
- **Push your branch to remote:**
  ```bash
  git push origin feature/describe-your-feature
  ```

### 5. Implement Your Function

1. **Read the docstring** for detailed instructions.
2. **Replace the `NotImplementedError`** with your implementation.
3. **Update the developer field** in the docstring
4. **Keep your code clean and simple.**

### 6. Update Corresponding Tests

- For every function you implement, update its corresponding test.
- Example: If you implement `agent.py::select_action()`, also implement
  `test_agent.py::test_select_action_training_mode()`.
- Find the relevant test:
  ```bash
  find tests/ -name "*.py" -exec grep -l "test_select_action" {} \;
  ```

### 7. Test & Validate

- Run your specific test:
  ```bash
  uv run pytest tests/test_agent.py::TestAgent::test_select_action_training_mode -v
  ```
- Run all tests:
  ```bash
  uv run pytest tests/ -v
  ```
- Run code quality checks:
  ```bash
  uv run ruff check .
  uv run ruff format .
  uv run mypy src/
  ```

## Git Workflow

### Committing Your Work

```bash
# Stage your changes
git add src/cumind/agent.py tests/test_agent.py

# Commit with an informative message (can be goofy but informative!)
git commit -m "feat: implement MCTS action selection

Added select_action method with exploration noise and visit count sampling.
Also implemented corresponding test with mock MCTS behavior."

# Push your branch
git push origin feature/mcts-action-selection
```

**Commit Message Tips:**

- Be informative about what you implemented
- Mention if you also updated tests
- Goofy/fun messages are fine as long as they're clear!
- Some conventional commits are: `feat:`, `fix:`, `test:`, `docs:`

### Merging Others' Work

If someone else worked on your branch:

```bash
# Get the latest changes
git fetch origin

# Merge their work into yours
git merge origin/feature/mcts-action-selection

# Or rebase if you prefer clean history
git rebase origin/feature/mcts-action-selection
```

### Pull Requests

> **Note:** You only need a Pull Request (PR) for major changes to the `master`
> branch. For most work, push directly to `dev` after passing all checks.

**To open a PR to `master`:**

1. Push your branch to GitHub.
2. Open a PR targeting `master`.

- List the functions you implemented.
- Briefly describe your approach and any challenges.
- Link related issues if needed.

3. Request a review from maintainers.
4. Make sure all checks pass (`pytest` and `mypy`).

**Else:**

- Push to `dev` for regular work (tests/checks must pass).

## Git Basics

New to Git? Check out these resources:

- [Git Handbook](https://guides.github.com/introduction/git-handbook/) -
  Official GitHub guide
- [Learn Git Branching](https://learngitbranching.js.org/) - Interactive
  tutorial
- [Oh Shit Git](https://ohshitgit.com/) - Common problems and solutions

## Essential Linux Usage for Contributors

Linux is a powerful open-source operating system. As a contributor, understanding basic command-line usage is key. This guide covers essential commands, system updates, and best practices for command-line work.

---

### Basic Linux Commands

The command line is your main interface. Here are core commands you'll use often:

* **`ls` (list):** Shows directory contents.
    * `ls`: Lists files and directories in the current location.
        * _Example:_ `ls` might output `documents images myproject.txt`
    * `ls -l`: Provides a "long listing" with details like permissions, size, and date.
        * _Example:_ `ls -l` might show `-rw-r--r-- 1 user group 1024 Jul 10 10:30 myproject.txt`
    * `ls -a`: Shows all files, including hidden ones (starting with a `.`).
        * _Example:_ `ls -a` might reveal `.bashrc .config documents`
* **`cd` (change directory):** Navigates between directories.
    * `cd <directory_name>`: Moves to a specific directory.
        * _Example:_ `cd documents`
    * `cd ..`: Moves up one directory level.
        * _Example:_ If in `/home/user/documents`, `cd ..` moves to `/home/user/`
    * `cd ~`: Returns to your home directory.
        * _Example:_ No matter where you are, `cd ~` takes you to `/home/user/`
* **`pwd` (print working directory):** Displays your current directory's full path.
    * _Example:_ `pwd` might output `/home/user/myproject`
* **`mkdir` (make directory):** Creates a new directory.
    * _Example:_ `mkdir new_folder`
* **`rmdir` (remove directory):** Deletes an empty directory.
    * _Example:_ `rmdir empty_folder`
* **`touch`:** Creates an empty file or updates a file's timestamp.
    * _Example:_ `touch new_file.txt` (creates a new empty file)
* **`cp` (copy):** Copies files or directories.
    * `cp <source_file> <destination_file>`: Copies a file.
        * _Example:_ `cp report.docx report_backup.docx`
    * `cp -r <source_directory> <destination_directory>`: Copies a directory and its contents.
        * _Example:_ `cp -r myproject myproject_copy`
* **`mv` (move):** Moves or renames files/directories.
    * _Example (move):_ `mv old_file.txt documents/` (moves `old_file.txt` into the `documents` folder)
    * _Example (rename):_ `mv old_name.txt new_name.txt`
* **`rm` (remove):** Deletes files or directories.
    * `rm <file_name>`: Deletes a file.
        * _Example:_ `rm unwanted_file.txt`
    * `rm -r <directory_name>`: Recursively deletes a directory (use with extreme caution!).
        * _Example:_ `rm -r old_project_folder` (Deletes the folder and everything inside it)
* **`cat` (concatenate):** Displays a file's content.
    * _Example:_ `cat README.md` (shows the content of the README.md file)
* **`less` / `more`:** Views file content page by page for large files.
    * _Example:_ `less /var/log/syslog` (allows you to scroll through a large log file; press `q` to quit)
* **`grep`:** Searches for text patterns within files.
    * _Example:_ `grep "error" /var/log/syslog` (finds all lines containing "error" in the syslog file)
* **`man` (manual):** Provides documentation for commands.
    * _Example:_ `man ls` (shows the manual page for the `ls` command; press `q` to quit)

---

### How to Update and Upgrade the System

Keeping your system updated is vital for security and new features. For Debian-based systems (like Ubuntu), use `apt`:

* **`sudo apt update`**: Refreshes the list of available packages from repositories.
    * _Example:_ `sudo apt update` (You'll see a list of package information being downloaded)
* **`sudo apt upgrade`**: Installs newer versions of all currently installed packages.
    * _Example:_ `sudo apt upgrade` (Prompts you to confirm the installation of available updates)
* **`sudo apt full-upgrade`**: Performs a more comprehensive upgrade, installing new packages if needed for dependencies and removing obsolete ones.
    * _Example:_ `sudo apt full-upgrade` (Use for major system version upgrades or when `upgrade` is insufficient)

**To update:**

1.  Open your terminal.
2.  Run `sudo apt update`.
3.  Then, run `sudo apt upgrade`.
4.  Optionally, use `sudo apt full-upgrade` for a deeper update.

---

### How `sudo` and `apt` Work

* **`sudo` (SuperUser DO):**
    * **Function:** Allows you to run commands with **root (administrator) privileges** using *your own password*.
    * **When to use:** For tasks requiring elevated permissions, like installing software, modifying system files, or managing services.
    * **Caution:** Always be careful with `sudo`; incorrect commands can harm your system.
        * _Example:_ `sudo systemctl restart apache2` (restarts the Apache web server, requires root privileges)

* **`apt` (Advanced Package Tool):**
    * **Function:** A command-line utility for managing software packages (installing, updating, removing) on Debian-based systems. It interacts with software repositories.
    * **When to use:**
        * `apt install <package_name>`: Install new software.
            * _Example:_ `sudo apt install git` (installs the Git version control system)
        * `apt remove <package_name>`: Uninstall software (leaves configuration files).
            * _Example:_ `sudo apt remove firefox`
        * `apt purge <package_name>`: Uninstall software and its configuration files.
            * _Example:_ `sudo apt purge apache2`
        * `apt search <keyword>`: Find packages.
            * _Example:_ `apt search text editor` (lists available text editor packages)

---

### Tips for Command-Line Navigation and Safety

Here are some best practices to make your command-line work more efficient and secure:

* **Tab Completion:** Press the `Tab` key to auto-complete commands, file names, or directory names. Press `Tab` twice to see all available options if there's more than one.
* **Arrow Keys:** Use the `Up` and `Down` arrow keys to cycle through your command history. This saves typing and helps recall previous commands.
* **`Ctrl+R` (Reverse Search):** Press `Ctrl+R` and start typing to search your command history for a specific command. It's incredibly useful for finding a command you ran a while ago.
* **Read the Manual (`man`):** If you're unsure about a command or its options, use `man <command_name>` for detailed documentation. Press `q` to quit the manual.
* **Be Careful with `sudo`:** Always double-check your commands before pressing Enter when using `sudo`. Commands run with root privileges can make significant, irreversible changes to your system if executed incorrectly.
* **Backup Regularly:** Make a habit of backing up important files and configurations, especially before performing major system changes or software installations. This can save you from potential data loss.

## Code Style

**Keep it simple and elegant!**

- **Follow the docstring guidance** - it tells you exactly what to implement
- **Use type hints** everywhere (already provided)
- **Keep functions focused** - one responsibility per function
- **Clean, readable code** over clever code

## Testing Philosophy

**Every function implementation should update its corresponding test!**

### Test Structure

```
src/cumind/agent.py     →  tests/test_agent.py
src/cumind/mcts.py      →  tests/test_mcts.py
src/cumind/network.py   →  tests/test_network.py
```

### Test Implementation

- Replace `pass` with actual test logic
- Follow the test docstring guidance
- Test both success and failure cases
- Use descriptive assertions

Example:

```python
def test_select_action_training_mode(self):
    """Test action selection in training mode."""
    # Implementation: Test with mock MCTS, verify exploration
    agent = Agent(config)
    action = agent.select_action(observation, training=True)
    assert isinstance(action, int)
    assert 0 <= action < config.action_space_size
```

## Project Structure

```
src/cumind/
├── agent.py      # CuMind agent with MCTS integration
├── mcts.py       # Monte Carlo Tree Search implementation
├── network.py    # Neural networks (representation, dynamics, prediction)
└── config.py     # Configuration and hyperparameters

tests/
├── test_agent.py    # Agent functionality tests
├── test_mcts.py     # MCTS algorithm tests
├── test_network.py  # Neural network component tests
└── test_cumind.py   # Integration tests
```

## Available Functions to Implement

**Quick way to see what needs work:**

```bash
# See all unimplemented functions
grep -r "NotImplementedError" src/ --include="*.py"

# See all available remote branches
git branch -r
```

**Popular starting points:**

- `feature/agent-initialization` - Set up the CuMind agent
- `feature/mcts-action-selection` - MCTS-based action selection
- `feature/vector-encoder` - Neural network for 1D observations (Classic
  Control)
- `feature/conv-encoder` - Neural network for 3D observations (Atari)
- `feature/residual-block` - Building block for neural networks

## Community Guidelines

- **Be respectful** and inclusive
- **Help each other** in discussions and reviews
- **Share knowledge** - document tricky parts
- **Ask questions** if docstrings aren't clear enough
- **Celebrate progress** - every implementation helps!

## Tips for Success

- **Start small:** Pick an easy function to get comfortable.
- **Explore related code:** Read similar functions to see how things fit
  together.
- **Test as you go:** Run tests early and often—don’t wait until the end.
- **Use examples:** Check out examples for inspiration. (TODO)
- **Ask for help:** If you’re stuck, open an issue or chat on Discord.

**Feeling stuck? That’s normal!**

- Re-read the docstring—often the answer is there.
- Look at how similar functions are implemented.
- Search existing issues or discussions for hints.
- If you need to, open a new issue. Include:
  - The function you’re working on
  - What you’ve tried so far
  - Where you’re stuck
  - Any relevant code snippets
- If you’re blocked for more than a day, reach out to maintainers on Discord,
  we’re here to help!

**Common stumbling blocks:**

- **PyTorch confusion?** Ask AI or the community for explanations.
- **Failing tests?** Double-check the test docstring for what’s expected.
- **Branch conflicts?** See the Git Basics section above.
- **Unclear requirements?** Open an issue to clarify or improve the docstring.

---

## Ready to Contribute?

1. **Find a function** you want to implement
2. **Check if someone started it** (`git branch -a | grep feature/...`)
3. **Create/checkout the branch**
4. **Read the docstring** and implement it
5. **Update the corresponding test**
6. **Test your changes**
7. **Commit and push**

**Welcome to the CUAIS community!**

_Every function you implement brings us closer to a complete CuMind
implementation. Thank you for contributing!_
