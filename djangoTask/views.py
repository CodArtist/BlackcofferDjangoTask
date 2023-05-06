from django.http import HttpResponse
from django.shortcuts import render
from py2neo import Graph
graph = Graph("neo4j+s://3b21ba85.databases.neo4j.io", auth=("neo4j", "SweMafBGC8X23iQpg98dhmE0aKwhV1eYuJuTPJK7W10"))

def HomePage(request):
    
    movie_results=[]
    if request.method == 'POST':
        search_query = request.POST.get('search')
        print(search_query)
        
        query = f'''MATCH (m:Movie)
                WHERE toLower(m.title) STARTS WITH {f"'{search_query.lower()}'"}
                OPTIONAL MATCH (m)<-[r]-(p:Person)
                RETURN m as movie, COLLECT({{person_details:p,relation:TYPE(r)}}) AS people
                '''
        data = graph.run(query).data()
        for e in data:
            people = []
            for p in e['people']:
                d={"name":p['person_details'].get('name'),
                   "born":p['person_details'].get('born'),
                   'relation':p['relation']}
                people.append(d)
            movie={'title': e['movie'].get('title'),
             'tagLine':e['movie'].get('tagline'),
             'year': e['movie'].get('released'),
             'people':people}
            movie_results.append(movie)
        print(movie_results)
       
    else:
        movie_results = []
    context = {
        'movie_results': movie_results
    }

    return render(request, 'HomePage.html', context)


def index(request):
    return HttpResponse("Hello, world!")