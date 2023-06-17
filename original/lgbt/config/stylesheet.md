---
revision_id: 8eca0054-d5a6-11ed-a36d-76588ee92bb3
revision_date: 1680914685
---

.arrow.down:hover:before {
position: absolute;
display: block;
z-index: 1000;
width: 200px;
padding: 6px 0;
background-color:#66FFCC;
color: #fff;
text-align: center;
font-size: 11px;
font-weight: bold;
margin-left: 20px;
-webkit-border-radius: 3px;
   -moz-border-radius: 3px;
-webkit-box-shadow: 2px 2px 3px rgba(0,0,0,0.2);
   -moz-box-shadow: 2px 2px 3px rgba(0,0,0,0.2);
box-shadow: 2px 2px 3px rgba(0,0,0,0.2);
content: "Vote based on quality, not opinion."; }
/* Toolbox */

.listing-page .link .add-domain-tag,
.listing-page .link .global-mod-button,
.listing-page .link a#add-user-tag,
.listing-page .link a.user-history-button{
    opacity: 0;
    transition: opacity 0.15s ease-in-out;
}

.link:hover .add-domain-tag,
.link:hover .global-mod-button,
.link:hover a#add-user-tag,
.link:hover a.user-history-button{
    opacity:100;
}

.listing-page .link.stickied .add-domain-tag,
.listing-page .link.stickied .global-mod-button,
.listing-page .link.stickied a#add-user-tag,
.listing-page .link.stickied a.user-history-button{
    opacity: 100!important;
}


.comment .add-domain-tag,
.comment .global-mod-button,
.comment a#add-user-tag,
.comment .nuke-button,
.comment a.user-history-button{
    opacity: 0;
    display: none !important;
    transition: opacity 0.15s ease-in-out;
}

.comment:hover .add-domain-tag,
.comment:hover .global-mod-button,
.comment:hover a#add-user-tag,
.comment:hover .nuke-button,
.comment:hover a.user-history-button{
    opacity:100;
    display: inline !important;
}

#tb-metrics-expand-list {
    position: absolute!important;
}

.drop-choices.lightdrop.sortorder-options.inuse a.choice{
    color: white;
}

.add-domain-tag:after{
    content: "ag Domain";
}

.add-domain-tag:hover {
    text-decoration: none!important;
    background-color: #a6a6a6!important;
    color: white!important;
    border-color: #a6a6a6!important;
}

.add-user-tag:after{
    content: "ag Domain";
}

.add-user-tag:hover {
    text-decoration: none!important;
    background-color: #a6a6a6!important;
    color: white!important;
    border-color: #a6a6a6!important;
}

.global-mod-button:after{
    content: "od Action"
}

.global-mod-button:hover {
    text-decoration: none!important;
    background-color: #00cc66!important;
    color: white!important;
    border-color: #00cc66!important;
} 
.nuke-button:hover {
    text-decoration: none!important;
    background-color: yellow!important;
    color: white!important;
    border-color: black!important;
} 
.nuke-button:after {
    content: "emove chain"!important;
}
.add-user-tag-lgbt:before {
    content: "User "!important;
}
.add-user-tag-lgbt:after {
    content: "otes"!important;
}

a#add-user-tag:hover {
    text-decoration: none!important;
    background-color: #9999ff!important;
    color: white!important;
    border-color: #9999ff!important;
}

b.usernote-span-lgbt {
    position: absolute!important;
    top: 5px!important;
}
    
a.user-history-button:after {
    content: "istory"   
}

a.user-history-button:before {
    content: "User "
}

a.user-history-button:hover {
    text-decoration: none!important;
    background-color: #ff4d4d!important;
    color: white!important;
    border-color: #ff4d4d!important;
}

a#add-user-tag a[title*=""]:before {
    font-size: 0px!important;
}
/* Make the flair selector more noticeable in sidebar */
div.side .flairselectbtn:after {
    content: " - please click here to assign yourself flair";
    color:#FF3300;
    font-weight: bold
    
    }




.arrow {
  -webkit-animation: arrowWobble 1s;
}

.arrow.up:hover {
  -webkit-animation: arrowSpin 1s;
}

@-webkit-keyframes arrowWobble {
  0%   { -webkit-transform: rotate(0deg); }
  33%  { -webkit-transform: rotate(20deg); }
  66%  { -webkit-transform: rotate(-20deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@-moz-keyframes arrowWobble {
  0%   { -moz-transform: rotate(0deg); }
  33%  { -moz-transform: rotate(20deg); }
  66%  { -moz-transform: rotate(-20deg); }
  100% { -moz-transform: rotate(360deg); }
}

@keyframes arrowWobble {
  0%   { transform: rotate(0deg); }
  33%  { transform: rotate(20deg); }
  66%  { transform: rotate(-20deg); }
  100% { transform: rotate(360deg); }
}

@-webkit-keyframes arrowSpin {
  from { -webkit-transform: rotate(0deg); }
  to   { -webkit-transform: rotate(720deg); }
}

@-moz-keyframes arrowSpin {
  from { -moz-transform: rotate(0deg); }
  to   { -moz-transform: rotate(720deg); }
}

@keyframes arrowSpin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(720deg); }
}
#header-img { margin: 0px 0px -5px;
    max-width: 100%;
    height: auto;
}
#header .pagename a {
    text-transform: uppercase;
}

a[href$="AntiPOZi/"]
{
    display: none;
}

