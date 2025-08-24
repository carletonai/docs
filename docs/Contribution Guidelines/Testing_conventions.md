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