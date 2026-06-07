# 🏷️ Repository Labels Index

## Label Definitions and Usage Guide

This document defines all labels used in the Quantum Computing project repository for organizing issues, pull requests, and tracking work across all 5 development phases.

---

## 📊 Phase Labels

These labels indicate which development phase a task belongs to.

### `phase-1-core-engine`
- **Color:** 🔵 Blue  
- **Icon:** 🏗️
- **Description:** Core quantum computing engine and mathematical foundation
- **Scope:** Quantum state, gates, circuits  
- **Status:** ✅ COMPLETED
- **Related Files:** `quantum_simulator/core/*.py`
- **Examples:**
  - "Implement QuantumState class"
  - "Add quantum gates matrices"
  - "Create circuit API"

---

### `phase-2-algorithms`
- **Color:** 🟨 Yellow
- **Icon:** 🧮
- **Description:** Quantum algorithm implementations
- **Scope:** Grover's search, Teleportation, Bell states, Deutsch
- **Status:** 🟡 IN PROGRESS
- **Target Duration:** 1 week
- **Related Files:** `quantum_simulator/algorithms/`
- **Examples:**
  - "Implement Grover's search algorithm"
  - "Add quantum teleportation"
  - "Create Bell state demonstration"
  - "Add Deutsch algorithm"

---

### `phase-3-vqe-optimization`
- **Color:** 🟠 Orange
- **Icon:** ⚙️
- **Description:** VQE and hybrid optimization algorithms
- **Scope:** Classical optimizers, hybrid loops, molecular Hamiltonians
- **Status:** 🟡 UPCOMING
- **Target Duration:** 1 week
- **Related Files:** `quantum_simulator/optimizers/`, `quantum_simulator/vqe/`
- **Examples:**
  - "Implement COBYLA optimizer wrapper"
  - "Add molecular Hamiltonian"
  - "Create VQE optimization loop"
  - "H2 molecule energy calculation"

---

### `phase-4-visualization-ui`
- **Color:** 🟣 Purple
- **Icon:** 🎨
- **Description:** Visualization, UI, and CLI components
- **Scope:** Circuit drawings, plots, command-line interface
- **Status:** 🟡 UPCOMING
- **Target Duration:** 3-5 days
- **Related Files:** `quantum_simulator/visualization/`, `main.py`
- **Examples:**
  - "Create ASCII circuit diagram drawer"
  - "Add Bloch sphere visualization"
  - "Build convergence plots"
  - "Implement CLI interface"

---

### `phase-5-advanced-features`
- **Color:** 🔴 Red
- **Icon:** 🚀
- **Description:** Advanced features and optimizations
- **Scope:** QAOA, QML, error mitigation, GPU acceleration
- **Status:** 🟡 UPCOMING
- **Target Duration:** Ongoing (2+ weeks)
- **Related Files:** Multiple
- **Examples:**
  - "Implement QAOA algorithm"
  - "Add quantum machine learning classifier"
  - "Implement error mitigation techniques"
  - "GPU acceleration support"

---

## 🎯 Work Type Labels

Describe the nature of the work being done.

### `type-enhancement`
- **Color:** 💚 Green
- **Icon:** ✨
- **Description:** New feature or functionality addition
- **Usage:** Pull requests that add new capabilities
- **Priority Level:** Can be medium/high/low
- **Examples:**
  - New algorithm implementation
  - New visualization feature
  - New utility function
  - Performance improvement

---

### `type-documentation`
- **Color:** 📘 Light Blue
- **Icon:** 📖
- **Description:** Documentation updates and guides
- **Usage:** README updates, API docs, tutorials, examples
- **Priority Level:** Usually medium
- **Examples:**
  - Update README with examples
  - Write API reference documentation
  - Create tutorial notebooks
  - Add inline code comments

---

### `type-bug`
- **Color:** 🔴 Red
- **Icon:** 🐛
- **Description:** Something isn't working correctly
- **Usage:** Issues tracking broken functionality
- **Priority Level:** Usually high/critical
- **Examples:**
  - Gate calculation error
  - State normalization issue
  - Measurement incorrect result
  - Circuit chaining bug

