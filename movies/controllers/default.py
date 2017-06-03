# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
import time
"""
film_data = [{'name':'The Shawshank Redemption',
              'director':1,
              'genres':['Crime','Drama'],
              'imdb_rating':9.2,
              'duration':142,
              'release_date':1994,
              'storyline':"Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he claims he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red."
             },
             {'name':'The Green Mile',
              'director':1,
              'genres':['Crime','Drama','Fantastic'],
              'imdb_rating':8.5,
              'duration':189,
              'release_date':1999,
              'storyline':"The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift."
             },
             {'name':'Spectre',
              'director':2,
              'genres':['Action','Adventure'],
              'imdb_rating':7.2,
              'duration':148,
              'release_date':2015,
              'storyline':"A cryptic message from Bond's past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to reveal the terrible truth behind SPECTRE."
             },
             {'name':'The Godfather',
              'director':3,
              'genres':['Crime','Drama'],
              'imdb_rating':9.2,
              'duration':175,
              'release_date':1972,
              'storyline':"The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
             },
             {'name':'Forrest Gump',
              'director':4,
              'genres':['Romance','Drama'],
              'imdb_rating':8.8,
              'duration':142,
              'release_date':1994,
              'storyline':"Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him."
             },
             {'name':'The Dark Knight',
              'director':5,
              'genres':['Fantastic','Action'],
              'imdb_rating':9.0,
              'duration':152,
              'release_date':2008,
              'storyline':"When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice."
             },
             {'name':'Inception',
              'director':5,
              'genres':['Action','Drama'],
              'imdb_rating':8.8,
              'duration':148,
              'release_date':2010,
              'storyline':"A thief who steals corporate secrets through use of the dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO."
             },
             {'name':'Fight Club',
              'director':6,
              'genres':['Drama'],
              'imdb_rating':8.9,
              'duration':139,
              'release_date':1999,
              'storyline':"An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more..."
             },
             {'name':'12 Angry Men',
              'director':7,
              'genres':['Crime','Drama'],
              'imdb_rating':8.9,
              'duration':96,
              'release_date':1957,
              'storyline':"A dissenting juror in a murder trial slowly manages to convince the others that the case is not as obviously clear as it seemed in court."
             },
             {'name':'Tosun Paşa',
              'director':12,
              'genres':['Comedy','History'],
              'imdb_rating':8.8,
              'duration':142,
              'release_date':1976,
              'storyline':"Late 19th century in Alexandria. Two traditionally rival Turkish families, Seferoglus and Tellioglus are competing for the Green Valley. The winner will be determined by Daver Bey, who has a beautiful young daughter, Leyla. Both families try to arrange a marriage between a man from their family and Leyla, so that Daver Bey will be inclined to give the green valley to his relatives. Tellioglus, who are behind in the race, desperately find a final solution"
             },
             {'name':'The Prestige',
              'director':5,
              'genres':['Mystery','Sci-fi'],
              'imdb_rating':8.5,
              'duration':130,
              'release_date':2006,
              'storyline':"Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion."
             },
             {'name':'Leon',
              'director':8,
              'genres':['Crime','Drama','Thriller'],
              'imdb_rating':8.6,
              'duration':110,
              'release_date':1994,
              'storyline':"Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a professional assassin, after her family is murdered. Léon and Mathilda form an unusual relationship, as she becomes his protégée and learns the assassin's trade."
             },
             {'name':'Gladiator',
              'director':9,
              'genres':['Action','Drama'],
              'imdb_rating':8.5,
              'duration':155,
              'release_date':2000,
              'storyline':"When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge."
             },
             {'name':'Braveheart',
              'director':10,
              'genres':['History','Drama'],
              'imdb_rating':8.4,
              'duration':178,
              'release_date':1995,
              'storyline':"When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt and leads Scottish warriors against the cruel English tyrant who rules Scotland with an iron fist."
             },
             {'name':'3 Idiots',
              'director':11,
              'genres':['Comedy','Drama'],
              'imdb_rating':8.5,
              'duration':170,
              'release_date':2009,
              'storyline':"Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots."
             }]

director_data = [{  'id':1 , 'name':'Frank Darabont', 'bio':"Three-time Oscar nominee Frank Darabont was born in a refugee camp in 1959 in Montbeliard, France, the son of Hungarian parents who had fled Budapest during the failed 1956 Hungarian revolution. Brought to America as an infant, he settled with his family in Los Angeles and attended Hollywood High School. His first job in movies was as a production assistant on the 1981 low-budget film, Hell Night (1981), starring Linda Blair. He spent the next six years working in the art department as a set dresser and in set construction while struggling to establish himself as a writer. His first produced writing credit (shared) was on the 1987 film, A Nightmare on Elm Street 3: Dream Warriors (1987), directed by Chuck Russell. Darabont is one of only six filmmakers in history with the unique distinction of having his first two feature films receive nominations for the Best Picture Academy Award: 1994's The Shawshank Redemption (1994) (with a total of seven nominations) and 1999's The Green Mile (1999) (four nominations). Darabont himself collected Oscar nominations for Best Adapted Screenplay for each film (both based on works by Stephen King), as well as nominations for both films from the Director's Guild of America, and a nomination from the Writers Guild of America for The Shawshank Redemption (1994). He won the Humanitas Prize, the PEN Center USA West Award, and the Scriptor Award for his screenplay of 'The Shawshank Redemption'. For 'The Green Mile', he won the Broadcast Film Critics prize for his screenplay adaptation, and two People's Choice Awards in the Best Dramatic Film and Best Picture categories. His most recent feature as director, The Majestic (2001), starring Jim Carrey, was released in December 2001. His next film as director will be an adaptation of Ray Bradbury's classic science fiction novel, Fahrenheit 451 (2007), which Darabont is currently writing for Castle Rock and Icon Productions. He is currently executive-producing the thriller, Collateral (2004), for DreamWorks, with Michael Mann directing and Tom Cruise starring. Future produced-by projects include 'Way of the Rat' at DreamWorks with Chuck Russell adapting and directing the CrossGen comic book series and 'Back Roads', a Tawni O'Dell novel, also at DreamWorks, with Todd Field attached to direct. Darabont and his production company, 'Darkwoods Productions', have an overall deal with Paramount Pictures."},
                 {  'id':2, 'name':'Sam Mendes', 'bio':"Samuel Alexander Mendes was born on August 1, 1965 in Reading, England, UK to parents James Peter Mendes, a retired university lecturer, and Valerie Helene Mendes, an author who writes children's books. Their marriage didn't last long, James divorced Sam's mother in 1970 when Sam was just 5-years-old. Sam was educated at Cambridge University and joined the Chichester Festival Theatre following his graduation in 1987. Afterwards, he directed Judi Dench in 'The Cherry Orchard', for which he won a Critics Circle Award for Best Newcomer. He then joined the Royal Shakespeare Company, where he directed such productions as 'Troilus and Cressida' with Ralph Fiennes and 'Richard III'. In 1992, he became artistic director of the reopened Donmar Warehouse in London, where he directed such productions as 'The Glass Menagerie' and the revival of the musical 'Cabaret', which earned four Tony Awards including one for Best Revival of a Musical. He also directed 'The Blue Room' starring Nicole Kidman. In 1999, he got the chance to direct his first feature film, American Beauty (1999). The movie earned 5 Academy Awards including Best Picture and Best Director for Mendes, which is a rare feat for a first-time film director."},
                 {  'id':3, 'name':'Francis Ford Coppola', 'bio':"Francis Ford Coppola was born in 1939 in Detroit, Michigan, but grew up in a New York suburb in a creative, supportive Italian-American family. His father, Carmine Coppola, was a composer and musician. His mother, Italia Coppola (née Pennino), had been an actress. Francis Ford Coppola graduated with a degree in drama from Hofstra University, and did graduate work at UCLA in filmmaking. He was training as assistant with filmmaker Roger Corman, working in such capacities as sound-man, dialogue director, associate producer and, eventually, director of Dementia 13 (1963), Coppola's first feature film. During the next four years, Coppola was involved in a variety of script collaborations, including writing an adaptation of 'This Property is Condemned' by Tennessee Williams (with Fred Coe and Edith Sommer), and screenplays for Is Paris Burning? (1966) and Patton (1970), the film for which Coppola won a Best Original Screenplay Academy Award. In 1966, Coppola's 2nd film brought him critical acclaim and a Master of Fine Arts degree. In 1969, Coppola and George Lucas established American Zoetrope, an independent film production company based in San Francisco. The company's first project was THX 1138 (1971), produced by Coppola and directed by Lucas. Coppola also produced the second film that Lucas directed, American Graffiti (1973), in 1973. This movie got five Academy Award nominations, including one for Best Picture. In 1971, Coppola's film The Godfather (1972) became one of the highest-grossing movies in history and brought him an Oscar for writing the screenplay with Mario Puzo The film was a Best Picture Academy Award-winner, and also brought Coppola a Best Director Oscar nomination. Following his work on the screenplay for The Great Gatsby (1974), Coppola's next film was The Conversation (1974), which was honored with the Golden Palm Award at the Cannes Film Festival, and brought Coppola Best Picture and Best Original Screenplay Oscar nominations. Also released that year, The Godfather: Part II (1974), rivaled the success of The Godfather (1972), and won six Academy Awards, bringing Coppola Oscars as a producer, director and writer. Coppola then began work on his most ambitious film, Apocalypse Now (1979), a Vietnam War epic that was inspired by Joseph Conrad's Heart of Darkness (1993). Released in 1979, the acclaimed film won a Golden Palm Award at the Cannes Film Festival, and two Academy Awards. Also that year, Coppola executive produced the hit The Black Stallion (1979). With George Lucas, Coppola executive produced Kagemusha (1980), directed by Akira Kurosawa, and Mishima: A Life in Four Chapters (1985), directed by Paul Schrader and based on the life and writings of Yukio Mishima. Coppola also executive produced such films as The Escape Artist (1982), Hammett (1982) The Black Stallion Returns (1983), Barfly (1987), Wind (1992), The Secret Garden (1993), etc."},
                 {  'id':4, 'name':'Robert Zemeckis', 'bio':"A whiz-kid with special effects, Robert is from the Spielberg camp of film-making (Steven Spielberg produced many of his films). Usually working with writing partner Bob Gale, Robert's earlier films show he has a talent for zany comedy (Romancing the Stone (1984), 1941 (1979)) and special effect vehicles (Who Framed Roger Rabbit (1988) and Back to the Future (1985)). His later films have become more serious, with the hugely successful Tom Hanks vehicle Forrest Gump (1994) and the Jodie Foster film Contact (1997), both critically acclaimed movies. Again, these films incorporate stunning effects. Robert has proved he can work a serious story around great effects."},
                 {  'id':5, 'name':'Christopher Nolan', 'bio':"Best known for his cerebral, often nonlinear story-telling, acclaimed writer-director Christopher Nolan was born on July 30, 1970 in London, England. Over the course of 15 years of film-making, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made"},
                 {  'id':6, 'name':' David Fincher', 'bio':"David Fincher was born in 1962 in Denver, Colorado, and was raised in Marin County, California. When he was 18 years old he went to work for John Korty at Korty Films in Mill Valley. He subsequently worked at ILM (Industrial Light and Magic) from 1981-1983. Fincher left ILM to direct TV commercials and music videos after signing with N. "},
                 {  'id':7, 'name':'Sidney Lumet', 'bio':"Sidney Lumet was a master of cinema, best known for his technical knowledge and his skill at getting first-rate performances from his actors -- and for shooting most of his films in his beloved New York. He made over 40 movies, often complex and emotional, but seldom overly sentimental. "},
                 {  'id':8, 'name':'Luc Besson', 'bio':"Luc Besson spent the first years of his life following his parents, scuba diving instructors, around the world. His early life was entirely aquatic. He already showed amazing creativity as a youth, writing early drafts of Derinlik sarhoslugu (1988) and 5. Güç (1997), as an adolescent bored in school"},
                 {  'id':9, 'name':' Ridley Scott', 'bio':"Ridley Scott was born in South Shields, Tyne and Wear (then Northumberland) on 30 November 1937. His father was an officer in the Royal Engineers and the family followed him as his career posted him throughout the UK and Europe before they eventually returned to Teesside."},
                 {  'id':10, 'name':'Mel Gibson', 'bio':"Mel Columcille Gerard Gibson was born January 3, 1956 in Peekskill, New York, USA, as the sixth of eleven children of Hutton Gibson, a railroad brakeman, and Anne Patricia (Reilly) Gibson (who died in December of 1990). His mother was Irish, from County Longford, while his American-born father is of mostly Irish descent."},
                 {  'id':11, 'name':' Rajkumar Hirani', 'bio':"Rajkumar Hirani was born on November 20, 1962 in Nagpur, Maharashtra, India. He is a writer and editor, known for 3 Aptal (2009), PK (2014) and Munna Bhai M.B.B.S. (2003). "},
                 {  'id':12, 'name':' Kartal Tibet', 'bio':"Kartal Tibet was born on March 27, 1939 in Ankara, Turkey. He is an actor and director, known for Tosun Pasa (1976)"}
                ]
db.directors.truncate()
for d in director_data:
  db.directors.insert(name=d['name'], bio= d['bio'])

db.genres.truncate()
genre_list = []
for film in film_data:
  genre_list.extend(film['genres'])
genre_list = list(set(genre_list))
for genre in genre_list:
  db.genres.insert(name=genre)

db.films.truncate()
for f in film_data:
  genreId_list = []
  for g in f['genres']:
    row = db(db.genres.name==g).select().first()
    gid = row.id
    genreId_list.append(gid)
  db.films.insert(title=f['name'],
    imdb_rate=f['imdb_rating'],
    duration=f['duration'],
    release_date=f['release_date'],
    storyline=f['storyline'],
    director_id=f['director'],
    genre=genreId_list
    )
"""

