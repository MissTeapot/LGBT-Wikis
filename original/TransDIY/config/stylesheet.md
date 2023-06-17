---
revision_id: b7663eb4-6c97-11e9-b47b-0e5193b22584
revision_date: 1556773448
---

.flair-green{ color:ForestGreen}
.flair-red{ color:Crimson}
.flair-yellow{ color:Gold}
.flair-purple{ color:Indigo}
.flair-black{ color:black}
.flair-pink{ color:Orchid}
.flair-cyan{ color:PaleTurquoise}
.flair-blue{ color:SteelBlue}
.flair-bot {border: none; background: ForestGreen; color: white;}
.flair-doc {border: none; background: RoyalBlue; color: white;}

/*Colorful Link Flairs*/
/*This adds a colorful little tag to posts*/
/*Flairs*/
.linkflairlabel { border: none; background: transparent; color: black;}
.linkflair-green .linkflairlabel {border: none; background: ForestGreen; color: white;}
.linkflair-red .linkflairlabel {border: none; background: Crimson; color: white;}
.linkflair-blue .linkflairlabel {border: none; background: DodgerBlue; color: white;}
.linkflair-navy .linkflairlabel {border: none; background: navy; color: white;}
.linkflair-violet .linkflairlabel {border: none; background: DarkViolet; color: white;}
.linkflair-orange .linkflairlabel {border: none; background: orangered; color: white;}
.linkflair-brown .linkflairlabel {border: none; background: Sienna; color: white;}
.linkflair-yellow .linkflairlabel {border: none; background: Goldenrod; color: white;}
.linkflair-purple .linkflairlabel {border: none; background: indigo; color: white;}
.linkflair-cyan .linkflairlabel {border: none; background: PaleTurquoise; color: black;}
.linkflair-pink .linkflairlabel {border: none; background: Orchid; color: white;}
.linkflair-coral .linkflairlabel {border: none; background: coral; color: white;}

  /*Changes the name of your subscribers/users here now*/
  .titlebox .word { display: none }
  .titlebox .number:after { content: " TransDIYers"; }
  .titlebox .users-online span.number:after { content: " people DIYing now"; }

.flair-rainbow1 {
    background-image: -webkit-linear-gradient(left, red 0%, red 14%, orange 14%, orange 28%, yellow 28%, yellow 43%, green 43%, green 57%, blue 57%, blue 72%, indigo 72%, indigo 86%, violet 86%, violet 100%);
    background-image: -moz-linear-gradient(left, red 0%, red 14%, orange 14%, orange 28%, yellow 28%, yellow 43%, green 43%, green 57%, blue 57%, blue 72%, indigo 72%, indigo 86%, violet 86%, violet 100%);
    background-image: -ms-linear-gradient(left, red 0%, red 14%, orange 14%, orange 28%, yellow 28%, yellow 43%, green 43%, green 57%, blue 57%, blue 72%, indigo 72%, indigo 86%, violet 86%, violet 100%);
    background-image: -o-linear-gradient(left, red 0%, red 14%, orange 14%, orange 28%, yellow 28%, yellow 43%, green 43%, green 57%, blue 57%, blue 72%, indigo 72%, indigo 86%, violet 86%, violet 100%);
    background-image: linear-gradient(to right, red 0%, red 14%, orange 14%, orange 28%, yellow 28%, yellow 43%, green 43%, green 57%, blue 57%, blue 72%, indigo 72%, indigo 86%, violet 86%, violet 100%);
    color: White;
    text-shadow: -1px -1px 0 Indigo, 1px -1px 0 Indigo, -1px 1px 0 Indigo, 1px 1px 0 Indigo;
    
}

@keyframes rainbow {0% {color:red;}14% {color:orange;}28% {color:goldenrod;}42% {color:green;}56% {color:DodgerBlue;}70% {color:BlueViolet;}84% {color:indigo;}}
@-moz-keyframes rainbow {0% {color:red;}14% {color:orange;}28% {color:goldenrod;}42% {color:green;}56% {color:DodgerBlue;}70% {color:BlueViolet;}84% {color:indigo;}}
@-webkit-keyframes rainbow {0% {color:red;}14% {color:orange;}28% {color:goldenrod;}42% {color:green;}56% {color:DodgerBlue;}70% {color:BlueViolet;}84% {color:indigo;}}

.flair-rainbow2{color:red; -webkit-animation:rainbow 5s linear infinite; -moz-animation:rainbow 5s linear infinite; animation:rainbow 5s linear infinite;}