---

### `type-refactor`
- **Color:** 💛 Yellow
- **Icon:** 🔧
- **Description:** Code improvements without new features
- **Usage:** Code cleanup, optimization, reorganization
- **Priority Level:** Usually low/medium
- **Examples:**
  - Optimize gate calculations
  - Reorganize module structure
  - Improve code readability
  - Remove duplicate code

---

### `type-optimization`
- **Color:** 🟠 Orange
- **Icon:** ⚡
- **Description:** Performance improvements and speed-ups
- **Usage:** Speed enhancements, memory optimization
- **Priority Level:** Medium/High depending on impact
- **Examples:**
  - Optimize state vector multiplication
  - Reduce memory usage
  - Cache gate matrices
  - Vectorize operations

---

### `type-testing`
- **Color:** 🔵 Blue
- **Icon:** ✅
- **Description:** Test coverage and quality assurance
- **Usage:** Adding tests, improving test coverage
- **Priority Level:** Medium
- **Examples:**
  - Add unit tests
  - Increase test coverage
  - Performance benchmarks
  - Edge case testing

---

## 🎪 Priority Labels

Indicate the importance and urgency of work.

### `priority-critical`
- **Color:** 🔴 Red
- **Icon:** 🚨
- **Description:** Blocks other work or is essential for phase completion
- **Usage:** Issues that must be resolved immediately
- **Effort:** Usually high
- **Impact:** Blocks multiple tasks
- **Examples:**
  - "Core algorithm not converging"
  - "Gate matrices calculations incorrect"
  - "Circuit measurement broken"

---

### `priority-high`
- **Color:** 🟠 Orange
- **Icon:** ⬆️
- **Description:** Important for current phase completion
- **Usage:** Features needed for milestone
- **Effort:** Usually medium-high
- **Timeline:** Should complete within week
- **Examples:**
  - "Implement Grover's algorithm"
  - "Add VQE optimizer"
  - "Create visualization module"

---

### `priority-medium`
- **Color:** 🟡 Yellow
- **Icon:** ➡️
- **Description:** Good to have in current phase
- **Usage:** Nice-to-have features and improvements
- **Effort:** Usually low-medium
- **Timeline:** Can be scheduled after high-priority items
- **Examples:**
  - "Improve documentation"
  - "Enhance visualization options"
  - "Add more test cases"

---

### `priority-low`
- **Color:** 💚 Green
- **Icon:** ⬇️
- **Description:** Can be deferred to later phases
- **Usage:** Nice-to-have features and future ideas
- **Effort:** Usually low
- **Timeline:** Complete when time allows
- **Examples:**
  - "Consider GPU acceleration"
  - "Explore distributed simulation"
  - "Add optional features"

---

## 🎓 Category Labels

Describe the domain or category of work.

### `category-quantum-core`
- **Color:** 🔷 Blue
- **Icon:** ⚛️
- **Description:** Core quantum computing concepts
- **Related:** Phase 1, fundamental mathematics
- **Scope:** Gates, states, measurements, circuits
- **Examples:**
  - Quantum state implementation
  - Gate matrix definitions
  - Circuit execution logic

---

### `category-algorithms`
- **Color:** 💜 Purple
- **Icon:** 🧮
- **Description:** Quantum algorithm implementations
- **Related:** Phase 2
- **Scope:** Grover, VQE, QAOA, Deutsch, Teleportation
- **Examples:**
  - Grover's search implementation
  - VQE optimizer
  - Quantum teleportation

---

### `category-optimization`
- **Color:** 🟠 Orange
- **Icon:** ⚙️
- **Description:** Classical and hybrid optimization
- **Related:** Phase 3
- **Scope:** COBYLA, L-BFGS, Adam, VQE loops
- **Examples:**
  - Classical optimizer wrapper
  - Hybrid quantum-classical loop
  - Convergence monitoring