def index():
    '''db.comment.truncate()
    db.films.truncate()
    db.directors.truncate()
    db.watch_list.truncate()'''
    title = "Homepage"
    #rows = db(db.films.title.contains('green')).select().first()
    return dict(title=title)

def about():
    title = "About"
    return dict(title=title)

def films():
    #db.watch_list.truncate()
    #rows=db(db.genres.name == "Crime").select().first()
    #print rows.id
    title = "Films"
    search = request.vars.s
    if(search):
    	film_data = db(db.films.title.contains(search)).select()
    else:
    	film_data = db(db.films).select()

    director_data = db(db.directors).select()
    genres=db(db.genres).select()
    for f in film_data:
      f['genre_names'] = db.films.genre.represent(f.genre) # returns name list
    #print genres


    return dict(title=title, films=film_data, directors=director_data)

def film():
    #db.comment.insert(user_id=auth.user.id,title="as",content="def")
    #directors
    k = int(request.args[0])
    film_data = db(db.films.id == k).select().first()
    film_data['genre_names'] = db.films.genre.represent(film_data.genre)
    director_data = db(db.directors.id == film_data['director_id']).select().first()
    title = film_data['title']
    #comments
    comment_obj = db(db.comment.film_id==k).select(orderby='comment.time DESC')

    form = FORM(DIV(INPUT(_type='text',_name='title', _placeholder='Title'),_class="field"),
                DIV(TEXTAREA(_type='text',_name='content', _placeholder='Content',_rows=10,_style='resize:none;'),_class="field"),
                INPUT(_type='submit', _class='ui button',_value='Submit') ,_action=URL('add_comment/%d' %k), _class="ui form"
                )
    return dict(title=title, film=film_data, director=director_data, datas=comment_obj, form=form)


