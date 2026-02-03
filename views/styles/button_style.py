primary = """
QPushButton:enabled {
	background-color: rgb(44, 163, 222);
	color: white;
}

QPushButton:disabled {
	background-color:rgb(185, 185, 185);
	color: white;
}

QPushButton {
	border-radius: 15px;
	padding: 3px;
}

QPushButton:hover{
	background-color: rgb(97, 221, 255);
}
"""

start = """QPushButton:enabled {
	background-color: green;
	color: white;
}

QPushButton:disabled {
	background-color:rgb(185, 185, 185);
	color: white;
}

QPushButton {
	border-radius: 15px;
	padding: 3px;
}

QPushButton:hover{
	background-color: rgb(71, 214, 0);
}

"""

stop = """QPushButton:enabled {
	background-color: red;
	color: white;
}

QPushButton:disabled {
	background-color:rgb(185, 185, 185);
	color: white;
}

QPushButton {
	border-radius: 15px;
	padding: 3px;
}

QPushButton:hover{
	background-color: rgb(255, 86, 29);
}"""

delete = """QPushButton:enabled {
	background-color: red;
	color: white;
}

QPushButton:disabled {
	background-color:rgb(185, 185, 185);
	color: white;
}

QPushButton {
	border-radius: 15px;
	padding: 3px;
}

QPushButton:hover{
	background-color: rgb(255, 86, 29);
}"""

blue = """
QPushButton:enabled {
	background-color: #39a5db;
	color: white;
}

QPushButton:disabled {
	background-color:rgb(185, 185, 185);
	color: white;
}

QPushButton {
	border-radius: 15px;
}

QPushButton:hover{
	background-color: rgb(59, 116, 190);
}
"""

transparent = """
QPushButton:enabled {
	background-color: rgba(255, 255, 255, 0);
	color: white;
}

QPushButton:disabled {
	background-color:rgba(255, 255, 255, 0);
	color: white;
}

QPushButton {
	border-radius: 15px;
}

QPushButton:hover{
	background-color: #E9E9E9;
}
"""

open_file = """
QPushButton:enabled {
	background-color: rgba(255, 255, 255, 0);
	color: #39a5db;
}

QPushButton:disabled {
	background-color:rgba(255, 255, 255, 0);
	color: gray;
}

QPushButton {
	border-radius: 0px;
	text-decoration: none;
	color: #39a5db;
}

QPushButton:hover{
    color: #27759c;
	text-decoration: underline;
}
"""