---

### `category-visualization`
- **Color:** 🎨 Pink
- **Icon:** 📊
- **Description:** User interface and graphics
- **Related:** Phase 4
- **Scope:** Circuit drawing, Bloch sphere, plots, CLI
- **Examples:**
  - Circuit ASCII art
  - Energy convergence plots
  - Bloch sphere rendering

---

### `category-infrastructure`
- **Color:** ⚙️ Gray
- **Icon:** 🛠️
- **Description:** Project structure and utilities
- **Related:** All phases
- **Scope:** Setup.py, requirements.txt, CI/CD, utils
- **Examples:**
  - Package structure
  - Dependency management
  - Testing infrastructure

---

## 📋 Status Labels

Track the current status of issues or PRs.

### `status-in-progress`
- **Color:** 🔵 Blue
- **Icon:** 🔄
- **Description:** Currently being worked on
- **Usage:** Assign when starting work
- **When to Use:** Immediately when beginning implementation
- **When to Remove:** When moving to review or blocked
- **Examples:** Any active development

---

### `status-blocked`
- **Color:** 🔴 Red
- **Icon:** 🛑
- **Description:** Blocked by another issue/dependency
- **Usage:** Waiting on dependency or decision
- **When to Use:** When work cannot proceed
- **When to Remove:** When blocker is resolved
- **Examples:**
  - "Waiting for Phase 1 completion"
  - "Depends on PR #123"
  - "Needs decision on architecture"

---

### `status-review`
- **Color:** 🟡 Yellow
- **Icon:** 👀
- **Description:** Ready for code review
- **Usage:** PR awaiting review
- **When to Use:** After pushing changes to PR
- **When to Remove:** After review completion
- **Examples:** Any PR ready for review

---

### `status-done`
- **Color:** ✅ Green
- **Icon:** ✔️
- **Description:** Completed and merged
- **Usage:** Closed issues and merged PRs
- **When to Use:** After merge completion
- **When to Remove:** Never (historical record)
- **Examples:** Completed tasks

---

## 🔗 Label Combinations (Common Patterns)

Useful combinations of labels for common scenarios:

### Pattern 1: New Algorithm Feature
```
Primary Labels:
- phase-2-algorithms
- type-enhancement
- priority-high
- category-algorithms

Add if applicable:
- status-in-progress (if starting work)
```

### Pattern 2: Performance Bug in Phase 1
```
Primary Labels:
- phase-1-core-engine
- type-bug
- priority-critical
- category-quantum-core

Add if applicable:
- status-blocked (if dependencies exist)
```

### Pattern 3: Documentation Update
```
Primary Labels:
- type-documentation
- priority-medium
- category-infrastructure

Add specific phase if related:
- phase-X-* (if phase-specific)
```

### Pattern 4: Code Cleanup/Refactoring
```
Primary Labels:
- type-refactor
- priority-low
- category-infrastructure

Add optimization if speed-related:
- type-optimization (if performance-related)
```

### Pattern 5: Test Coverage Enhancement
```
Primary Labels:
- type-testing
- priority-medium
- category-infrastructure

Add phase if phase-specific:
- phase-X-* (if phase-specific tests)
```

### Pattern 6: Optimization Task
```
Primary Labels:
- type-optimization
- priority-medium (or high if impactful)
- category-infrastructure

Add category of what's being optimized:
- category-* (relevant to optimization)
```

---

## 📝 Using Labels Effectively

### Best Practices:

#### When Creating Issues:
1. **Always assign phase label** - Which phase does this belong to?
2. **Choose work type** - enhancement, bug, documentation, refactor, optimization, or testing?
3. **Set priority** - critical, high, medium, or low?
4. **Add category** - quantum-core, algorithms, optimization, visualization, or infrastructure?
5. **Add status** - Mark as "in-progress" if you're starting work immediately

#### When Creating PRs:
1. Include phase label
2. Mark type (enhancement, bug, refactor, etc.)
3. **Link related issues:** "Closes #123" or "Relates to #456"
4. Use status-review label automatically or manually
5. Request specific reviewers when ready
6. Add category label if applicable