def directors():
    title = "Directors"
    film_data = db(db.films).select()
    director_data = db(db.directors).select()
    return dict(title=title, films=film_data, directors=director_data)



def director():
    k = int(request.args[0])
    director_data = db(db.directors.id == k).select().first()
    #print director_data
    film_data = db(db.films.director_id==director_data.id).select()
    title = director_data['name']
    return dict(title = title,film=film_data ,director=director_data)

def category():
  
  gid = int(request.args[1])
  genre_data = db(db.genres.id == gid).select().first()
  title=genre_data.name
  film_data=db(db.films).select()
  director_data = db(db.directors).select()

  data = []
  for f in film_data:
    if(gid in f.genre):
      data.append(f)
  

  return dict(title=title,film_data=data,genre_data=genre_data,directors=director_data)

def login():
  form = FORM(DIV(INPUT(_type='text',_name='username', _placeholder='Username'),_class="field"),
              DIV(INPUT(_type='password',_name='password', _placeholder='Password'),_class="field"),
              INPUT(_type='submit', _class='ui button',_value='Login') , _class="ui form"
              )
  username = request.post_vars.username
  password = request.post_vars.password
  user = auth.login_bare(username,password) # returns user if exist 
  if(user):
    redirect(URL('index'))

  return dict(title="",form=form)


