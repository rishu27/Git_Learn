marks = {"ram":82,"shyam":99,"sita":91,"ujwal":100}
for name , marks in marks.items():
    print(f"{name}:{marks}")


average = sum(marks.value()) / len(marks)
print(f"Class average marks :{average}")

top  = max(marks, key= marks.get)
print(f"top students:{top}")

