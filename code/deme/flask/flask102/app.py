from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unit-converter/', methods=['GET','POST'])
def unit_converter():
    if request.method == 'POST':
        meters = float(request.form.get('feet')) * 0.3048
        return render_template('unit-converter.html',  meters = meters)
    return render_template('unit-converter.html')

    ## different return lines for post and get

@app.route('/anagram/', methods=['GET', 'POST'])
def anagram():
    if request.method=='POST':
        print(request.form)
        data = dict(request.form)
        first_word = data['first_word']
        second_word = data['second_word']
        print(data)
        first_word_split = list(first_word)
        print(first_word_split)
        second_word_split = list(second_word)
        print(second_word_split)
        first_word_split.sort()
        second_word_split.sort()
        if first_word_split == second_word_split:
            anagram = "anagrams"
        else:
            anagram= "not anagrams"
    return render_template('anagram.html', first_word=first_word, second_word=second_word, anagram = anagram)
    
    
    
  
    

#     # distance = input("What is the distance in feet? ")
#     # print(f"{distance} ft is {round(int(distance) * mea['feet'], 4)} m") 
#     #used the round function here because it started returning a bunch of zeros at the end
#     dist = input("what is the distance? ")
#     unit = input("what are the units? ")
#     print(f"{dist} {(unit)} is {int(int(dist) * mea[unit])}")
#     return render_template('anagram.html')



# first_word = input("Enter the first word: ")
# first_word_split = list(first_word)
# print(first_word_split)
# second_word = input("Enter the second word: ")
# second_word_split = list(second_word)
# print(second_word_split)
# first_word_split.sort()
# second_word_split.sort()
# if first_word_split == second_word_split:
#     print(f"{first_word} and {second_word} are anagrams.")
# else:
#     print(f"{first_word} and {second_word} are not anagrams.")
    





app.run(debug=True)