def register():
    title = ""
    form = FORM(DIV(INPUT(_type='text',_name='first_name', _placeholder='Firstname'),_class="field"),
              DIV(INPUT(_type='text',_name='last_name', _placeholder='Lastname'),_class="field"),
              DIV(INPUT(_type='text',_name='username', _placeholder='Username'),_class="field"),
              DIV(INPUT(_type='text',_name='email', _placeholder='Email'),_class="field"),
              DIV(INPUT(_type='password',_name='password', _placeholder='Password'),_class="field"),
              DIV(INPUT(_type='password',_name='password_two', _placeholder='Confirm password'),_class="field"),
              INPUT(_type='submit', _class='ui button',_value='Register') , _class="ui form"
              )
    first_name = request.post_vars.first_name
    last_name = request.post_vars.last_name
    username = request.post_vars.username
    email = request.post_vars.email
    password = request.post_vars.password
    password_two = request.post_vars.password_two
    if(email and username and password and password_two):
      if(password==password_two):
        db.auth_user.validate_and_insert( username = username, 
                                          first_name = first_name,
                                          last_name = last_name,
                                          password = password,
                                          email = email,
                                          )
        user = auth.login_bare(username,password)
        if(user):
          redirect(URL('index'))
    else:
      pass
    return dict(title=title,form=form)


