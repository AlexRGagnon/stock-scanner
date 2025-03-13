# Development Roadmap

This document outlines the development strategy for the Stock Scanner project. 
 It ensures that each AI agent understands its task and collaborates with other AI agents.

- Git Branch: main
- Planning Agent: Project Manager AI
- Lead Developer: dev/lead-dev.md
- Feature Developer: feature/*/feature-dev.md
- Code Review: bugfix/*/code-review.md
- Optimization: optimize/*/optimization.md
- Automated Testing: test/*/testing.md
- Deployment: deploy/*/deployment.md
- Documentation: docs//docs.md

## Full Project Roadmap

### Phase 1: API Integration (Week 1-2)
-[] Setup OAuth 2.0 login with Charles Schwab API.
-[] Implement token storage with `keyring`.

## Phase 2: Filtering and Scannning (
- Extract stock data from the API using requests.
- Run filtering criteria on stock data.
- Update the GUI with stock filters.
- Create asynchronous stock fundamental data retrieval.
