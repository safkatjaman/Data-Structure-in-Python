                                                                                    #""" Data Structure """#



                                                                                    #""" List Structure """#
avengers = ['Thor', 'Captain America', 'Iron Man', 'Dead pool', 'Ant Man']
print(avengers)



""" Add or Remove in Data Structure """
avengers2 = ['Thor', 'Captain America', 'Iron Man', 'Dead pool', 'Ant Man', 'Bat Man']
print(avengers2)
""" To remove use remove() keyword in Python """
avengers2.remove('Bat Man') 
print(avengers2)
""" To add use append() keyword in Python """
avengers2.append('Vision')
print(avengers2, '\n \n \n')



                                                                                         #"""  Stack  """#
                                                                                          #""" LIFO """#

""" Stack is a list where you add element, everytime when you add element it always put one element on top of another. As you put it in the top it means it stays at the top of the list. And when you want to use the pop() keyword you have to remove the last element you put there.. this means LAST IN FIRST OUT (LIFO).. So the summary is 'Stack uses the LIFO policy'. Let's talk about LIFO in more details, like if you are in Canada and the temperature there is -1 degree then you have to put some clothes to get outside, as the human cloth wearing policy you will wear a t-shirt then a sweat shirt, then a hoodie then a warm jacket or something like that. After coming home if you want to take off those clothes first you have to take off the jacket then the hoodie then the sweat shirt then finally the t-shirt. So here is the thing that when you are wearing the stack is like t-shirt -> sweat shirt -> hoodie -> jacket and the take off part was like jacket -> hoodie -> sweat shirt -> t-shirt.. this is what we call LIFO. Let's make a stack below """

""" Another thing you should remember that you have to use list.append() to add element in the stack and list.pop() to remove element from the stack """
clothes = []
print(clothes)
clothes.append('t-shirt')
print(clothes)
clothes.append('sweat shirt')
print(clothes)
clothes.append('hoodie')
print(clothes)
clothes.append('jacket')
print(clothes)
clothes.pop()
print(clothes)
clothes.pop()
print(clothes)
clothes.pop()
print(clothes)
clothes.pop()
print(clothes, '\n \n \n')



                                                                                         #"""  Queue  """#
                                                                                          #""" FIFO """#
""" So think that you want to go to USA.. For that you have to buy a ticket (VISA is done), so you go to the airport and see that there is a line in the ticket counter or there is a waiting line in the ticket counter.. queue is like that.. every waiting line is a queue. If you store data in a manner of waiting line then it will be called a Queue Data Structure.. The main thing of queue is First In First Out (FIFO). Like the waiting line of the ticket counter the first person of the counter will get the ticket first and get out from the line. This is called FIFO. Queue uses FIFO policy. Use list.append() to add something in the Queue list. To remove the first element from the list you always have to write list.pop(0) if you are removing like one after another line """

waitingLine = []
print(waitingLine)
waitingLine.append('Vladimir Putin')
print(waitingLine)
waitingLine.append('Donald Trump')
print(waitingLine)
waitingLine.append('Kim Jong Un')
print(waitingLine)
waitingLine.append('Norendro Modi')
print(waitingLine)
#waitingLine.append(input('Your name: '))
waitingLine.append('Safkat Jaman')
print(waitingLine)
waitingLine.pop(0)
print(waitingLine)
waitingLine.pop(0)
print(waitingLine)
waitingLine.pop(0)
print(waitingLine)
waitingLine.pop(0)
print(waitingLine)
waitingLine.pop(0)
print(waitingLine, '\n \n \n')



                                                                                          #""" Dictionary """#
""" So the main part to remember about dictionary is every data can be connected like your friend named Lutuputu has a girlfriend named Kutukutu. So they are connected. In Python this data connection is called Dictionary Data Structure. (In some programming languages it is called Hash Tables). There is another example like you have a smartphone and in that smartphone you have saved a number with a name Mutumutu. So your main target was saving the number to save it you need a name that means The name is connected with that number, and this is a dictionary. In fact your mobile phonebook is a dictionary. To declare a dictionary you just need to name the dictionary, give a equal sign and two curly brackets, inside the curly brackets you have to put the elements like girlFriendName = {'Lutuputu' : 'Kutukutu', 'Putuputu' : 'Mutumutu'}. That's how you declare a dictionary. """ 

""" You can also access the data of the dictionary for this you have to write the name of the dictionary then two square brackets with the name and inside the brackets just write the key of the dictionary. Like girFriendName['Lutuputu'] """

""" To add a value in the dictionary with a key you just have to write the name of the dictionary then write two square brackets with it inside the square bracket write the key and then an equal sign and then put the value of the key. like, girlFriendName['Kutumutu'] = 'Gutugutu' """

