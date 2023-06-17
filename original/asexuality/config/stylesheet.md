---
revision_id: a959709e-4dbc-11ec-a07f-6e862d88dcae
revision_date: 1637823323
---

.side h6:nth-of-type(1) {
    position: absolute;
    display: block;
    top: 80px;
    left: 0px;
    background-color: #ffee60;
    color: black;
    text-align: center;
    right: 320px;
    left: 20px;
    border-radius: 8px;
    padding: 5px 3px;
    background-repeat: no-repeat;
    background-position: left;
    font-size: 15px;
    border: 1px solid #444;
    }
/* Allow absolute positioning to page */
.titlebox form {
    position: static
    }


/* Images -------------- */

a[href="/cake"]:after {
    background-image: url(%%cake1%%);
    background-position: 0;
    content: "";
    display: inline-block;
    height: 36px;
    width: 41px
    }

a[href="/cookie"]:after {
    background-image: url(%%acookie%%);
    background-position: 0;
    content: "";
    display: inline-block;
    height: 42px;
    width: 41px
    }


/* Old member nickname */
/*
div.titlebox span.number::after {
    content: " Aces"
    }
div.titlebox span.word {
    display: none
    }
*/

/* Old header */
/*
#header {
    background: #fcfcfc url(%%ato1%%) top left no-repeat;
    border-bottom: 1px solid #000;
    position: relative;
    z-index: 99;
    height: 80px
    }

#header-bottom-right {
    background-color: #f5f5f5;
    border: 1px solid #000;
    color: #000
    }
#header-bottom-right a {
    color: #000
    }
#header-bottom-right a:hover {
    color: #000;
    text-decoration: none
    }
#header-bottom-left {
    top: 5px;
    padding-left: 5px;
    position: relative
    }
*/
#header {
    background: #fcfcfc url(%%Asexuality-banner%%) top left no-repeat;
    border-bottom: 1px solid #000;
    position: relative;
    z-index: 99;
    height: 80px
    }
#header-bottom-right {
    background-color: #f5f5f5;
    border: 1px solid #000;
    color: #000
    }
#header-bottom-right a {
    color: #000
    }
#header-bottom-right a:hover {
    color: #000;
    text-decoration: none
    }
.pagename a {
   color: white;
   }
#header-bottom-left {
    top: 5px;
    padding-left: 5px;
    color: white;
    }

body, .side, .titlebox, #adlink, .spacer {
    background: #fcfcfc
    }
.thing .title, .thing .title.loggedin {
    color: #000;
    text-decoration: none
    }
.thing .title:hover, .thing .title.loggedin:hover {
    color: #5D0B71;
    text-decoration: none
    }
.thing .title:visited, .thing .title.loggedin:visited {
    color: #5D0B71;
    text-decoration: none
    }
.title a:visited, .title.loggedin a:visited {
    color: #000;
    text-decoration: none
    }
.expando-button.selftext.collapsed:hover, .eb-sch, .expando-button.selftext.expanded:hover, .eb-seh {
    background-image: url(%%icons43%%)
    }
a.author {
    color: #5d0b71
    }
a.author:hover {
    color: #5d0b71;
    text-decoration: none
    }
.side {
    color: #000000
    }
.side a {
    color: #5d0b71
    }
.side a:hover {
    text-decoration: none
    }
.sidebox .spacer {
    background-color: #F2F2F2;
    top: -11px;
    border: 1px solid #000;
    }

/* bullet point */
.md ul {
    list-style-type: circle
    }
.titlebox form.toggle {
    background: none
    }
.morelink {
    background: none;
    background-color: #dcdcdc;
    border: 1px solid #000
    }
.morelink:hover {
    background: none;
    background-color: #dcdcdc;
    border: 1px solid #000
    }
.morelink a:hover {
    text-decoration: none
    }
.link .usertext .md {
    border: 1px solid #000
    }
.nub {
    display: none
    }
.tagline .submitter {
    color: #1729d9;
    }
.tagline .submitter:hover {
    color: #1729d9;
    }
.linkinfo {
    background-color: #dcdcdc;
    border: 1px solid #000
    }
.expando-button.selftext.collapsed, .expando-button.selftext.expanded {
    background: url(%%expndb1%%) 0 0
    }
.expando-button.selftext.collapsed:hover, .expando-button.selftext.expanded:hover {
    background: url(%%22%%) 0 0
    }

/* -----------------------------------*/
.thing .arrow {
    height: 15px;
    width: 15px;
}

.arrow.upmod {
    background: url(%%Ace-purple%%);
    }