/*==Sticky, thanks yt==*/
.titlebox .usertext-body .md ol {
font-family: "Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif !important;
color: #555 !important;
width: auto !important;
background: #F6F6F6 !important;
border-left: 8px solid #AAA !important;
position: absolute !important;
top: 118px !important;
left: 11px !important;
z-index: 50 !important;
margin: 0 !important;
padding: 3px 6px 5px 5px !important;
list-style: none !important;
display: block !important;
white-space: nowrap !important;
overflow: hidden !important;
animation: none !important;
}

body.res-nightmode .titlebox .usertext-body .md ol {
background: #222;
border: 1px solid #AAA;
border-left: 8px solid #AAA;
}

.content {margin-top: 42px!important;}  

/*Dropdown menu CSS; thanks, Circlebroke!*/

/* Related subreddits */
.titlebox .md ul {
    margin:0;
}
body.res-nightmode .titlebox .md ul, body.res-nightmode .md ol { background-color: #222; }

.titlebox ul li {
    width:274px;
    background-color: #f2f2f2;
    border:none;
    
    color: black;
    display:none;
    padding:7px 7px 9px 13px;
    margin: 0 0 -1px -3px;
    text-align: left;
    border-top: 1px solid #CCCCCC;
    }
.titlebox ul li:hover {
    background-color:#DDDDDD;
}
body.res-nightmode .titlebox ul li {
    background-color: #333333;
    color: #DDDDDD;
    border-top: none;
    }

.titlebox ul li:hover {
    background-color:#DDDDDD;
}
body.res-nightmode .titlebox ul li:hover {
    background-color:#555555;
}
.titlebox ul li:nth-child(1) {
    display:block;
    font-family: "Helvetica Neue",Helvetica,Arial,"Lucida Grande",sans-serif;
    font-weight: 300;
    background-color: #333333;
    display: inline-block;
    font-size: 1.4em;
    border-top:none;
    font-size:15px;
    }
.titlebox ul li:nth-child(1):hover {
    background-color:#F2F2F2;
    color:#555555;
}
body.res-nightmode .titlebox ul li:nth-child(1):hover {
    color:#DDDDDD;
}

/* Fix for Edurne; would otherwise not highlight every other link */
.titlebox ul li:nth-child(odd):hover {
    background-color:#DDDDDD;
    color:#555555;
}
body.res-nightmode .titlebox ul li:nth-child(odd):hover {
    background-color:#555555;
}

.titlebox ul:hover &gt; li {
    display:block;
}

.side .titlebox hr {
border:none;
margin-bottom:10px;
}

/* ==Edurne Reddit CSS Theme v5.2 - (http://www.reddit.com/r/edurne/)== */

/* GENERAL */
body { position:relative; font-family:arial, helvetica, sans-serif; }
body &gt; .content { overflow:hidden; }
.md p { font-family:Verdana, arial, sans-serif; padding:1px 0; }

.link .usertext .md,.usertext table.markhelp,.btn .login-form-side,.infobar,#search,#search input[type=text],
.link,#header-bottom-right #userbarToggle,.linkinfo,textarea,.rounded,.sidecontentbox .content {
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

/* HEADER */
#sr-header-area {
    background-color:#c6daed;
    text-transform:lowercase;
    border-bottom:3px solid #c2d6e9;
    font-size:100%;
    font-family:Verdana, arial, sans-serif;
}



#header-bottom-right {
    right:20px;
    background-color:#deeaf6;
    -moz-border-radius:0;
    -webkit-border-radius:0;
    -o-border-radius:0;
    -ms-border-radius:0;
    -khtml-border-radius:0;
    border-radius:0;
}
body.res-nightmode #header-bottom-right { background-color: #DEEAF6 !important; }
#header-bottom-right.res-navTop { top: 21px !important; }

#header-bottom-right.res-navTop #userbarToggle {
    -moz-border-radius-topleft: 0;
    -webkit-border-top-left-radius: 0;
    border-top-left-radius: 0;
}
#header-bottom-right #userbarToggle {
    font-family:"Courier New", Courier, monospace;
    font-size:12px;
}
#header-bottom-right #userbarToggle {
    font-family:"Courier New", Courier, monospace;
    font-size:12px;
    width:14px;
    padding-right:4px;
    -moz-border-radius-bottomleft:0;
    -moz-border-radius-bottomright:0;
    border-bottom-left-radius:0;
    border-bottom-right-radius:0;
    -webkit-border-bottom-left-radius:0;
    -webkit-border-bottom-right-radius:0;
}

/* SIDEBAR */

/* search */
.side #search {
    border:1px solid #eaeaea;
    padding:10px;
    margin-top:20px;
    background-color:#FAFAFA;
}
body.res-nightmode #search {
    background-color: #AAA;
    border-color: #BBB;
}
#search input[type=text] {
    width:265px;
    border:1px solid #DBDADA;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
    font-size:14px;
    font-style:italic;
    padding:4px;
}

