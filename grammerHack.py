string = """For __________ has Andrew cooked the
delicious Moroccan dinner, complete with a
fried camel appetizer?

After a month of dating Aarav, Mahika decided
that she wasn’t ready for a relationship with an
entomologist __________ spent more time
looking for bugs when they dined al fresco than
listening to her stories about lacrosse exploits.

Chini registered for European Literature, even
though the professor was TBA. She prayed
that she would not find herself in a classroom
with Dr. Chandak, the one professor
__________ no one can please.

__________ did you find to keep your
obnoxious, stinky, loud poodle while you are in
Spain?

Almira asked her fiancé Cesar to ride home
with Anand, __________ their other friends
would not trust with their own lives because of
his poor driving record.

Rhea insisted that her appointment was with
Aviral, the only stylist __________ she would
trust with her luscious locks.

Neha cringed when Dr. Rajwani paired her with
Ryan, the one lab partner __________ no one
can stand.

Abhilash gave a dozen vanilla-carrot cupcakes
to his sweetheart Nisha, __________ declared
them the most delicious treat that she had ever
tasted.

__________ ate the leftover lasagna?
Everyone does know that Yash uses food to
experiment with bugs for his entomology class,
right?

Mr. Mandala decided to fire Teja, the cashier
__________ could never make correct change.

Everyone at the gym stared at Keshav,
__________ sang along at the top of his voice
to the Brandi Carlisle songs on his iPhone.

Mrs. Satish, __________ is paranoid about
burglary, clutches her handbag so tightly that
she has constant shoulder pain.

When Abigail sat down in the computer lab,
she cursed the previous user __________ left
the keyboard sticky from a melted lollipop.

Adithya dreaded another soccer camp with
Coach Cherukapalli, _________ insisted that
players collapse on the field before she would
give them permission to leave a practice early.

__________ else knows that Nehal lost all his
hair when he neglected to follow the package
directions on the home perm kit?

Although Dawson prefers Grandma’s company
when gossiping at family picnics, his mother is
the woman __________ he admires the most.

Anvith contemplated his flattery options as he
waited for Professor Kim, the teacher
__________ might ruin Anvith's perfect 4.GPA.

To __________ has Shivkar spilled the tea
about Saara and Anish?

Heba shook her head in disgust as another
moronic driver yammering on a cell phone
nearly steered into a pedestrian __________
the driver was too preoccupied to notice.

When you are walking around the track, do not
try to stand your ground against Rohan,
_________ will run you over with the baby
carriage and then allow Gertrude, his husky, to
nip at your heels."""
strings = string.split("\n\n")
final = []
for i in range(0,len(strings)):
    strings[i]  = strings[i].replace("\n" , " ")
    j = strings[i].find("_")
    x=j
    while(strings[i][j] == "_"):
        j+=1
    temp = strings[i].replace(strings[i][x:j], "who")
    temp1 = strings[i].replace(strings[i][x:j], "whom")
    final.append(temp)
    final.append(temp1)
f = open("grammer.txt" , "w")
for i in final:
    f.write(i.replace(i[0], i[0].upper()))
    f.write("\n")