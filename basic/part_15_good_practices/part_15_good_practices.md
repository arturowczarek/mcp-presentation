---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('../presentations/background.svg')
---

![bg left:40% 80%](../presentations/mcp.svg)

# **Good practices**

---

# Tool naming and description

- Help your LLM understand what the tool does
- Use evaluators to check if the tool is used
- The existing REST endpoints descriptions are probably not good for LLMs.

---

# Use the right schemas

- The REST schemas are for the machines
- LLMs are more human-like
- Filter everything that is not needed

---

# Don't use too many tools

- The LLMs are not good at tool selection
- If you do, write a good prompt

---

# Consider other features

- Autocompletion suggestions
- Icons for tools
- Pagination
  - Maybe you don't need to read everything?
- Long operations
  - Progress tracking
  - Cancellation
- Tools/resources/roots updates with notifications

---

# Keep an eye on updates

- https://modelcontextprotocol.io/specification/draft/changelog
- Frequent security improvements
- New features
- Good place to learn