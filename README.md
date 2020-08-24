# API POETRY

A REST API for poetry

## Table of Contents

* Get a random verse
* Get all verses

## API Documentation

### Get a random verse

Using the language / framework of your choice:
Load http://apipoetry.pythonanywhere.com/aVerse
The JSON response looks like that :
   ` {
        poetry: {
            author: "Cesare Pavese",
            id: 1,
            verse: "Moi, je commence à faire des poèmes quand la partie est perdue. On n'a jamais vu qu'un poème ait changé les choses."
         }
    } `
For example with javascript you can get a random verse like that : 
    `fetch('http://apipoetry.pythonanywhere.com/aVerse/')
    .then(function(body) { 
      return body.json(); 
    })
    .then(function(json) {
      let span = document.getElementById('aVerse');
      span.innerHTML = json.poetry.verse + " - " + json.poetry.author;
      console.log(json.poetry.id);
    });`
Enjoy the poetry ❤️
Bonus: Add a button to repeat the request for a new poetry!


### Get all verses

## License

    Copyright © 2020 Sarah Rubio & LeilusPocus

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the “Software”), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE. ```


