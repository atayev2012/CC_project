let rating;

function selectRating(starNumber){
    rating = starNumber;
    for (let i=1; i < starNumber + 1; i++) {
        let star = document.getElementById(i);
        star.style.color = "#f5b041";
    }

    for (let i=starNumber+1; i < 6; i++) {
        let star = document.getElementById(i);
        star.style.color = "#797d7f";
    }
}

function startOnLoad(){
    rating = 0;
    const stars = document.querySelector(".star");
    stars.addEventListener("onclick", selectRating(this.id));
}


