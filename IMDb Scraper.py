import os, imdb

def set_home_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

# Movie name should be in the following format: 'Name (YYYY) *'

os.system('cls')

set_home_directory()

def turn_red(skk): return ('\033[91m{}\033[00m'.format(skk)) 

def turn_green(skk): return ('\033[92m{}\033[00m'.format(skk)) 

movies = [[]]
for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        for ext in ['.mp4', '.avi', '.mkv', '.flv']:
            if ext in f:
                params = f.split('(')
                movies.append([params[0].strip(), params[1][:4].strip(), os.path.dirname(os.path.join(root, f))])

ia = imdb.IMDb()
failed_files = []

print('---------------------')
for m in movies:
    if len(m) > 1:
        print(m[0])
        found = False
        try:
            found_movies = ia.search_movie(title = m[0], results = 5) # Querying IMDb for movies with given title.
            for mov in found_movies:
                    ID = mov.movieID # Obtaining all IDs of queried movies.
                    mov_data = ia.get_movie(ID).data
                    if str(mov_data['year']) == str(m[1]) and str(mov_data['kind']) in ['movie', 'video movie']:
                        os.chdir(m[2])
                        found = True
                        file_name = str(m[0]) + '.txt'
                        file = open(file_name, 'w+', newline = '')
                        file.write(str(mov_data['genres']))
                        file.write('\n\n')
                        file.write(str(mov_data['plot outline']))
                        print(turn_green('Successful.'))
                        break
        except:
            failed_files.append('Exception: ' + str(m[0]) + '\n')
            print(turn_red('Unsuccessful.'))
            print('---------------------')
            continue
        if found == False:
            failed_files.append('Not found: ' + str(m[0]) + '\n')
            print(turn_red('Unsuccessful.'))
            print('---------------------')
            continue
        print('---------------------')

if len(failed_files) != 0:
    set_home_directory()
    failed_txt = open('Failed Files.txt', 'w+', newline='')
    for line in failed_files:
        failed_txt.write(line)
    

input('Press enter to close...')