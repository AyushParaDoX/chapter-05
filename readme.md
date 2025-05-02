
---

## 🔑 **Dictionary in Python**

### 👉 What is it?

A dictionary is a collection of **key-value pairs** — like a real-world dictionary where a **word (key)** has a **meaning (value)**.

### 👉 Example:

```python
student = {
    "name": "Ayush",
    "age": 13,
    "class": "8B"
}
```

* `"name"` is the key, `"Ayush"` is the value.
* You can access like this:

```python
print(student["name"])  # Output: Ayush
```

* Add new data:

```python
student["hobby"] = "coding"
```

---

## 🌿 **Set in Python**

### 👉 What is it?

A set is a collection of **unique values** — it does **not allow duplicates**.

### 👉 Example:

```python
my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}
```

### 👉 You can:

* Add items:

```python
my_set.add(10)
```

* Remove items:

```python
my_set.remove(2)
```

---

## 🧠 Quick Comparison

| Feature          | Dictionary        | Set                    |
| ---------------- | ----------------- | ---------------------- |
| Stores           | Key-Value pairs   | Only values            |
| Allows duplicate | No duplicate keys | No duplicate items     |
| Access           | By key            | By checking membership |
| Example          | {"name": "Ayush"} | {1, 2, 3}              |

---

Let me know if you want some small coding exercises to practice these concepts!

dictionary & sets use in when we make real world projects where we need to store the things like:
---
| Student data manager.|
| Quiz app.|
| To-do list.|
| Visitor tracker.|
| Email filter.|
---
why sets do not allow to dulpicate any existing value?
> Internally Python uses a hash table to store sets.
> Hash table allows only one copy of each value (like a club with strict entry).
so what will a programmer do when he want to work within dulpicative values?
-> He can use list and tuples which allow us to work with multiple duplicative values.