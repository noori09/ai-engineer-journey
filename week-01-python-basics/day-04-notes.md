# Day 4 — Conditionals and Loops

Today covered the two foundations of every program: making decisions (`if/elif/else`) and repeating actions (`for` and `while`). Wrapped up with FizzBuzz and a full Contact Book CLI as a capstone.

## What I learned

### Conditionals
- `if / elif / else` with chained comparisons (`0 <= age <= 100`)
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators in English: `and`, `or`, `not` (Python's nicer take on `&&`, `||`, `!`)
- Truthy and falsy values — empty list, empty string, 0, None are all falsy
- `try / except ValueError` for handling bad user input gracefully

### For loops
- `range(start, stop, step)` — stop is exclusive
- `enumerate(items, start=1)` for index + value together
- Iterating over strings character by character
- Nested loops for grid patterns and table generation

### Loop patterns I now know cold
- **Running total** — accumulate with `total += x`
- **Find max** — track the "best so far" while iterating
- **Find by value** — loop + `if` + `break`
- **Collect then print** — build a list, then `", ".join()` it
- **Find with flag** — `found = False` before, `found = True` on match, `if not found:` after

### While loops
- `while condition:` for unknown iteration count
- `while True:` + `break` for menu-driven programs
- `continue` to skip the rest of an iteration
- The bulletproof input pattern: `while True` + `try/except` + `break` on valid input

### FizzBuzz
- The classic interview problem
- Key insight: check the most specific condition first (divisible by 3 AND 5 → "FizzBuzz" must come before the individual checks)
- Modulo operator `%` for divisibility

## Files in this day

| File | What it covers |
|---|---|
| `day-04-conditionals.py` | Voting eligibility, grade calculator, day classifier, login simulator |
| `day-04-loops.py` | Basic `range()` patterns — count, countdown, even numbers |
| `day-04-loop-patterns.py` | Multiplication table, sum 1-100, numbered list, longest name, vowel counter |
| `day-04-while-loops.py` | Countdown, input validation, number guessing game, odd numbers with continue |
| `day-04-fizzbuzz.py` | FizzBuzz 1-100 |
| `day-04-contact-book.py` | Full CLI program — the Day 4 capstone (~80 lines, 6 features) |

## Capstone: Contact Book CLI

A menu-driven terminal program that lets the user manage contacts.

### Features
- Add a contact (name, phone, city)
- List all contacts (numbered, formatted, handles empty list)
- Search by name (case-insensitive, with not-found message)
- Update a contact's phone number
- Delete a contact with confirmation
- Quit cleanly

### Run it
```bash
python day-04-contact-book.py
```

### Combines every Day 1-4 concept
Lists, dictionaries, list-of-dictionaries, `if/elif/else`, `while True`/`break`, `for`/`enumerate`, string methods (`.lower()`, `.strip()`, `.capitalize()`), find-with-flag pattern, `in` operator, dictionary modification, `list.remove()`.

## Bugs I caught while building today

A few real bugs I found through testing — not by reading the code, but by running it and noticing the result didn't match my expectations:

1. **Stale variable in error message** — printed `{age}` in an except block after `int()` failed. The variable held the *previous* valid value. Fixed by using `{age_input}` (the raw string) instead.

2. **`while True` without `break`** — number guessing game kept running after the correct answer because I forgot to `break`. Lesson: every `while True` needs a reachable exit.

3. **Silent update failure** — collected new phone number into a variable, printed "updated", but never assigned it back to the dictionary. Fixed by adding `contact["phone"] = new_phone`.

4. **`del contact` didn't delete from list** — `del` removes the local reference, not the item from the list. Switched to `contacts.remove(contact)`.

5. **Method on wrong object** — wrote `contact["name".capitalize()]` (capitalizing the key string "name") instead of `contact["name"].capitalize()` (capitalizing the looked-up value). Methods operate on whatever's immediately to their left.

6. **List containing one weird string** — `["a,e,i,o,u"]` is a list with ONE item (the whole string), not five separate vowels. The fix: `["a", "e", "i", "o", "u"]` or just use `"aeiou"`.

## Concepts I went deep on

A few things I asked about that turned into real lessons:

**Statements vs expressions** — Why `num * i` works inside an f-string but `sum += i` doesn't. Anything with `=` (including `+=`, `-=`) is a statement, not an expression, so it can't be evaluated inside `{ }` in an f-string. Python deliberately separates "doing" from "producing a value" to prevent the JavaScript bug of `if (x = 5)`.

**Shadowing built-ins** — Naming a variable `sum` overrides Python's built-in `sum()` function. Same problem with `list`, `dict`, `int`, `str`, `input`, `print`, `len`, `max`, `min`. Avoid these as variable names.

**`continue` vs "go to input line"** — `continue` doesn't know about specific lines; it just jumps to the top of the loop body. It happens to land at the input line because the input is the first line in the loop.

**Why "find all with tie" is harder than "find one max"** — Naive append-as-you-go doesn't work because previous "winners" become losers as the bar rises. Either reset the list when a new max is found, or use two passes (find max, then collect matches).

**`raise` vs `if/else` for validation** — `raise` is for exceptional failures in functions other code calls. `if/else` is for expected invalid input you're handling locally. Don't use exceptions for control flow.

## What's next

Day 5 is functions. The Contact Book has obvious repetition (`if not contacts:` appears 4 times, the find-with-flag pattern appears 3 times). Functions will let me write each pattern once and call it from multiple places. The refactor will be the first concrete payoff of learning `def`.