@auth.requires_login(URL('login'))
def logout():
  title = "logout"
  return auth.logout()
  return locals

@auth.requires_login(URL('login'))
def profile():
    user = auth.user
    title = 'Profile'
    form = FORM(DIV(INPUT(_type='text',_name='first_name', _placeholder='Firstname', _value=user.first_name),_class="field"),
              DIV(INPUT(_type='text',_name='last_name', _placeholder='Lastname',_value=user.last_name),_class="field"),
              DIV(INPUT(_type='text',_name='username', _placeholder='Username',_value=user.username, _disabled=""),_class="field"),
              DIV(INPUT(_type='text',_name='email', _placeholder='Email',_value=user.email),_class="field"),
              INPUT(_type='button', _class='ui button',_id='apply-changes-button',_value='Apply Changes') , _class="ui form", _id='form1'
              )
    if request.post_vars:
    	first_name = request.post_vars.first_name
    	last_name = request.post_vars.last_name
    	email = request.post_vars.email
    	password = request.post_vars.password
    	#print password,email,first_name,last_name
    	#email must be entered
    	if(email):
    		db(db.auth_user.id==user.id).update(first_name=first_name, last_name=last_name, email=email)
    		auth.login_bare(user.username, password)
    		redirect(URL('profile'))
    comment_data = db(db.comment.user_id == auth.user.id).select(orderby='comment.time DESC')
    return dict(title=title, form=form, comments=comment_data)

@auth.requires_login(URL('login'))
def add_comment():
    title = "Add comment"
    #db.comment.truncate()
    #db.auth_user.truncate()
    #form = SQLFORM(db.comment)
    fid = request.args[0]
    t = request.post_vars.title
    c = request.post_vars.content
    #print c,t
    if(c and t):
      db.comment.insert(user_id=auth.user.id, title=t, content=c, film_id=fid)
      f = 'film/%s' %fid
      redirect(URL(f))



@auth.requires_login(URL('login'))
def edit_comment():
    k = int(request.args[0])
    fid = db(db.comment.id==k).select().first()['film_id']
    comment_obj = db(db.comment.id==k).select().first()
    if(comment_obj['user_id']==auth.user.id):
      t = request.post_vars.title
      c = request.post_vars.content
      if(c and t):
        db(db.comment.id==k).update(title=t, content=c)
        #redirect(URL('index', args=(1,2,3), vars=dict(a='b'))) passing parameter in redirect
        redirect(URL('film', args=(fid), vars=dict()))
      #print comment_obj
    else:
      film = 'film/%s' %fid
      redirect(URL(film))
    form = FORM(DIV(INPUT(_type='text',_name='title',_value=comment_obj['title']),_class='field'),
                DIV(TEXTAREA(_type='text',_name='content',_rows=10,_style='resize:none;', _value=comment_obj['content'] ), _class="field"), 
                INPUT(_type='submit', _class='ui button',_value='Submit') , _class="ui form", _action=URL('edit_comment/%d' %k)
                )
    
    return dict(title="",form=form)

@auth.requires_login(URL('login'))
def watchlist():
    title = 'My Watchlist'
    watchlist = db(db.watch_list.owner==auth.user.id).select().first()
    film_data = db(db.films).select()
    film_list = []
    if(watchlist):
      for f in film_data:
        if(f.id in watchlist['film_list']):
          film_list.append(f)
    else:
      film_list = []
    #print film_list
    return dict(title=title,films=film_list)

@auth.requires_login(URL('login'))
def add_watch_list():
    fid = int(request.args[0])
    owner = auth.user.id
    film_data = db(db.watch_list.owner==owner).select().first()
    #print film_data
    if(film_data):
      if fid in film_data.film_list:
        pass
      else:
        film_data.film_list.append(fid)
        db(db.watch_list.owner==owner).update(film_list=film_data.film_list)

    else:
      film_list = []
      film_list.append(fid)
      db.watch_list.insert(owner=owner, film_list=film_list)
    redirect(URL('films'))

@auth.requires_login(URL('login'))
def remove_watch_list():
    fid = fid = int(request.args[0])
    owner = auth.user.id
    film_data = db(db.watch_list.owner==owner).select().first()
    if(film_data):
      if(fid in film_data.film_list):
        film_data.film_list.remove(fid)
        db(db.watch_list.owner==owner).update(film_list=film_data.film_list)
        redirect(URL('watchlist'))
    else:
      pass

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


