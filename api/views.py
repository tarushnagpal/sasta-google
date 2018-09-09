from django.http import JsonResponse
import json
import pprint
import math

global_index = {}
global_directory = []
global_vocabulary = []
global_sizes = []
global_autocomplete = []

prefix = "../../"
# prefix = ""

with open( prefix + "index.json", "r") as f:
    global_index = json.load(f)

old_index = global_index
global_index = {int(k):{int(i):[int(j) for j in global_index[k][i] ] for i in v} for k,v in global_index.items()}

with open(prefix + "autocomplete.json", "r") as f:
    for line in f:
        global_autocomplete.append(line.strip())

with open(prefix + "global_sizes.json", "r") as f:
    for line in f:
        global_sizes.append(line.strip())

with open(prefix + "directory.json", "r") as f:
    for line in f:
        global_directory.append(line.strip())

total_docs = len(global_directory) + 1
with open(prefix + "vocabulary.json", "r") as f:
    for line in f:
        global_vocabulary.append(line.strip())

def get_total_frequency(filename):
    return( global_sizes[ global_directory.index(filename) ] )

def search(search_term):
    print(search_term)
    search_terms = str(search_term).split("+")
    total_occurences = {}

    count = 0
    total_search_index = {}

    #Building Iniital Index with only documents containing search terms
    for i in search_terms:
        try:
            term_index = global_index [ global_vocabulary.index(i) ]
            for j in term_index:
                document_location = global_directory[j]
                if(document_location in total_search_index):
                    temp_list = total_search_index[ document_location ]
                    if( j in temp_list ):
                        temp_list_inner = temp_list[j]
                        temp_list_inner.append( global_index[global_vocabulary.index(i)][j] )
                        total_search_index[ document_location ] = temp_list_inner
                    else:
                        total_search_index[document_location][i] = global_index[global_vocabulary.index(i)][j]
                else:
                    total_search_index[ document_location ] = { i : global_index[global_vocabulary.index(i)][j] }
        except:
            print("nahi he bro")

    score = {}
    idf = {}

    # for i in search_terms:
    #     try:
    #         idf[i] =
    #     except:
    #         print("Nahi mila")

    #For each term closenss
    for i in total_search_index:

        for j in search_terms:
            term_frequency = total_search_index[i]

            try:
                if( i in score ):
                    score[i] += math.log( total_docs / len(old_index[str(global_vocabulary.index(j))].keys()) ) * (len(term_frequency[j])/int(get_total_frequency(i)))
                else:
                    score[i] = math.log( total_docs / len(old_index[str(global_vocabulary.index(j))].keys()) ) * (len(term_frequency[j])/int(get_total_frequency(i)))
            except:
                print('',end='')


        if( len(total_search_index[i]) > 1 ):
            keys = list(total_search_index[i].keys() )

            for x in range(len(keys)):
                for z in total_search_index[i][keys[x]] :
                    # print(total_search_index[i][keys[x]])
                    xx = x+1
                    if(xx<len(keys)):
                        for aa in total_search_index[i][keys[xx]]:
                            if( aa - z < 7 and aa - z > 0 ):
                                print(i,keys[xx],keys[x],aa,z)
                                score[i] += math.exp(z-aa)*100
                                print(math.exp(z-aa)*100)



                # for z in total_search_index[i][j]:
                #     print(z)

    #For sequence finding
    print(score)
    return(sorted( score.items(), key=lambda x: score.get(x[0])) )

def autoComplete():
    return(global_autocomplete)

def getSearch(request):
    body_unicode = request.body.decode('utf-8')
    req = body_unicode
    query = str(req).split('=')[1]
    return JsonResponse(search(query), status=200, safe=False )

def getAutocomplete(request):
    return JsonResponse( autoComplete(), status=200, safe=False )