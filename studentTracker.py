import tkinter as tk

class StudentScoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Score Tracker")
        self.root.geometry("450x560")
        self.root.resizable(False, False)

        # ---------- EDIT STUDENT NAMES HERE ----------
        # Change the names in this list as needed.
        self.student_names = [
            "Бакибаев Мурат",
            "Греков Максим",
            "Гришин Артём",
            "Жамжуров Михаил",
            "Иль Данил",
            "Ключарёв Николай",
            "Мардашев Абылай",
            "Мукашев Расул",
            "Пятницкий Станислав",
            "Жанат Нұржамал"
        ]
        # ---------------------------------------------

        # Initialize scores (all start at 0)
        self.scores = [0] * len(self.student_names)

        # List to hold references to score label widgets
        self.score_labels = []

        # Create header labels
        header_name = tk.Label(root, text="Имя", font=("Arial", 12, "bold"))
        header_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        header_score = tk.Label(root, text="Оценка", font=("Arial", 12, "bold"))
        header_score.grid(row=0, column=1, padx=10, pady=10)

        header_action = tk.Label(root, text="", font=("Arial", 12, "bold"))
        header_action.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

        # Create rows for each student
        for i, name in enumerate(self.student_names, start=1):
            # Student name label
            name_label = tk.Label(root, text=name, font=("Arial", 10))
            name_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            # Score label (initial value 0)
            score_label = tk.Label(root, text="0", font=("Arial", 10), width=5)
            score_label.grid(row=i, column=1, padx=10, pady=5)
            self.score_labels.append(score_label)

            # Minus button
            minus_btn = tk.Button(root, text="-", command=lambda idx=i-1: self.decrement_score(idx), width=3)
            minus_btn.grid(row=i, column=2, padx=5, pady=5)

            # Plus button
            plus_btn = tk.Button(root, text="+", command=lambda idx=i-1: self.increment_score(idx), width=3)
            plus_btn.grid(row=i, column=3, padx=5, pady=5)

        # Optional quit button
        quit_btn = tk.Button(root, text="Выйти", command=root.destroy, bg="#f0f0f0")
        quit_btn.grid(row=len(self.student_names)+1, column=0, columnspan=4, pady=20)

        # Configure column weights
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=0)
        root.columnconfigure(2, weight=0)
        root.columnconfigure(3, weight=0)

    def increment_score(self, index):
        """Increase the score of the student at the given index by 1."""
        self.scores[index] += 1
        self.score_labels[index].config(text=str(self.scores[index]))

    def decrement_score(self, index):
        """Decrease the score of the student by 1, but not below 0."""
        if self.scores[index] > 0:
            self.scores[index] -= 1
            self.score_labels[index].config(text=str(self.scores[index]))

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentScoreTracker(root)
    root.mainloop()