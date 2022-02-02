
const plus = document.getElementById("plus")
const limitValue = document.getElementById("limitValue")
const minus = document.getElementById("minus")
const similarUserGenre = document.getElementById('similarUserGenre')
const similarUserRating = document.getElementById('similarUserRating')
const similarUserMovieId = document.getElementById('similarUserMovieId')
const filterButton = document.getElementById('filterButton')
const getCountButton = document.getElementById('getCountButton')
// const movieLensGrid=document.getElementById('movieLensGrid')
var genreString=document.getElementById('genreString')
var recordLimit=document.getElementById('recordLimit')
var similarUserGenreHidden= document.getElementById('similarUserGenreHidden')
var similarUserRatingHidden = document.getElementById('similarUserRatingHidden')
var similarUserMovieIdHidden = document.getElementById('similarUserMovieIdHidden')


//repopulating data from python to maintain the state
// similarUserGenre.value=similarUserGenreHidden.value;
similarUserRating.value=similarUserRatingHidden.value;
similarUserMovieId.value=similarUserMovieIdHidden.value;

var limitNum=limitValue.innerText //limit
console.log(limitNum);


// tableIndex=1 //count of table rows
// movieLensTableData.forEach(_=>{
//     var row = movieLensGrid.insertRow(tableIndex++);
//     row.insertCell(0).innerText=_.title
//     row.insertCell(1).innerText=_.genres
//     row.insertCell(2).innerText=_.year
//     row.insertCell(3).innerText=_.L_Rating

// })

function addCheckedGenre(val){
    let ind=genreSelectedArray.indexOf(val)
    if(ind>=0) genreSelectedArray.splice(ind,1)
    else genreSelectedArray.push(val)
    console.log(genreSelectedArray);

    var res= genreSelectedArray.reduce((prev,cur,ind)=>{return prev+(ind>0?" or ":"")+`genres like '%${cur}%'`},"")
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

// similarUserGenre.addEventListener('change',(event)=>{
//     // console.log(event);
//     similarUserGenreHidden.value=event.target.value;
// })

similarUserRating.addEventListener('change',(event)=>{
    similarUserRatingHidden.value=event.target.value;
})

similarUserMovieId.addEventListener('keyup',(event)=>{
    similarUserMovieIdHidden.value=event.target.value;
})

function addCheckedGenreSimilarUsers(val){
    let ind=genreSelectedArraySimilarUsers.indexOf(val)
    if(ind>=0) genreSelectedArraySimilarUsers.splice(ind,1)
    else genreSelectedArraySimilarUsers.push(val)
    console.log(genreSelectedArraySimilarUsers);

    
}

submitForm=false;
filterButton.addEventListener('click',(event)=>{
    if(!submitForm){
        event.preventDefault();
        document.getElementById('buttonFlag').value="filter"
        submitForm=true
    }
    let temp=JSON.stringify(genreSelectedArraySimilarUsers)
    similarUserGenreHidden.value="'"+temp.replaceAll(/\"/g,"''")+"'"
    filterButton.click()
})

getCountButton.addEventListener('click',(event)=>{
    if(!submitForm){
        event.preventDefault();
        document.getElementById('buttonFlag').value="getCount"
        submitForm=true;
    }
    let temp=JSON.stringify(genreSelectedArraySimilarUsers)
    similarUserGenreHidden.value="'"+temp.replaceAll(/\"/g,"''")+"'"
    getCountButton.click()
})