#### Checklist for Good Labels:
- [ ] Phase label assigned (1-5)
- [ ] Work type chosen (enhancement/bug/doc/refactor/optimization/testing)
- [ ] Priority set (critical/high/medium/low)
- [ ] Category selected (quantum-core/algorithms/optimization/visualization/infrastructure)
- [ ] Status label added if applicable (in-progress/blocked/review/done)

---

## 📊 Label Statistics & Expected Distribution

### Phase Distribution (By Count):
- **Phase 1:** ✅ 4 issues (Completed)
- **Phase 2:** 🟡 8 issues (In Progress)
- **Phase 3:** 🟡 6 issues (Planned)
- **Phase 4:** 🟡 4 issues (Planned)
- **Phase 5:** 🟡 5+ issues (Planned)

### Work Type Distribution:
- **Enhancement:** ~50% (new features)
- **Documentation:** ~20% (guides, READMEs)
- **Testing:** ~15% (tests, coverage)
- **Refactor:** ~10% (cleanup, improvements)
- **Optimization:** ~5% (performance)
- **Bug:** ~varies (as they occur)

### Priority Distribution:
- **Critical:** ~5% (must fix immediately)
- **High:** ~30% (phase blockers)
- **Medium:** ~50% (normal work)
- **Low:** ~15% (nice to have)

---

## ✅ Quick Reference Table

| Label | Purpose | Color | Type |
|-------|---------|-------|------|
| phase-1-core-engine | Core quantum engine | 🔵 | Phase |
| phase-2-algorithms | Algorithm implementations | 🟡 | Phase |
| phase-3-vqe-optimization | VQE and optimization | 🟠 | Phase |
| phase-4-visualization-ui | UI and visualization | 🟣 | Phase |
| phase-5-advanced-features | Advanced features | 🔴 | Phase |
| type-enhancement | New feature | 💚 | Work Type |
| type-documentation | Docs update | 📘 | Work Type |
| type-bug | Bug fix | 🔴 | Work Type |
| type-refactor | Code improvement | 💛 | Work Type |
| type-optimization | Performance improvement | 🟠 | Work Type |
| type-testing | Test coverage | 🔵 | Work Type |
| priority-critical | Urgent/blocking | 🔴 | Priority |
| priority-high | Important | 🟠 | Priority |
| priority-medium | Normal | 🟡 | Priority |
| priority-low | Can defer | 💚 | Priority |
| category-quantum-core | Core concepts | 🔷 | Category |
| category-algorithms | Algorithms | 💜 | Category |
| category-optimization | Optimization | 🟠 | Category |
| category-visualization | UI/Graphics | 🎨 | Category |
| category-infrastructure | Utils/Setup | ⚙️ | Category |
| status-in-progress | Being worked on | 🔵 | Status |
| status-blocked | Blocked by other work | 🔴 | Status |
| status-review | Awaiting review | 🟡 | Status |
| status-done | Completed | ✅ | Status |

---

## 🔄 Label Workflow & State Machine

### Phase Progression Workflow:
```
phase-1-core-engine
    ↓
phase-2-algorithms
    ↓
phase-3-vqe-optimization
    ↓
phase-4-visualization-ui
    ↓
phase-5-advanced-features
```

### Status Workflow:
```
(new issue/PR created)
    ↓
[Assign labels based on type/phase/priority]
    ↓
status-in-progress
    ↓
[Optional] status-blocked → back to in-progress
    ↓
(For PRs) status-review
    ↓
Code review and feedback
    ↓
status-done (merged/closed)
```

### Priority Workflow:
```
priority-low
    ↓ (if becomes important)
priority-medium
    ↓ (if becomes blocking)
priority-high
    ↓ (if critical issue found)
priority-critical
```

---

## 📋 Example Issues

