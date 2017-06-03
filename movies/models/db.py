db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True,signature=False)
"""
auth.settings.actions_disabled.append('profile')
auth.settings.actions_disabled.append('login')
auth.settings.actions_disabled.append('register')"""

db.define_table('directors', 
    Field('name',type='string'),
    Field('bio', type='text'), 
    format='%(name)s'
    )

db.define_table('genres', 
    Field('name'),
    format='%(name)s'
    )

db.define_table('films', 
    Field('title',type='string'),
    Field('imdb_rate',type='double'),
    Field('duration',type='integer'),
    Field('release_date', type='integer'),
    Field('storyline', type='text'),
    Field('director_id', 'reference directors'),
    Field('genre','list:reference genres'),

    format='%(title)s'
    )

'''db.define_table('genre_films', 
    Field('fid','reference films'),
    Field('gid',type='list:reference genres'), 
    )'''

db.define_table('comment', 
    Field('user_id', 'reference auth_user'),
    Field('title', type='string' ),
    Field('content', type='text'),
    Field('film_id', 'reference films'),
    Field('time', type='datetime', default=request.now),
    )

db.define_table('watch_list', 
    Field('owner',  'reference auth_user', unique=True),
    Field('film_list', 'list:reference films'),
    )

db.define_table('ratings', 
    Field('owner', 'reference auth_user'),
    Field('film', 'reference films' ),
    Field('rate', type='integer'),
    )