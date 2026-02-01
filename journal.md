# Learning Journal — Network Automation Sprint

## Context
Goal: Prepare for a Network Automation / SRE-style role (Ticketmaster-inspired) with a 2-week intensive plan.
Background:
- Level: Junior
- Strongest skills: Swift, HTML, Core Data
- Weakest area: Networking fundamentals and applying coding to networks
- Time available: ~20 hours/week
- Timeline: 2 weeks

## Key Decisions
- Selected `netmiko_tool` as the flagship project.
- Focus on Python-based network automation as the primary learning vehicle.
- Treat this repo as interview-facing and agent-friendly.

## Repository State
Location:
`/Users/rebeccaclarke/Documents/Financial/Gigs/Devops - Software Engineering/ConceptProjects/netmiko_tool`

Files:
- `network_tool.py`: Python Netmiko-based automation script (currently mock-driven).
- `README.md`
- `AGENTS.md`: Added to document build/lint conventions and code style for agentic coding.

## AGENTS.md Highlights
- Run: `python network_tool.py`
- Lint: `python -m py_compile network_tool.py`
- Formatting: Black recommended
- Security: No hardcoded secrets; use environment variables
- Style: Typed functions, structured logging, clear separation of CLI and logic

## Learning Philosophy
- Learn networking as a software problem.
- Prefer clarity and safety over cleverness.
- Build small, explainable automation artifacts suitable for interviews.

---
End of saved session.



