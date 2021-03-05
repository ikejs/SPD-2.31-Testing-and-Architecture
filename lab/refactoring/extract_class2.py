# by Kami Bigdely
# Extract class

people = [
    {
        name: 'elizabeth debicki',
        birth_year: 1990,
        movies: ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
        email: 'deb@makeschool.com'
    },
    {
        name: 'Jim Carrey',
        birth_year: 1962,
        movies: ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'],
        email: 'jim@makeschool.com'
    }
]

def send_hiring_email(email):
    print("email sent to: ", email)
    
for person in people:
    if person.birth_year > 1985:
        print(person.name)
        print('Movies Played: ', end='')
        for m in person.movies:
            print(m, end=', ')
        print()
        send_hiring_email(value)