/* side */
.side { margin: 0 20px; }
.side .md { overflow:hidden; }
.titlebox { padding:0 10px; }
.titlebox .bottom { display:none; }
.side .titlebox &gt; h1 { font-size:24px; }
.linkinfo { padding:15px; border:none; background-color:#CEE3F8; }
body.res-nightmode .side .redditname a { color: #DDD !important; }
.sidebox.submit .spacer, .sidebox.create { display:none; }
.linkinfo .score .word,.linkinfo .score .number { font-size:15px; }
.sidecontentbox .content { border:1px solid #EAEAEA; background-color:#FAFAFA; padding:10px; }
.icon-menu li { margin:0 0 5px; }
.side h1, .side h2, .side h3 {color: #222;}
.side h1 {font-size: 19px;}
.side h2 {font-size: 16px;}
.side h3 {font-size: 14px;}

body.res-nightmode .login-form-side {
    background-color: #111 !important;
    color: #DDD !important;
    border: 1px solid #DDD !important;
}

body.res-nightmode .login-form-side #remember-me label { color: #DDD !important; }
body.res-nightmode .login-form-side #remember-me input { width: auto !important; margin-left: 6px; }
body.res-nightmode .side .login-form-side .submit { padding: 4px; background-color: transparent; }
body.res-nightmode .side .login-form-side .submit .btn { margin: auto; }

/* submit */

body.res-nightmode .sidebox { padding-left: 0 !important; }
body.res-nightmode .sidebox.submit { background-image: none !important; }

body.res-nightmode .sidebox.submit .nub {
    background: #222;
    border-left: 24px solid #393939;
}
body.res-nightmode .sidebox, body.res-nightmode .subredditbox, body.res-nightmode .subreddit-info, body.res-nightmode .raisedbox, body.res-nightmode .login-form-side {
    border: 0 !important;
    border-radius: 0 !important;
    -moz-border-radius: 0 !important;
    -webkit-border-radius: 0 !important;
}
body.res-nightmode .sidebox.submit .morelink a { color: #DDD !important; }
body.res-nightmode .sidebox.submit:hover { background-color: #444 !important; }
body.res-nightmode .sidebox.submit:hover .nub { border-left-color: #444; }
.side #search { margin-top:61px; }

.morelink,.morelink:hover,.side a[href*='/#btn'] {
    font-weight:normal;
    letter-spacing:0;
    background:#449EF8;
    border: none;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
    height: 30px;
    line-height: 30px;
    overflow: hidden;
}

.morelink a,.morelink a:hover { color:#FFF; font-family:Verdana, Arial, sans-serif; font-size:16px; }
.morelink .nub,.morelink:hover .nub {
    top: 0;
    right: -25px;
    height: 0;
    width: 0;
    background: white;
    border: 24px solid #449EF8;
    border-top-width: 15px;
    border-top-color: transparent;
    border-bottom-width: 15px;
    border-bottom-color: transparent;
    border-right-color: transparent;
}

.morelink:hover .nub { border-left-color: #56A6F7 }
.disabled .morelink a,.disabled .morelink a:hover { cursor:default; color:#AAA; }
.morelink:hover { background-color:#56a6f7; border-color:#56a6f7; }
.disabled .morelink,.disabled .morelink:hover { background:#f5f5f5; border-color:#f5f5f5; }
.disabled .morelink .nub,.disabled .morelink:hover .nub { background:url(%%sprites-05%%) 0 0 no-repeat transparent; }

/* CONTENT */

/* main content */
.sitetable { font-family:verdana, arial, helvetica, sans-serif; clear:left;}
.infobar { overflow:hidden; margin:0 0 10px; }
.content { margin:20px 0 0 20px; }
.entry { padding: 2px; }

.link {
    overflow:hidden;
    margin:0px;
    padding:5px;
    border:1px solid #EAEAEA;
    background-color:#FAFAFA;
}
body.res-nightmode .sitetable .thing.link, body.res-nightmode div#siteTable div[onclick="click_thing(this)"] {
    border: 1px solid #4c4c4c !important;
    background-color: #333 !important;
}
body.res-nightmode .sitetable .thing.link .keyHighlight {
    background-color: #363636 !important;
    border-color: #666 !important;
    outline-color: #666 !important;
}
body.res-nightmode .midcol {
    background-color: #222 !important;
    padding: 4px;
}

.link .rank { display:none; }
.link.last-clicked { border:1px dashed #EAEAEA; }
body.res-nightmode .link.last-clicked { border-color: #666; }
.linklisting &gt; .clearleft { margin:5px; }
.entry .buttons li { display:inline; float:left; }
.link .midcol { margin-right:10px; margin-left:0; }

/* main comments */
.commentarea { margin-top:10px; }
.link.self .usertext-body .md p,.comment .usertext-body .md p { line-height:17px; }
.link .usertext .md { padding:5px 10px; }
.panestack-title { border:none; margin:0; padding:0; }
.panestack-title .title { float:left; font-size:11px; color:#888; margin:0; }
.commentarea .menuarea { font-size:11px; margin:0; }
.panestack-title:after { content:'-'; padding:0 5px; float:left; }
.commentarea &gt; .usertext { clear:left; margin:0; }
.usertext-edit { width:auto; }
.usertext-edit textarea { width:430px; padding:10px; }
.usertext .bottom-area { width:450px; }
.usertext button { margin:5px 5px 10px 0; border:none; min-width:70px; }
body.res-nightmode .usertext .help-toggle { background-color:#DDD; }
.usertext .help-toggle a { color:#FFF; }
body.res-nightmode .usertext .help-toggle a { color:#444 !important; }
.usertext table.markhelp { width:450px; font-size:11px; }
.link .usertext .md { background-color:#FFF; border:1px solid #EAEAEA; }
.entry .buttons li a { font-family:verdana, arial, sans-serif; }

.usertext .help-toggle {
    background-color:#999;
    border:none;
    color:#FFF;
    padding:6px;
    margin:5px 0;
    font-size:13px;
}

/* MODERATOR SPECIFIC */

/* stylesheet tweaks */
.stylesheet-customize-container { width: 100%; }
#subreddit_stylesheet { display: block; overflow: hidden; padding-right: 80px; }
.sheets { margin: 0; }

#stylesheet_contents {
    font-family: Consolas, Monaco, monospace;
    padding: 12px;
    background-color: #222;
    color: #ace;
    border: 8px solid #222;
}
body.res-nightmode #stylesheet_contents {
    background-color: #111;
    border-color: #111;
}


/* MISC STYLING */

/* tables */
.md table { border: 1px solid #ccc; font-family: Arial, Helvetica, Sans-serif; margin: 10px 0px; }
body.res-nightmode .md table { border-color: #666; }
.side .md table { width:100%; }
.md table * { border: 0; }
body.res-nightmode .md table * { color: #ddd; }
.md table th { text-align: center; }
.md table tr:nth-child(even), .md table thead { background-color: #f6f6f6; }
body.res-nightmode .md table tr:nth-child(even), body.res-nightmode .md table thead { background-color: #444; }
.md table td, .md table th { border-right: 1px solid #ccc; padding: 4px 8px; }
body.res-nightmode .md table td, body.res-nightmode .md table th { border-color: #666; }
body:not(.res-nightmode) .md table tbody { color: #444; }

/* lists */
.md &gt; ul, .md &gt; ol { border-left: 4px solid #ccc; }
body.res-nightmode .md &gt; ul, body.res-nightmode .md &gt; ol { border-color: #666; }

.md ul, .md ol {
    margin: 10px 0px;
    padding: 6px;
    background-color: #fff;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

body.res-nightmode .md ul, body.res-nightmode .md ol { background-color: #444; }
.md ul { list-style: disc inside; }
.md ol { list-style: none; }

.md ul li, .md ol li {
    padding: 4px 8px;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

.md ul li ul, .md ol li ol { margin: 8px 4px; }
.md ul li:nth-child(odd), .md ol li:nth-child(odd) { background-color: #f6f6f6; }
body.res-nightmode .md ul li:nth-child(odd), body.res-nightmode .md ol li:nth-child(odd) { background-color: #222; }
.md ol { counter-reset: inc 0; }

.md ol li:before {
    counter-increment: inc 1;
    content: counter(inc, decimal) '. ';
    margin-right: 4px;
    color: #999;
}

/* boxes */
.side blockquote + hr {
    border-width:0;
    width:0;
    background-color:transparent;
    margin:20px 0 0;
}
body.res-nightmode .side hr {
    border: 0 !important;
    border-bottom: 1px solid #000 !important;
}
.side blockquote {
    border:0 none;
    padding:15px;
    margin:0;
    border:1px solid #CCC;
    background-color:#F5F5F5;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

.side h4, .side h5, .side h6 { height:0; }
.side blockquote h1 ~ p { margin-left:21px; }
.side blockquote h1 { background-color: transparent !important; margin-bottom: 15px; }
.side blockquote pre, .side blockquote code { color: #222 !important; }
.side h6 + blockquote p, .side h5 + blockquote p, .side h4 + blockquote p { color: #000; }
.side h6 + blockquote a, .side h5 + blockquote a, .side h4 + blockquote a { color: #369; }
.side .spacer .md h1, .side .spacer .md h2, .side .spacer .md h3 { background: transparent !important; }
.side blockquote + p,.side p + blockquote,.side p + h4,.side p + h5,.side p + h6 { margin-top:15px; }
body.res-nightmode .side blockquote h1, body.res-nightmode .side blockquote h1 a { color: #EEE !important; }
body.res-nightmode .side h4+blockquote,body.res-nightmode .side h5+blockquote,body.res-nightmode .side h6+blockquote { background-color: #111; }

/* colors */
.md h4 + table { border-color: #9EF886; }
.md h4 + table td, .md h4 + table th { border-right-color: #9EF886; }
.md h4 + table tr:nth-child(even), .md h4 + table thead { background-color: #E9FFE6; }
.md h5 + table { border-color: #F4F225; }
.md h5 + table td, .md h5 + table th { border-right-color: #F4F225; }
.md h5 + table tr:nth-child(even), .md h5 + table thead { background-color: #FFFFE6; }
.md h6 + table { border-color: #FF9185; }
.md h6 + table td, .md h6 + table th { border-right-color: #FF9185; }
.md h6 + table tr:nth-child(even), .md h6 + table thead { background-color: #FEF0F0; }

.md h4 + ul, .md h4 + ol { border-left-color: #9EF886; }
.md h4 + ul li:nth-child(odd), .md h4 + ol li:nth-child(odd) { background-color: #E9FFE6; }
.md h5 + ul, .md h5 + ol { border-left-color: #F4F225; }
.md h5 + ul li:nth-child(odd), .md h5 + ol li:nth-child(odd) { background-color: #FFFFE6; }
.md h6 + ul, .md h6 + ol { border-left-color: #FF9185; }
.md h6 + ul li:nth-child(odd), .md h6 + ol li:nth-child(odd) { background-color: #FEF0F0; }

.side h6 + blockquote { display:block; background-color:#FEF0F0; border:1px solid #FF9185; }
.side h5 + blockquote { display:block; background-color:#FFFFE6; border:1px solid #F4F225; }
.side h4 + blockquote { display:block; background-color:#E9FFE6; border:1px solid #9EF886; }

body.res-nightmode .md h4 + table { border-color: #9EF886; }
body.res-nightmode .md h4 + table td, body.res-nightmode .md h4 + table th { border-right-color: #9EF886; }
body.res-nightmode .md h4 + table tr:nth-child(even), body.res-nightmode .md h4 + table thead { background-color: #207807; }
body.res-nightmode .md h5 + table { border-color: #F4F225; }
body.res-nightmode .md h5 + table td, body.res-nightmode .md h5 + table th { border-right-color: #F4F225; }
body.res-nightmode .md h5 + table tr:nth-child(even), body.res-nightmode .md h5 + table thead { background-color: #626105; }
body.res-nightmode .md h6 + table { border-color: #FF9185; }
body.res-nightmode .md h6 + table td, body.res-nightmode .md h6 + table th { border-right-color: #FF9185; }
body.res-nightmode .md h6 + table tr:nth-child(even), body.res-nightmode .md h6 + table thead { background-color: #670808; }

body.res-nightmode .md h4 + ul, body.res-nightmode .md h4 + ol { border-left-color: #9EF886; }
body.res-nightmode .md h4 + ul li:nth-child(odd), body.res-nightmode .md h4 + ol li:nth-child(odd) { background-color: #207807; }
body.res-nightmode .md h5 + ul, body.res-nightmode .md h5 + ol { border-left-color: #F4F225; }
body.res-nightmode .md h5 + ul li:nth-child(odd), body.res-nightmode .md h5 + ol li:nth-child(odd) { background-color: #626105; }
body.res-nightmode .md h6 + ul, body.res-nightmode .md h6 + ol { border-left-color: #FF9185; }
body.res-nightmode .md h6 + ul li:nth-child(odd), body.res-nightmode .md h6 + ol li:nth-child(odd) { background-color: #670808; }

/* buttons */
.btn, button, .side a[href*='/#btn'] {
    background-color:#449EF8;
    border:none;
    color:#FFF;
    padding:6px;
    margin:5px 5px 5px 0;
    cursor:pointer;
    font-size:13px;
    font-family:arial,helvetica,sans-serif;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}
.side a[href*='/#btn'] {
    text-align: center;
    display: block;
    width: auto;
    font-weight: normal;
    letter-spacing: 0;
    line-height: 29px;
    margin:10px 0px;
}

body.res-nightmode .btn, body.res-nightmode button, 
body.res-nightmode .side a[href*='/#btn'] { color: #444 !important; background-color: #CCC !important; }
.btn a { color:#FFF; }
body.res-nightmode .btn a { color: #444 !important; }
.btn:hover,button:hover,.side a[href*='/#btn']:hover { background-color:#56a6f7; border-color:#56a6f7; }
body.res-nightmode .btn:hover, body.res-nightmode button:hover, 
body.res-nightmode .side a[href*='/#btn']:hover { background-color:#DDD !important; border-color:#DDD; }

/* code styling */
.usertext-body pre {
    margin:10px 0;
    padding:10px;
    color: #222 !important;
}
.usertext-body pre, .usertext-body p &gt; code {
    background:#f7f7f7;
    border:1px solid #ccc;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
    font-size:11px;
    color: #222 !important;
    overflow: auto;
}
.usertext-body code {
    color: #222 !important;
    font-family:Consolas, Monaco, monospace;
    line-height:1.5em;
}
.usertext-body p &gt; code {
    padding:0 3px;
    color: #222 !important;
}

/* mobile-friendly spoiler tags (credit /u/listen2) */
a[href='#s'] {
    font-size:0;
    visibility:hidden;
    cursor:default;
    display:inline-block;
}
a[href='#s']::after {
    content:attr(title);
    background:#cee3f8;
    color:#cee3f8;
    font-size:small;
    visibility:visible;
}
body.res-nightmode a[href='#s']::after {
    content:attr(title);
    background:#666;
    color:#666;
    font-size:small;
    visibility:visible;
}
a[href='#s']:hover::after,a[href='#s']:active::after {
    color:#000;
    background:transparent;
    text-decoration:none;
    font-size:small;
}
body.res-nightmode a[href='#s']:hover::after, body.res-nightmode a[href='#s']:active::after {
    color:#DDD;
    background:transparent;
    text-decoration:none;
    font-size:small;
}

/* sidebar icons */
.side a[href*='#icon-'] { color:#000 !important; cursor:default; }
.side a[href*='#icon-']:hover { text-decoration:none; }
.side a[href*='#icon-']::before {
    display:inline-block;
    height:16px; width:16px;
    content:'';
    margin:0 5px -1px 0;
    background: url(%%sprites-05%%) 30px 30px no-repeat;
}

.side a[href='#icon-exclamation']::before   {background-position: -16px -32px;}
.side a[href='#icon-information']::before   {background-position: -54px -51px;}
.side a[href='#icon-lightbulb']::before     {background-position: -16px -51px;}
.side a[href='#icon-comments']::before      {background-position: -35px -89px;}
.side a[href='#icon-unhappy']::before       {background-position: -73px -89px;}
.side a[href='#icon-check']::before         {background-position: -73px -51px;}
.side a[href='#icon-clock']::before         {background-position: -35px -51px;}
.side a[href='#icon-cross']::before         {background-position: -35px -70px;}
.side a[href='#icon-smile']::before         {background-position: -54px -89px;}
.side a[href='#icon-error']::before         {background-position: -54px -32px;}
.side a[href='#icon-note']::before          {background-position: -54px -70px;}
.side a[href='#icon-star']::before          {background-position: -73px -32px;}
.side a[href='#icon-help']::before          {background-position: -16px -70px;}
.side a[href='#icon-time']::before          {background-position: -73px -70px;}
.side a[href='#icon-bell']::before          {background-position: -35px -32px;}
.side a[href='#icon-eye']::before           {background-position: -16px -89px;}

/* SUBREDDIT-SPECIFIC STYLES - add you own styles below without modifying the code above.*/


/* sidebar image */
    .side {
    background: url(%%safespace%%) no-repeat;
    background-color: #FFFFFF;
    margin-top: 5px;
    padding-top: 100px;
} 

.listing .listing .listing .listing .listing .listing .listing { border-left: 1px dotted #ddddff; }
.listing .listing .listing .listing .listing .listing { border-left: 1px dotted #710071; } 
.listing .listing .listing .listing .listing { border-left: 1px dotted #000093; }
.listing .listing .listing .listing { border-left: 1px dotted #008241; }
.listing .listing .listing { border-left: 1px dotted #cfcf00; }
.listing .listing { border-left: 1px dotted #e67300; }
.listing { border-left: 1px dotted #d91226; }

div.titlebox span.number:after {
    content: " fabulous"
    }

.author[href$="/moonflower"]:after{
color: red;
content: " troll"
}

.author[href$="/onetimer"]:after{
color: red;
content: " Unconcerned Troll"
}

.titlebox h1 {
  margin: 8px 0 0;
}

.redditname h1 a {
  color: black;
}

.titlebox h1 a {
  color: #369;
}

.titlebox .usertext-body .md h2 {
    display: block;
    position: absolute;
    top: 120px;
    left: 815px;
    margin-top: .5em;
    padding-top: .2em;
    padding-bottom: .2em;
    padding-left: .7em;
    padding-right: .7em;
    margin-bottom: 1em;
    font-size: 1.2em;
    font-weight: normal;
    color: #000000;
    border-width: 1px;
    border-style: solid;
    border-color: #000000;
    border-radius: 3px;
    background-color: #eeffff;
    }


/* hover text for the report button */
.report-button .option:not(.error):hover:before {
    color: black;
    background-color: #CCF;
    border: 1px solid #333;
    border-radius: 4px;
    content: "Please message the moderators if you click report, otherwise we won't know why it was reported.";
    display: block;
    font-size: 11px;
    font-weight: bold;
    margin-left: 75px;
    margin-top: 7px;
    padding: 5px;
    position: absolute;
    text-align: center;
    z-index: 1000
    }

/* rainbow arrows  with RES-nightmode version now*/
.res-nightmode .arrow.upmod
{
background: url(%%darkup%%) 0 0 no-repeat !important;
}
.arrow.upmod { 
 background: url(%%up%%) 0 0 no-repeat !important;
}

.res-nightmode .arrow.downmod
{
background: url(%%darkdown%%) 0 0 no-repeat !important;
}
.arrow.downmod { 
 background: url(%%down%%) 0 0 no-repeat !important;
}

a[href*="/meta"].title:link, a[href*="/meta_"].title:link, a[href*="/meta"].title:visited, a[href*="/meta_"].title:visited { color: #282 !important; }

a[href*="/chat"].title:link, a[href*="/chat_"].title:link, a[href*="/chat"].title:visited, a[href*="/chat_"].title:visited { color: #0088FF !important; }

a[href*="/hot_topic"].title:link, a[href*="/hot_topic_"].title:link, a[href*="/hot_topic"].title:visited, a[href*="/hot_topic_"].title:visited { color: #FF0036 !important; }


/* Trigger Warnings */

/*== Spoiler Tags From GameOfThrones, ty to nekosune ==*/

a[href="/rc"]:before {
    content: "[Removed Content:]";
    color: #003F87 !important;
    background: #87CEFA !important
    }
a[href="/s"], a[href="/b"], a[href="/rc"], a[href="/tw"] {
    padding: 0 2px;
    color: #FFF !important;
    cursor: text;
    border-radius: 3px;
    -moz-border-radius: 3px;
    -webkit-border-radius: 3px;
    }
a[href="/s"]:hover, a[href="/b"]:hover, a[href="/rc"]:hover, a[href="/tw"]:hover {
    color: #FF0 !important
    }
a[href="/s"]::after, a[href="/b"]::after, a[href="/rc"]::after, a[href="/tw"]::after {
    content: attr(title);
    padding: 0px 8px
    }
a[href="/s"]:hover::after, a[href="/s"]:active::after, a[href="/b"]:hover::after, a[href="/b"]:active::after, a[href="/rc"]:hover::after, a[href="/rc"]:active::after, a[href="/tw"]:active::after, a[href="/tw"]:hover::after {
    color: #FFF
    }
a[href="/tw"]:before {    content: "[TW]";    color: black !important;    background: salmon !important    }
a[href="/s"] {
    background: #000
    }
a[href="/s"]::after {
    background: #000;
    color: #000
    }
a[href="/b"] {
    background: #800
    }
a[href="/b"]::after {
    background: #800;
    color: #800
    }
a[href="/rc"] {
    background: #003F87
    }
a[href="/rc"]::after {
    color: #003F87 ;
    background: #003F87
    }
a[href="/tw"] {
    background: #000
    }
a[href="/tw"]::after {
    background: #000;
    color: #000
    }

/*== legacy trigger warnings ==*/

.content a[href="/trigger"] {
    color: black !important;
    background: black !important
    }
a[href="/trigger"]:hover {
    color: white !important;
    background: black
    }
a[href="/trigger"]:before {
    content: "[TW]";
    color: black !important;
    background: salmon !important
    }
.content a[href="/removed"] {
    color: #003F87 !important;
    background: #003F87 !important
    }
a[href="/removed"]:hover {
    color: white !important;
    background: #003F87
    }
a[href="/removed"]:before {
    content: "[Removed Content:]";
    color: #003F87 !important;
    background: #87CEFA !important
    }



/* stolen from askscience yet again by robotanna I WANT THIS TO BE PRETTY */
.commentarea {
    position: static
    }
.commentarea .usertext .usertext-edit:after {
    content: "Please review the sidebar and FAQ before posting! This subreddit is heavily moderated. Posts that are disrespectful to GSRM (Gender, Sexual and Romantic Minority) people of any type are subject to removal, and may lead to removal of your posting privileges.";
    display: block;
    text-align: left;
    margin-top: -5px;
    margin-bottom: 5px;
    padding: 10px;
    background-color: #eff7ff;
    border: 2px solid #FF8322;
    font-size: 12px;
    width: 430px;
    }
body.res-nightmode .commentarea .usertext .usertext-edit:after {
    color: black;
}

/* Thread-specific banners - for invasions etc. stolen by anna from r/anarchy*/
/* HOW-TO: Add "#siteTable:first-child .id-t3_&lt;UNIQUE IDENTIFIER&gt;:before," above the appropriate content tag. */
#siteTable:first-child .id-t3_16mhzf:before, #siteTable:first-child .id-t3_16mhzf:before, #siteTable:first-child .id-t3_16mhzf:before, #siteTable:first-child .id-t3_16mhzf:before, #siteTable:first-child .id-t3_16mhzf:before, #siteTable:first-child .id-t3_16mhzf:before {
    content: "Welcome visitors from /r/all! Please review the rules of this subreddit before posting. This is a safe space and content deemed inappropriate, offensive or in violation of the rules will be removed. Thank you!";
    background-color: #eff7ff;
    border: 1px solid #FF8322;
    border-radius: 3px;
    margin: 5px 305px 5px 0px;
    padding: 5px 10px;
    display: block;
    font-size: 18px;
    text-align: left
    }

/* Next 4 sections make deleted messages less noticeable -stolen from askscience by GD*/
form.grayed, form.grayed ~ ul.flat-list.buttons {
    display: none
    }
p.tagline &gt; a.expand:first-child + em:after, div.collapsed &gt; a.expand:first-child + em:after {
    visibility: visible;
    font-size: x-small;
    font-weight: bold;
    content: "[deleted]"
    }
p.tagline &gt; a.expand:first-child + em, div.collapsed &gt; a.expand:first-child + em {
    visibility: hidden;
    font-size: 0
    }
p.users-online {
    visibility: hidden;
    font-size: 0;
    }
div.collapsed &gt; a.expand:first-child + em + time + a.expand, div.collapsed &gt; a.expand:first-child + em + time + em + a.expand {
    display: none
    }

/* Blockquotes stolen from circlebroke, thanks brokers - slyder565 */

.md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #ff8686;
    padding: 2px 3px 2px 6px
    }

.listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #ffc986;
    padding: 2px 3px 2px 6px
    }

.listing .listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #ffff86;
    padding: 2px 3px 2px 6px
    }

.listing .listing .listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #9acc86;
    padding: 2px 3px 2px 6px
    }

.listing .listing .listing .listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #86abff;
    padding: 2px 3px 2px 6px
    }

.listing .listing .listing .listing .listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #be89c6;
    padding: 2px 3px 2px 6px
    }

.listing .listing .listing .listing .listing .listing .md blockquote {
    background: #F2F2F2;
    border-left: 8px solid #AAAAAA;
    padding: 2px 3px 2px 6px
    }

.keyHighlight .md blockquote {
    background-color: white !important
    }

.res-nightmode .md blockquote p {
    color: #555555 !important
    }

/* Added by nekosune to add submission guidlines */
#text-desc:after {
    display: block;
    margin-top: 1em;
    content: "Please be sure to review the sidebar and FAQ before posting! This subreddit is heavily moderated. Posts that are disrespectful to GSM (Gender and Sexual Minority) people of any type are subject to removal, and may lead to removal of your posting privileges in this subreddit."
    }

#link-desc:after {
    display: block;
    margin-top: 1em;
    content: "Please be sure to review the sidebar and FAQ before posting! This subreddit is heavily moderated. Posts that are disrespectful to GSM (Gender and Sexual Minority) people of any type are subject to removal, and may lead to removal of your posting privileges in this subreddit."
    }

/* "No Participation"-Mode, aka "Read Only"-Mode
 * by /u/KortoloB
 * /r/NoParticipation
 * 
 * Link people to np.reddit.com/r/YourSubreddit to show them a read-only version.
 * Subscribers will see the full page, only non-subscribers will see the read-only version.
 * This is of course by no means fool-proof, but it should work for the average user.
 *  */

body:lang(np):not(.subscriber) .arrow
{ 
visibility: hidden !important;
}

body:lang(np):not(.subscriber) .usertext-edit, body:lang(np):not(.subscriber) .sidebox.submit, body:lang(np):not(.subscriber) .commentingAs, body:lang(np):not(.subscriber) .markdownEditor, body:lang(np):not(.subscriber) .report-button, body:lang(np):not(.subscriber) a[onclick*="return reply(this)"], body:lang(np):not(.subscriber) .subButtons, body:lang(np):not(.subscriber) .helplink, body:lang(np):not(.subscriber) .titlebox .fancy-toggle-button.toggle &gt; .option.add
{
display: none !important;
}

body:lang(np):not(.subscriber) .styleToggle /* Hides the RES toggle userstyles button, probably gonna get patched if this exploit gets widespread attention */
{
z-index: -1 !important;
}

body:lang(np):not(.subscriber) #siteTable:before
{
content: "You have been linked to a read-only version of this subreddit. Please respect the community by not voting.";
display: block;
max-width: 800px;
background-color: #F6E69F;
padding: 5px 10px;
margin: 5px 305px 5px 0px;
border: 1px solid orange;
font-size: small;
}

body:lang(np):not(.subscriber) .entry.likes:not(.reddit-entry):before, body:lang(np):not(.subscriber) .entry.dislikes:not(.reddit-entry):before
{
content: "Please do not vote or comment when you come from external subreddits.";
color: red;
font-size: large;
font-weight: bold;
}

/* END COPY */
/* ------------------------- */

/* Wiki */

.wiki-page-content .md { margin-right: -280px }

#siteTable:first-child .id-t3_1pnxkl:before {
content: "Welcome visitors from /r/all! Please review the rules of this subreddit before posting. This is a safe space and content deemed inappropriate, offensive or in violation of the rules will be removed. Thank you!";
background-color: #EFF7FF;
border: 2px solid #FF8322;
border-radius: 3px;
margin: 5px 305px 5px 0px;
padding: 5px 10px;
display: block;
font-size: 18px;
text-align: left
}

/* sidebar community icons */
.side .md a[href="#community"]+a {
    font-size: 14px;
    line-height: 32px;
}
.side .md a[href="#community"]+a:hover {
    text-decoration: underline;
}
.side .md a[href="#community"]+a:before {
    content: '';
    width: 32px;
    height: 32px;
    background: url(%%icon-spritesheet%%) -5px -299px;
    background-position: -5px -257px;
    display: inline-block;
    margin-right: 10px;
    vertical-align: middle;
}
.side .md a[href="#community"]+a:hover:before {
    opacity: .9;
}
.side .md a[href="#community"]+a[href*='r/pan']:before {
    background-position: -5px -257px;
}
.side .md a[href="#community"]+a[href*='r/RPANStudio']:before {
    background-position: -5px -803px;
}
.side .md a[href="#community"]+a[href*='r/BestOfRPAN']:before {
    background-position: -5px -719px;
}
.side .md a[href="#community"]+a[href*='r/AnimalsOnReddit']:before {
    background-position: -5px -5px;
}
.side .md a[href="#community"]+a[href*='r/distantsocializing']:before {
    background-position: -5px -47px;
}
.side .md a[href="#community"]+a[href*='r/GlamourSchool']:before {
    background-position: -5px -89px;
}
.side .md a[href="#community"]+a[href*='r/HeadlineWorthy']:before {
    background-position: -5px -131px;
}
.side .md a[href="#community"]+a[href*='r/lgbt']:before {
    background-position: -5px -761px;
}
.side .md a[href="#community"]+a[href*='r/ReadWithMe']:before {
    background-position: -5px -341px;
}
.side .md a[href="#community"]+a[href*='r/RedditInTheKitchen']:before {
    background-position: -5px -173px;
}
.side .md a[href="#community"]+a[href*='r/RedditMasterClasses']:before {
    background-position: -5px -215px;
}
.side .md a[href="#community"]+a[href*='r/RedditSessions']:before {
    background-position: -5px -299px;
}
.side .md a[href="#community"]+a[href*='r/RedditSets']:before {
    background-position: -5px -383px;
}
.side .md a[href="#community"]+a[href*='r/RedditSweats']:before {
    background: url(%%RSW%%);
}
.side .md a[href="#community"]+a[href*='r/shortcircuit']:before {
    background-position: -5px -425px;
}
.side .md a[href="#community"]+a[href*='r/tabletoplive']:before {
    background-position: -5px -593px;
}
.side .md a[href="#community"]+a[href*='r/talentShow']:before {
    background-position: -5px -551px;
}
.side .md a[href="#community"]+a[href*='r/TheArtistStudio']:before {
    background-position: -5px -467px;
}
.side .md a[href="#community"]+a[href*='r/TheGamerLounge']:before {
    background-position: -5px -509px;
}
.side .md a[href="#community"]+a[href*='r/TheYouShow']:before {
    background-position: -5px -635px;
}
.side .md a[href="#community"]+a[href*='r/whereintheworld']:before {
    background-position: -5px -677px;
}

/*

Temporary Holiday Styles

*/
#siteTable &gt; div.thing:nth-child(2n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(2n + 1){
  background-color: rgba(255, 165, 44, .2);
}
#siteTable &gt; div.thing:nth-child(4n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(4n + 1){
  background-color: rgba(255, 255, 65, .2);
}
#siteTable &gt; div.thing:nth-child(6n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(6n + 1){
  background-color: rgba(0, 128, 24, .2);
}
#siteTable &gt; div.thing:nth-child(8n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(8n + 1){
  background-color: rgba(0, 0, 249, .2);
}
#siteTable &gt; div.thing:nth-child(10n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(10n + 1){
  background-color: rgba(134, 0, 125, .2);
}
#siteTable &gt; div.thing:nth-child(12n + 1), .content &gt; .commentarea &gt; .sitetable &gt; div.thing:nth-child(12n + 1){
  background-color: rgba(255, 0, 24, .2);
}