import streamlit as st
import pickle

st.set_page_config(
	layout = "centered",
	page_title = "Wordle Solver",
	page_icon = "🔍"
)

st.write("By Jonathan Ngo")

english_words = pickle.load(open("english_5_letter_words.pickle", "rb"))

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters_not_in_answer = st.multiselect("Letters not in answer (gray)", alphabet)

st.subheader("Position 1")
pos_1 = st.selectbox("Correct letter (green)", ["Unknown"] + alphabet, key = 1)
not_pos_1 = st.multiselect("Letter cannot be (yellow)", alphabet, key = 1)

st.subheader("Position 2")
pos_2 = st.selectbox("Correct letter (green)", ["Unknown"] + alphabet, key = 2)
not_pos_2 = st.multiselect("Letter cannot be (yellow)", alphabet, key = 2)

st.subheader("Position 3")
pos_3 = st.selectbox("Correct letter (green)", ["Unknown"] + alphabet, key = 3)
not_pos_3 = st.multiselect("Letter cannot be (yellow)", alphabet, key = 3)

st.subheader("Position 4")
pos_4 = st.selectbox("Correct letter (green)", ["Unknown"] + alphabet, key = 4)
not_pos_4 = st.multiselect("Letter cannot be (yellow)", alphabet, key = 4)

st.subheader("Position 5")
pos_5 = st.selectbox("Correct letter (green)", ["Unknown"] + alphabet, key = 5)
not_pos_5 = st.multiselect("Letter cannot be (yellow)", alphabet, key = 5)

letters_to_try = st.multiselect("Letters to try", alphabet, key = 6)
letters_in_answer = set(letters_to_try + not_pos_1 + not_pos_2 + not_pos_3 + not_pos_4 + not_pos_5)

pos_1 = [pos_1] if pos_1 != "Unknown" else [a for a in alphabet if a not in not_pos_1 + letters_not_in_answer]
pos_2 = [pos_2] if pos_2 != "Unknown" else [a for a in alphabet if a not in not_pos_2 + letters_not_in_answer]
pos_3 = [pos_3] if pos_3 != "Unknown" else [a for a in alphabet if a not in not_pos_3 + letters_not_in_answer]
pos_4 = [pos_4] if pos_4 != "Unknown" else [a for a in alphabet if a not in not_pos_4 + letters_not_in_answer]
pos_5 = [pos_5] if pos_5 != "Unknown" else [a for a in alphabet if a not in not_pos_5 + letters_not_in_answer]

if st.button("Submit"):
	guesses = []
	for a in pos_1:
		for b in pos_2:
			for c in pos_3:
				for d in pos_4:
					for e in pos_5:
						if set([a, b, c, d, e]).intersection(letters_in_answer) == letters_in_answer:
							word = a + b + c + d + e
							if word in english_words:
								guesses.append(word)

	st.table(guesses)