### Example 1: New Algorithm Issue
```
Title: [PHASE-2] Implement Grover's search algorithm

Labels:
✓ phase-2-algorithms
✓ type-enhancement
✓ priority-high
✓ category-algorithms
✓ status-in-progress

Body:
## Description
Implement Grover's quantum search algorithm for unsorted database search.

## Acceptance Criteria
- [ ] Amplitude amplification working
- [ ] Oracle creation functional
- [ ] Test with 3-8 qubits
- [ ] Performance benchmarked
- [ ] Documentation complete

## Related
Closes #45, Relates to PROJECT_PLAN
```

### Example 2: Bug Fix Issue
```
Title: [PHASE-1] Gate normalization not working correctly

Labels:
✓ phase-1-core-engine
✓ type-bug
✓ priority-critical
✓ category-quantum-core

Body:
## Bug Description
Hadamard gate not creating equal superposition as expected.

## Expected Behavior
H|0⟩ should create (|0⟩ + |1⟩)/√2 with probabilities 50/50

## Actual Behavior
Getting 60% |0⟩ and 40% |1⟩

## Steps to Reproduce
1. Create 1-qubit circuit
2. Apply Hadamard to qubit 0
3. Measure 1000 times
```

### Example 3: Documentation PR
```
Title: [DOCS] Add comprehensive API reference

Labels:
✓ type-documentation
✓ priority-medium
✓ category-infrastructure

Body:
## Changes
- Added complete API reference for all modules
- Documented all public methods
- Added usage examples
- Fixed typos in existing docs

## Checklist
- [x] Builds without errors
- [x] All links working
- [x] Examples tested
- [x] Follows style guide
```

---

## 🎯 Decision Tree: Which Labels to Use?

```
START: Creating Issue/PR
│
├─ PHASE?
│  ├─ Core Engine → phase-1-core-engine
│  ├─ Algorithms → phase-2-algorithms
│  ├─ VQE/Optimization → phase-3-vqe-optimization
│  ├─ Visualization → phase-4-visualization-ui
│  └─ Advanced → phase-5-advanced-features
│
├─ WORK TYPE?
│  ├─ Adding feature → type-enhancement
│  ├─ Fixing bug → type-bug
│  ├─ Updating docs → type-documentation
│  ├─ Cleaning code → type-refactor
│  ├─ Speeding up → type-optimization
│  └─ Adding tests → type-testing
│
├─ PRIORITY?
│  ├─ Blocks everything → priority-critical
│  ├─ Phase blocker → priority-high
│  ├─ Normal work → priority-medium
│  └─ Nice-to-have → priority-low
│
├─ CATEGORY?
│  ├─ Quantum concepts → category-quantum-core
│  ├─ Algorithm code → category-algorithms
│  ├─ Optimization code → category-optimization
│  ├─ UI/Graphs → category-visualization
│  └─ Infrastructure → category-infrastructure
│
└─ STATUS?
   ├─ Starting work now → status-in-progress
   ├─ Waiting on something → status-blocked
   ├─ Ready for review → status-review
   └─ Already done → status-done

END: Apply all relevant labels
```

---

## 📞 Questions & Answers

**Q: Can an issue have multiple phase labels?**  
A: No, typically one phase label per issue. If spanning phases, assign to primary phase.

**Q: Should I use both type-refactor and type-optimization?**  
A: Refactor is structural, optimization is performance. Use the primary one.

**Q: What if I don't know the priority?**  
A: Start with priority-medium, can be adjusted after review.

**Q: Can status labels change after issue creation?**  
A: Yes! Track progress: in-progress → blocked (if needed) → review → done

---

## 📚 Reference Links

- [DEVELOPMENT_TRACK.md](DEVELOPMENT_TRACK.md) - Overall project progress
- [README.md](README.md) - Project overview
- [PROJECT_PLAN.md](projects/PROJECT_PLAN.md) - Detailed phase plans
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

**Last Updated:** June 7, 2026  
**Total Labels Defined:** 25+  
**Active Phase:** 🟡 Phase 2 (Algorithms)  
**Next Label Update:** After Phase 2 completion
