# Day 3 Notes

## Lists
- Like JS arrays. Use [].
- len(list) instead of list.length
- .append() = .push()
- Negative indexing: list[-1] = last item (cool!)
- "x in list" checks if x exists

## Dictionaries
- Like JS objects. Use {}.
- Keys MUST be in quotes.
- Only obj["key"] access. No obj.key.
- .get("key", "default") for safe access.
- Loop with .items() to get key + value together.

## Combined pattern
- List of dictionaries = most common real-world shape.
- Chat messages, products, users — all use this.
- Access: list[0]["key"]
- Find by value: loop + if + break

## Today's wins
- Found people from sirsa using collect-then-print
- Updated radhika's role by name
- Calculated average age with total + len
- Discovered Python 3.12+ allows nested same-quote f-strings