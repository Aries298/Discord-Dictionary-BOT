# Discord-Dictionary-BOT
Discord BOT to search entries from a Google Sheets dictionary. It was made for a Polish conlang project but can work for any other language given the same structure sheet.
# Sheet structure
![image](https://user-images.githubusercontent.com/85286463/135252138-7075e154-6925-47b1-a044-6875cd336b24.png)

The sheet consists of two columns:
The first one containing words and their Polish counterparts (if there's a one).

The second one marked "Przypisy" containing additional notes.
# Syntax
The Bot handles 3 following commands:
?jak phrase - searches for all lines containing this phrase (even as a part of a word)
?zob phrase - searches for exact translated word
?kon - stops printing out output (in case someones types "?jak  " which literally prints out the whole dictionary)

