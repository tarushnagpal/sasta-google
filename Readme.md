# Sasta Google

Sasta Google is a cloud-enabled, versatile information retreival system system which is deployed as an API!

  - Make a post request to /search with search query as parameter
  - Get documents with score as response
  - Easy!

# Features

  - Retrieval of information from any type of documents
  - Ranking of documents based on proximity to search query
  - Ranking words according to their probability distribution in the documents ( For Autocomplete )

### Tech

Sasta-Google uses a number of open source projects to work properly:

* Textract - Text extractor for Python
* Django - Deployment to server
* Django-rest-framework - Deploying API
* [jQuery] - duh

### Usage

On web(Jquery):
```
$.post("http://www.sasta-google.com/search/",
{
    search: search_val.toLowerCase()
},
function(data, status){
    console.log(data)
});
```

On C#:
```
var values = new Dictionary<string>
{
   { "search", "This is the Query" }
};

var content = new FormUrlEncodedContent(values);

var response = await client.PostAsync("http://www.sasta-goole.com/search/", content);

var responseString = await response.Content.ReadAsStringAsync();
```

On Python:
```
r = requests.post("http://www.sasta-google.com/search/", data={'search': 'this is the query'} )
```

### Deploying on your Own Machine

Run ```build.py``` in your folder with documents in 'data/' and you're Good!
Now you can pass search query to ```search.py``` and receive data!



