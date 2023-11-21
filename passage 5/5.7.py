# 郭鑫 20222146060 数据科学与大数据技术
text = ("What is a function in Python?"
        " In Python, function is a group of related statements that perform a specific task. "
        "Functions help break our program into smaller and modular chunks. As our program grows"
        " larger and larger, functions make it more organized and manageable. Furthermore, "
        "it avoids repetition and makes code reusable. A function definition consists of following components."
        " Keyword def marks the start of function header. A function name to uniquely identify it. Function naming "
        "follows the same rules of writing identifiers in Python. Parameters (arguments) through which we pass values "
        "to a function. They are optional. A colon (:) to mark the end of function header. Optional documentation "
        "string (docstring) to describe what the function does. One or more valid Python statements that make up the function body. Statements must have same indentation level (usually 4 spaces). An optional return statement to return a value from the function.")
text = text.lower()
for ch in ",.;?!'":
    text = text.replace(ch, ' ')
words = text.split()
counts = {}
for word in words:
    if word in counts.keys():
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
words_count = list(counts.items())
words_count.sort(key=lambda x: x[1], reverse=True)
print("共有{0}个单词".format(len(words)))
print(words_count)

for i in range(14):
    if words_count[i][0] != 'a' and words_count[i][0] != 'the' and words_count[i][0] != 'of':
        print(words_count[i][0], words_count[i][1])