.arrow.downmod {
    background: url(%%AceDown-purple%%);
    }
.arrow.up {
    background: url(%%Ace-grey%%);
    }
.arrow.down {
    background: url(%%AceDown-grey%%);
    }

.fancy-toggle-button .add:hover {
    background-image: none;
    background-color: white
    }
/* -----------------------------------*/
/*NAVMENU (copied from r/firefly)*/
ul.tabmenu {
    background-image: none;
    background-color: #f2f2f2;
    border: 1px solid #000;
    position: absolute;
    font-size: 12px;
    top: 80px;
    left: 50px;
    border-radius: 9px;
    -moz-border-radius: 9px;
    -webkit-border-radius: 9px
    }
ul.tabmenu li {
    padding: 7px 0px;
    display: block;
    float: left
    }
ul.tabmenu:after {
    clear: both
    }
ul.tabmenu li a, ul.tabmenu li.selected a {
    background-color: transparent;
    border: 0;
    color: #000;
    font-weight: bold
    }
ul.tabmenu li.selected a {
    color: #5D0B71;
    font-weight: bold
    }

/*CONTENT*/
.content {
    margin: 50px 5px 0px 5px
    }
#sr-more-link {
    display: none
    }
div.content {
    margin-right: 30px;
    padding-left: 10px
    }

/* -----------------------------------*/
.thumbnail.default {
    height: 50px;
    background: url(%%cake2%%) !important;
    }
.thumbnail.self {
    height: 50px;
    background: url(%%cake2%%) !important;
    }
.thumbnail.nsfw {
    height: 67px;
    background: url(%%nsfw%%) !important;
    }
/* -----------------------------------*/
.tabmenu li.selected a {
    background-color: #efefef;
    border-color: #151415;
    color: #8350AF
    }
.tabmenu li a {
    -moz-border-radius-topleft: 8px;
    -moz-border-radius-topright: 8px;
    -webkit-border-top-left-radius: 8px;
    -webkit-border-top-right-radius: 8px
    }
.tabmenu li a {
    background-color: #EFEFEF !important;
    color: #818181
    }
.tabmenu a:hover {
    text-decoration: none
    }
.link .score.likes {
    color: #B17BDF
    }

/*----------------------------------*/
.delete-field {
    background-color: transparent
    }
.tabmenu.formtab .selected a {
    color: #5d0b71;
    font-size: 100%;
    background-color: transparent
    }
.tabmenu.formtab a {
    border: none
    }
.roundfield {
    background-color: #f2f2f2
    }
.formtabs-content {
    border-top: 4px solid #B17BDF;
    margin-top: -50px
    }


/*-------------------------------------*/

/*** Begin common styles for all flair. ***/
/* If you want to add a new flag, add its flair class to this list. Refer 
 * to "flair images" section below for naming requirements.
 */
/*
span.flair-tinycake
{
visibility: visible;
width: 15px;
height: 13px;
padding: 0;
margin: 0;
display: inline;
}
*/
/*** End common styles for all flair ***/

.flair-purple {
    background-color:#800080;
    color:#FFFFFF
}

.flair-grey {
    background-color:#A3A3A3;
    color:#FFFFFF
}

.flair-white {
    background-color:#FFFFFF;
    color:#000000
}

.flair-black {
    background-color:#000000;
    color:#FFFFFF
}

.flair-green {
    background-color:#269D39;
    color:#FFFFFF
}

.flair:before{
    content:"";
    height:16px; /* size of displayed image */
    margin-top:-2px;
    background-repeat:no-repeat;
    background-image:url(%%flags%%); /* name of the flair spritesheet uploaded */
    background-size:auto 64px; /* 64px = total height of image */
    display:inline-block;
    vertical-align:middle
}

.flair-asexual:before{width:16px;background-position: 0 -0px}
.flair-aromantic:before{width:16px;background-position: 0 -16px}
.flair-demisexual:before{width:16px;background-position: 0 -32px}
.flair-demiromantic:before{width:16px;background-position: 0 -48px}

/*** Begin flair images. ***/
/* The %%flagname%% should correspond to whatever you entered as the
 * image name in the stylesheet page. If you take the suggested filename
 * from when you upload them, it should just work. 
 * The word after span.flair- should be what you enter into the CSS class
 * box on the flair template page. So for span.flair-ainbow you would enter
 * ainbow in the flair template's CSS class. 
 */
/*
span.flair-tinycake {  background:none url(%%tinycake%%) no-repeat left top !important; }
*/

/*** End flair images ***/