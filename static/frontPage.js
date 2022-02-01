const plus = document.getElementById("plus")
const limitValue = document.getElementById("limitValue")
const minus = document.getElementById("minus")
const movieLensGrid=document.getElementById('movieLensGrid')
var genreString=document.getElementById('genreString')
// var recordLimit=document.getElementById('recordLimit')

var limitNum=4 //limit
var genreSelectedArray=[]
var movieLensTableData=[
    {
        "movieId": 318,
        "title": "Shawshank Redemption, The (1994)",
        "genres": "['Crime', 'Drama']",
        "year": "1994",
        "L_Rating": 4.4135413087,
        "User_Count": 81482.0
    },
    {
        "movieId": 170705,
        "title": "Band of Brothers (2001)",
        "genres": "['Action', 'Drama', 'War']",
        "year": "2001",
        "L_Rating": 4.396539028,
        "User_Count": 1356.0
    },
    {
        "movieId": 858,
        "title": "Godfather, The (1972)",
        "genres": "['Crime', 'Drama']",
        "year": "1972",
        "L_Rating": 4.3242857143,
        "User_Count": 52498.0
    },
    {
        "movieId": 1221,
        "title": "Godfather: Part II, The (1974)",
        "genres": "['Crime', 'Drama']",
        "year": "1974",
        "L_Rating": 4.2616847031,
        "User_Count": 34188.0
    },
    {
        "movieId": 198185,
        "title": "Twin Peaks (1989)",
        "genres": "['Drama', 'Mystery']",
        "year": "1989",
        "L_Rating": 4.2586206897,
        "User_Count": 288.0
    },
    {
        "movieId": 2019,
        "title": "Seven Samurai (Shichinin no samurai) (1954)",
        "genres": "['Action', 'Adventure', 'Drama']",
        "year": "1954",
        "L_Rating": 4.2545814945,
        "User_Count": 13367.0
    },
    {
        "movieId": 163809,
        "title": "Over the Garden Wall (2013)",
        "genres": "['Adventure', 'Animation', 'Drama']",
        "year": "2013",
        "L_Rating": 4.253649635,
        "User_Count": 546.0
    },
    {
        "movieId": 527,
        "title": "Schindler's List (1993)",
        "genres": "['Drama', 'War']",
        "year": "1993",
        "L_Rating": 4.2475377816,
        "User_Count": 60411.0
    },
    {
        "movieId": 1203,
        "title": "12 Angry Men (1957)",
        "genres": "['Drama']",
        "year": "1957",
        "L_Rating": 4.2428640396,
        "User_Count": 16569.0
    },
    {
        "movieId": 2959,
        "title": "Fight Club (1999)",
        "genres": "['Action', 'Crime', 'Drama', 'Thriller']",
        "year": "1999",
        "L_Rating": 4.2282688218,
        "User_Count": 58773.0
    },
    {
        "movieId": 1193,
        "title": "One Flew Over the Cuckoo's Nest (1975)",
        "genres": "['Drama']",
        "year": "1975",
        "L_Rating": 4.21859401,
        "User_Count": 36058.0
    },
    {
        "movieId": 912,
        "title": "Casablanca (1942)",
        "genres": "['Drama', 'Romance']",
        "year": "1942",
        "L_Rating": 4.2064740443,
        "User_Count": 26890.0
    },
    {
        "movieId": 922,
        "title": "Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)",
        "genres": "['Drama', 'Film-Noir', 'Romance']",
        "year": "1950",
        "L_Rating": 4.2061736771,
        "User_Count": 7368.0
    },
    {
        "movieId": 202439,
        "title": "Parasite (2019)",
        "genres": "['Comedy', 'Drama']",
        "year": "2019",
        "L_Rating": 4.2048192771,
        "User_Count": 496.0
    },
    {
        "movieId": 44555,
        "title": "Lives of Others, The (Das leben der Anderen) (2006)",
        "genres": "['Drama', 'Romance', 'Thriller']",
        "year": "2006",
        "L_Rating": 4.2001307332,
        "User_Count": 9177.0
    },
    {
        "movieId": 148298,
        "title": "Awaken (2013)",
        "genres": "['Drama', 'Romance', 'Sci-Fi']",
        "year": "2013",
        "L_Rating": 4.2,
        "User_Count": 3.0
    },
    {
        "movieId": 118268,
        "title": "Borrowed Time (2012)",
        "genres": "['Drama']",
        "year": "2012",
        "L_Rating": 4.2,
        "User_Count": 3.0
    },
    {
        "movieId": 158958,
        "title": "Pollyanna (2003)",
        "genres": "['Children', 'Drama']",
        "year": "2003",
        "L_Rating": 4.2,
        "User_Count": 13.0
    },
    {
        "movieId": 179731,
        "title": "Sound of Christmas (2016)",
        "genres": "['Drama']",
        "year": "2016",
        "L_Rating": 4.2,
        "User_Count": 3.0
    },
    {
        "movieId": 1178,
        "title": "Paths of Glory (1957)",
        "genres": "['Drama', 'War']",
        "year": "1957",
        "L_Rating": 4.1987781955,
        "User_Count": 4254.0
    },
    {
        "movieId": 3435,
        "title": "Double Indemnity (1944)",
        "genres": "['Crime', 'Drama', 'Film-Noir']",
        "year": "1944",
        "L_Rating": 4.1935812061,
        "User_Count": 5404.0
    },
    {
        "movieId": 296,
        "title": "Pulp Fiction (1994)",
        "genres": "['Comedy', 'Crime', 'Drama', 'Thriller']",
        "year": "1994",
        "L_Rating": 4.1888821949,
        "User_Count": 79672.0
    },
    {
        "movieId": 6016,
        "title": "City of God (Cidade de Deus) (2002)",
        "genres": "['Action', 'Adventure', 'Crime', 'Drama', 'Thriller']",
        "year": "2002",
        "L_Rating": 4.1814686369,
        "User_Count": 19894.0
    },
    {
        "movieId": 1213,
        "title": "Goodfellas (1990)",
        "genres": "['Crime', 'Drama']",
        "year": "1990",
        "L_Rating": 4.1804530843,
        "User_Count": 32663.0
    },
    {
        "movieId": 175981,
        "title": "Twelve Angry Men (1954)",
        "genres": "['Drama']",
        "year": "1954",
        "L_Rating": 4.1699029126,
        "User_Count": 101.0
    },
    {
        "movieId": 926,
        "title": "All About Eve (1950)",
        "genres": "['Drama']",
        "year": "1950",
        "L_Rating": 4.1692307692,
        "User_Count": 5068.0
    },
    {
        "movieId": 58559,
        "title": "Dark Knight, The (2008)",
        "genres": "['Action', 'Crime', 'Drama', 'IMAX']",
        "year": "2008",
        "L_Rating": 4.1664820211,
        "User_Count": 41519.0
    },
    {
        "movieId": 79132,
        "title": "Inception (2010)",
        "genres": "['Action', 'Crime', 'Drama', 'Mystery', 'Sci-Fi', 'Thriller', 'IMAX']",
        "year": "2010",
        "L_Rating": 4.1554490064,
        "User_Count": 38895.0
    },
    {
        "movieId": 2324,
        "title": "Life Is Beautiful (La Vita \u00e8 bella) (1997)",
        "genres": "['Comedy', 'Drama', 'Romance', 'War']",
        "year": "1997",
        "L_Rating": 4.1542455584,
        "User_Count": 23976.0
    },
    {
        "movieId": 26082,
        "title": "Harakiri (Seppuku) (1962)",
        "genres": "['Drama']",
        "year": "1962",
        "L_Rating": 4.1522346369,
        "User_Count": 714.0
    },
    {
        "movieId": 5971,
        "title": "My Neighbor Totoro (Tonari no Totoro) (1988)",
        "genres": "['Animation', 'Children', 'Drama', 'Fantasy']",
        "year": "1988",
        "L_Rating": 4.1522157996,
        "User_Count": 9340.0
    },
    {
        "movieId": 1207,
        "title": "To Kill a Mockingbird (1962)",
        "genres": "['Drama']",
        "year": "1962",
        "L_Rating": 4.1462972229,
        "User_Count": 15986.0
    },
    {
        "movieId": 1217,
        "title": "Ran (1985)",
        "genres": "['Drama', 'War']",
        "year": "1985",
        "L_Rating": 4.141612409,
        "User_Count": 5220.0
    }
]

tableIndex=1 //count of table rows
movieLensTableData.forEach(_=>{
    var row = movieLensGrid.insertRow(tableIndex++);
    row.insertCell(0).innerText=_.title
    row.insertCell(1).innerText=_.genres
    row.insertCell(2).innerText=_.year
    row.insertCell(3).innerText=_.L_Rating

})

function addCheckedGenre(val){
    let ind=genreSelectedArray.indexOf(val)
    if(ind>=0) genreSelectedArray.splice(ind,1)
    else genreSelectedArray.push(val)
    console.log(genreSelectedArray);

    var res= genreSelectedArray.reduce((prev,cur,ind)=>{return prev+(ind>0?" or ":"")+`genre like '${cur}'`},"")
    console.log(res);
    genreString.value=res;
}

plus.addEventListener('click', (event)=>{
    limitValue.innerText=++limitNum;
    if(limitNum>=100) plus.style.visibility="hidden";
    else minus.style.visibility="visible"
    recordLimit.value=limitNum
} )

minus.addEventListener('click', (event)=>{
    limitValue.innerText=--limitNum;
    console.log(limitNum);
    if(limitNum<=1) minus.style.visibility="hidden";
    else plus.style.visibility="visible"
    recordLimit.value=limitNum
} )