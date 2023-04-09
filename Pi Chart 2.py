import matplotlib.pyplot as plt

Subjects = ["Science", "Math", "English", "Indigenous Studies", "Visual Arts", "Dance", "Music"]



slices = [15, 15, 23, 9, 19, 18, 16]

colors = ['rosybrown', 'gold', 'lightcyan', 'violet', 'lightgreen', 'cornflowerblue', 'peru']



plt.pie(slices, labels = Subjects, colors = colors,
       startangle = 180, shadow = True, explode = (0, 0, 0, 0, 0.8, 0.6, 0.4),
       radius = 0.9, autopct = '%2.1f%%')

plt.legend()

plt.show()