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
