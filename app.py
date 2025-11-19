from flask import Flask, render_template, url_for
app = Flask(__name__)  #Flask(__name__) means where to relocate all things 

# ***********************  FLASK APP ROUTING  *************************************
# Routing in Flask means mapping a URL (web address) to a 
# specific function in your Python code. e.g: ek URL hm bnayn gy about ka or ek bnayn gy 
# home page ka, jab user in URLs m s kisi ek pr jay ga to flask framwork dekhy ga 
# k is URL pr corresponding functions hn unhyn run kr do

@app.route('/', methods = ['GET'])  #default is get method
def welcome_home_page():
    return 'weolcome to home page'

@app.route('/about', methods = ['GET'])
def about_page(): #function names should aways be different for each page (i mean)
    return '<h1>this is about page, can also show HTML tags to it</h1>'

# **************************  VARIABLE RULE  ***************************************
@app.route('/result_page_pass_students/<score>') #<> k andr jo user likhy ga vhi page ka URL bn jay ga, 
# this is dynamic URL 
def passs(score):
    return('the student is pass with score:'+score)

@app.route('/result_page_fail_students/<int:score>') #<> k andr jo bhi ja rha h vo string k 
# tor pr ja rha h, agr m khu k m n variable int k tor pr lena h to m kr skti hun, by 
# using this: <int:> THIS IS CALLED VARIABLE RULE, 
def fail(score):
    # return('the student is fail with score:'+score)# agr m direct esy likh dun to error ay ga
    # because we cannot concatenate string  and integer, we have to typecast like below:
    return('the student is fail with score:'+ str(score))
# def demo(): #this cause error because ap n score varaibale pas nhi kia yhan pr, <> k andr jo bhi likhna h 
# vo hr hal m function k andr pas krvana hi krvana h    
#     return ('this is demo')

# *************************  Rendering Templates  **************************************
# in flask, we can render templates usinf render_template library, yani ap kisi or folder s templates ko
# is page k andr la skty ho, e.g: we are creating a form, and form kisi or file i.e form.html m pra h, 
# to hm render template k zrye y form ek specific webpage pr dikha skty hn, but for using render_template, it 
# necessary to put all templates (jin ko rendor krna h) in templates folder. is liye hm n form.html ko templates
# m rkha h 
@app.route('/demo_rendering', methods = ['GET'])
def form_demo():
    return render_template('demo.html')

# ***********************  NOW WE ARE RENDERING FORM AND SHOWING IT TO THE CLIENT SO THAT
# HE CAN ENTER DATA ***********************************************************
@app.route('/form')
def form():
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)  #debug = True is liye likha q k agr hm code m kuch
    # chnage kry to hmy hr bar server to dubara start krna pry ga 
    # app.run() m 2 parametrs dety hn, ek URL and dusra Port, url m nhi de rhi
    # q k m localhost use kr rhi hun or port bydefault 5000 hoti h






# ***********************  USAGE OF URL_FOR  *********************************
# URL_FOR IS A FLASK FUNCTION THAT IS USED TO CREATE AUTOMATIC URLS, yani hmary pas ek 
# web page h 'research', us webpage pr bhhhtttt sary URLs lgy hn, agr hm n research
# page ka URL chnage kia to hmy us page k saary URLs ko manually chnage krn pry ga, kuch esa
# hona chahye k hm just research page ka URL chnage kry and andr valy saary pages k 
# URLs automatically chnage ho jayn , to y possible h URL_FOR k zrye,

# means, if we chnage the url of research from 'home/research' to 'home/dashboard/research', 
# the about button in research page that will move us to about page, about URL will not 
# chnage automatically. it is still 'home/research/about' unless we manually chnage the 
# address inside @app.route() decorator. if we do not chnage URL for about chnage from 
# 'home/research/about' to 'home/dashboard/research/about' inside decoratr, the about button will not work,
# it will not move us to the about page. Now, URL_FOR advantage is that we do not have to
# manually chnage the about page URL inside Home page href = '', because URL_FOR 
# automatically update when we update the URl inside @app.route decorator, we will just 
# write: <a href="{{ url_for('about') }}" click to go to about>, instead 
# of <a href="home/dashboad/research/about" click to go to about >, we will just chnage the 
# about URL inside about decorator and we will just use <a href="{{ url_for('about') }} each time, and y
# new vala URL le le ga
 

