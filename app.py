from flask import Flask, render_template, request
from dbco import db
from user import User
import json
import os

app = Flask('MyApp')

@app.route('/login')
def login():
	usersJson = list(db.users.find({}))
	# takes users from mongo and converts them into a User object
	users = map(User.from_json, usersJson)

	for user in users:
		print "user:", user.username
		print "pass:", user.password

	

	return render_template('login.html', usersList=users, uName=user.username)


@app.route('/form')
def form():
	return render_template('form.html')
# #if note id, find single note
# # if no note id, find all notes
# #if multiple note ids, show all
# @app.route('/notes/<int:noteId>')
# def show_notes(noteId=None):
# 	if noteId:
# 		notes = (list(db.notes.find({'noteId': noteId})))
# 		print notes
# 		if notes:
# 			note = Note.from_json(notes[0])  # convert to python object
# 			note_title = note.title
# 			content = note.content
# 			noteId = note.noteId
# 			return render_template('show_note.html', title=note_title, content=content, noteId=noteId)


# @app.route('/update_note', methods=["POST"])
# def update_note():
# 	data = request.get_json(force=True, silent=True)
# 	print "POST data received"
# 	print data
# 	title = data.get("title")
# 	content = data.get("content")
# 	noteId = int(data.get("noteId"))

# 	the_note = db.notes.find_one({'noteId': noteId})
# 	if the_note:
# 		print type(the_note)
# 		my_note = Note.from_json(the_note)
# 		my_note.title = title
# 		my_note.content = content
# 	else:
# 		my_note = Note(title, content, noteId=noteId)

# 	print the_note
# 	db.notes.find_and_modify(query={'noteId': noteId},
# 		update=my_note.to_json(),
# 		upsert=True)

# 	return json.dumps({"success": True})


# @app.route('/new_note')
# def new_note():
# 	aNote = Note("Title here", "Content here")
# 	return render_template('show_note.html', noteId=aNote.noteId, title=aNote.title)


app.debug = True
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv("PORT", 8080)))
