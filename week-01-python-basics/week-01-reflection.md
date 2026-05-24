# Week 1 Reflection

## What I built
- Day 1-2: Python basics, input/output
- Day 3: Lists, dictionaries, list-of-dicts patterns
- Day 4: Conditionals, loops, FizzBuzz, Contact Book v1 (~80 lines, no functions)
- Day 5: Functions, refactor — Contact Book v2 (~110 lines, organized)
- Day 6: Virtual environments, pip, requests, first API call
- Day 7: File I/O, JSON, Joke fetcher v2, Contact Book v3 (persistent)

## Biggest aha moments
- Statements vs expressions (why `sum += i` can't go in an f-string)
- `del contact` doesn't delete from a list — `contacts.remove()` does
- `.append()` returns `None`, not the list (don't reassign)
- The `try` block must wrap the code that can fail
- Mutating methods modify in place; functions like `sorted()` return new copies

## Production-grade Python I now write reflexively
- Virtual environments for every project
- Constants in CAPS, single source of truth
- Early returns / guard clauses
- Specific exceptions (FileNotFoundError, not bare except)
- f-strings with single quotes inside double quotes
- 4-space indentation, formatter on save

## Habits I'm building
- Test edge cases (empty, first, last, broken input)
- Read errors carefully (last line tells you the most)
- Use Claude as a debugging tutor, not an answer machine
- Commit small, with meaningful messages