""" If you want you can update the value of each and every keys. Like you friend Lutuputu broke up with Kutukutu and get in a new relationship with Nutunutu. So you will update the dictionary right? Like, girlFriendName['Lutuputu'] = 'Nutunutu' """

""" If you want to delete a element from the dictionary you just have to write the keword 'del' before the dictionary name and the key. Like, del girlFriendName['Putuputu'] """

""" List (Array) only stores the value like band = ['Aurthohin'] but Dictionary stores the Key and value bandVocal = ['Aurthohin' : 'BassBaba Sumon'] """

bandVocal = {'Lincoln' : 'Artcell', 'BassBaba Sumon' : 'Aurthohin', 'John Kabir' : 'Indalo', 'Ayub Bacchu' : 'LRB', 'Johad' : 'Nemesis'}
print(bandVocal)
print(bandVocal['Johad'])
bandVocal['Rafa'] = 'Aurthohin'
print(bandVocal)
bandVocal['Rafa'] = 'AvoidRafa'
print(bandVocal)
del bandVocal['Ayub Bacchu']
print(bandVocal, '\n \n \n')



                                                                                          #""" Linked List """#
""" Linked list is easy to understand. Just remember that in a list the elements are independent and in a linked list the elements are connected. Like you went on a date with your girl and hold her hand during the whole date. So you people are connected right! Each item in a linked list is called a 'Node'. Every 'Node' in a linked list will have two information, 1) Data or a value and 2) a pointer to the next node. Data is a value of a list (array). Pointer is a special property that creates a connection with the next 'Node'. """

""" The first 'Node' of a linked list is called 'Head' and the last 'Node' of a linked list is called 'Tail' rest of other 'Node' are called 'Nodes' """

""" To create a node in a linked list you have to be familiar with object and class. First thing you have to do is to add a Head in the linked list. Once you have a head you can add another node in the head. Once you add the node in the head, the head will point to the next node like this, "Batman" -> "Superman". To add a node you have to remember three things: 1) Start with the Head, 2) Walk all the way to the last node, 3) Create a link from the last node to the new node. Like this, "Batman" -> "Fatman" -> "Catman" -> "Ratman".. If you want to add a node you have to check where is the last node without any pointer then you can add. """

""" You have to do four things to add a node in the middle of a linked list:  1) You have to start from the head. 2) Find the node after which you want to add. 3) Point the current node towards the new node. 4) Point the new node to the next node. """

""" Removing a node is easier. You have to do 3 things: 1) Start with the Head. 2) Keep going to the right and search for the element. 3) Once you find the element link the previous element to the next element. """



                                                                                               #""" Tree """#
""" So trees are in Data Structure as well. And remember that it starts from the root. Tree in data structure is like your family, you have a grand father right! His father is your great grand father! Your great grand father's son is your grand father, your grand father's son is your father and your father's brother means your uncle, you are your father's son and you have a brother and a sister, also your uncle have two sons/daughters. So here is the deal your great grand father is the root of the tree, then your grand father then your father then you. See the below example of tree in data structure. """

#                                                                                               Grand Father - (Root or Parent Node)
#                                                                                               /         \
#                                                                                         Father          Uncle - (Parent Node of below nodes and Child Node of the Root or upper Node)
#                                                                                         /    \          /    \
#                                                                                      You   Sister     Son   Daughter - (Child Node of the upper node)

""" If you compare the family structure you can compare with the reverse tree. Where the root is in the upside. """

""" In the tree data structure each element is called a node. In the above example your grand father is a node, you father and uncle are nodes even you, your sister and your cousins are also node. The top most node of the data structure is called Root and the other nodes are called child node. Another thing is any upper node is called the Parent Node. """

""" A node consists at least two data. One is the Value and the other is the Children (Nodes under the current node).  """

""" Binary Tree is a special kind of Tree Data Structure. Where one Node can have maximum of two Nodes. Like the Upper Example of your Father's family. While coding for a binary tree you will have two or three elements. One is data and rest two are left and right node. Like the below example, """

#         A
#       /   \
#      /     \
#     B        C
#    / \      / \
#   /   \    /   \
#  D    E    F    G
#      / \
#     H   I



                                                                                          #""" Priority Queue """#
""" If a queue is designed in such way to give higher priority to a special type of element, that queue is called Priority Queue. So the actual deal is if you are in a waiting line of Serving Food in your School the waiting line is a queue. But there is a policy like if a teacher comes he/she will be served first. Means teacher is getting priority as well as if the Principal comes he/she will be served before the teachers. That's how priority queue works. """