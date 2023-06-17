---
revision_id: f30a0ab2-4a96-11e5-918b-0e550be6a457
revision_date: 1440444788
---

/*** Begin common styles for all flair. ***/
/* If you want to add a new flag, add its flair class to this list. Refer 
 * to "flair images" section below for naming requirements.
 */
span.flair-ainbow, 
span.flair-trans, 
span.flair-bi, 
span.flair-ace, 
span.flair-ally, 
span.flair-pan, 
span.flair-genderqueer,
span.flair-queer,
span.flair-questioning,
span.flair-trans-ainbow, 
span.flair-trans-pan, 
span.flair-trans-bi, 
span.flair-trans-ace, 
span.flair-genderqueer-ainbow, 
span.flair-genderqueer-pan, 
span.flair-genderqueer-bi, 
span.flair-genderqueer-ace
{
visibility: visible;
width: 18px;
height: 12px;
padding: 0;
margin: 0;
}


/* TROLLSLAYER special flare added */
.flair-trollslayer {
      background: url(%%trollslayer%%) no-repeat 0 0;
      width: 25px;
      height: 36px;
      border: 0;
      padding: 0;
}

/*** Fixed text cropping in flair, occurring in moderator box (Height +2px) -Zazie_Lavender &lt;-- Raises all the flags for everyone, though? ~CW ***/
/*** End common styles for all flair ***/

/*** Begin common styles for inline images. ***/
/* Same deal, add URL selector here for additional flags. Refer to 
 * inline images section below for URL usage. */
a[href="/ally"]:after, 
a[href="/ainbow"]:after, 
a[href="/trans"]:after, 
a[href="/bi"]:after, 
a[href="/ace"]:after, 
a[href="/pan"]:after, 
a[href="/genderqueer"]:after,
a[href="/queer"]:after,
a[href="/questioning"]:after,
a[href="/trans-ainbow"]:after, 
a[href="/trans-bi"]:after, 
a[href="/trans-pan"]:after, 
a[href="/trans-ace"]:after, 
a[href="/genderqueer-ainbow"]:after,
a[href="/genderqueer-bi"]:after,
a[href="/genderqueer-pan"]:after,
a[href="/genderqueer-ace"]:after
{
    width: 18px;
    height: 12px;
    content: "";
    background-position: -0px;
    display: inline-block;
    border: 1px solid #DDD;
    border-radius: 2px;
}

span.flair
{
   text-indent: 22px;
   width: auto;
   min-width: 15px;
   padding-right: 3px;
}

/* commenting out the hover text code
span.flair:hover
{ 
   text-indent: 22px;
   width: auto;
   padding-right: 3px;
}
*/

/*** End common styles for inline images. ***/

/*** Begin flair images. ***/
/* The %%flagname%% should correspond to whatever you entered as the
 * image name in the stylesheet page. If you take the suggested filename
 * from when you upload them, it should just work. 
 * The word after span.flair- should be what you enter into the CSS class
 * box on the flair template page. So for span.flair-ainbow you would enter
 * ainbow in the flair template's CSS class. 
 */

span.flair-ally { background:#F5F5F5 url(%%ally%%) no-repeat left top !important; }
span.flair-ainbow { background:#F5F5F5 url(%%ainbow%%) no-repeat left top !important;}
span.flair-bi { background:#F5F5F5 url(%%bi%%) no-repeat left top !important; }
span.flair-ace { background:#F5F5F5 url(%%ace%%) no-repeat left top !important; }
span.flair-trans { background:#F5F5F5 url(%%trans%%) no-repeat left top !important; }
span.flair-pan { background:#F5F5F5 url(%%pan%%) no-repeat left top !important; }
span.flair-genderqueer { background:#F5F5F5 url(%%gq%%) no-repeat left top !important; }
span.flair-queer { background:#F5F5F5 url(%%queer%%) no-repeat left top !important; }
span.flair-questioning { background:#F5F5F5 url(%%questioning%%) no-repeat left top !important; }
span.flair-trans-ainbow { background:#F5F5F5 url(%%trans-ainbow%%) no-repeat left top !important; }
span.flair-trans-pan { background:#F5F5F5 url(%%trans-pan%%) no-repeat left top !important; }
span.flair-trans-bi { background:#F5F5F5 url(%%trans-bi%%) no-repeat left top !important; }
span.flair-trans-ace { background:#F5F5F5 url(%%trans-ace%%) no-repeat left top !important; }
span.flair-genderqueer-ainbow { background:#F5F5F5 url(%%gq-ainbow%%) no-repeat left top !important; }
span.flair-genderqueer-pan { background:#F5F5F5 url(%%gq-pan%%) no-repeat left top !important; }
span.flair-genderqueer-bi { background:#F5F5F5 url(%%gq-bi%%) no-repeat left top !important; }
span.flair-genderqueer-ace { background:#F5F5F5 url(%%gq-ace%%) no-repeat left top !important; }
span.flair-misanthropicusername {background:#F5F5F5 url(%%misanthropicusername%%) no-repeat left top !important; }

/* This flair style should be entered as "none" (no quotes) in the flair
 * template screen. It's to let people unset their flag. */
.flair-none { display:none; }

/*** End flair images ***/


/*** Begin inline images ***/

/* This allows you to insert flair, rage-face style, into posts or comments
 * with [](/flagname). This is mainly for the sidebar, or for announcements
 * but will also work for any user in the comments. 
 */

a[href="/ally"]:after { background-image: url(%%ally%%); }
a[href="/ainbow"]:after { background-image: url(%%ainbow%%); }
a[href="/trans"]:after { background-image: url(%%trans%%); }
a[href="/bi"]:after { background-image: url(%%bi%%); }
a[href="/ace"]:after { background-image: url(%%ace%%); }
a[href="/pan"]:after { background-image: url(%%pan%%); }
a[href="/genderqueer"]:after { background-image: url(%%gq%%); }
a[href="/queer"]:after { background-image: url(%%queer%%); }
a[href="/questioning"]:after { background-image: url(%%questioning%%); }
a[href="/trans-ainbow"]:after { background-image: url(%%trans-ainbow%%); }
a[href="/trans-bi"]:after { background-image: url(%%trans-bi%%); }
a[href="/trans-pan"]:after { background-image: url(%%trans-pan%%); }
a[href="/trans-ace"]:after { background-image: url(%%trans-ace%%); }
a[href="/genderqueer-ainbow"]:after { background-image: url(%%gq-ainbow%%); }
a[href="/genderqueer-bi"]:after { background-image: url(%%gq-bi%%); }
a[href="/genderqueer-pan"]:after { background-image: url(%%gq-pan%%); }
a[href="/genderqueer-ace"]:after { background-image: url(%%gq-ace%%); }

/* End inline images */

/* Beginning of the "readers" and "subscribed now" custom code */

.subscribers .word,
.users-online .word {
    display: none;
}

.subscribers .number:after {
content: " Incorrectly Assigned Redditors";
}

.users-online .number:after {
content: " Trans Females Here Right Now";
} 

/* END of the "readers" and "subscribed now" custom code */



/* Begin code to remove downvote arrows */

/*            .down{display:none}
.commentarea.arrow.down, .commentarea.arrow.downmod {display:block}    */

/* End downvote remover */

/* TEST */

/* ==Edurne Reddit CSS Theme v5.6 - (http://www.reddit.com/r/edurne/)== */

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

#sr-header-area a { color:#54708b; }
body.res-nightmode #header { border-color: #DDF; }
body.res-nightmode #header .tabmenu li:not(.selected) a { color: #346; }
#header .tabmenu li.selected a { border: 0; border-bottom: 1px solid #FFF; }
#header .tabmenu li:not(.selected):hover a { background-color: #449EF8; color: #FFF; }
body.res-nightmode #header .tabmenu li { background-color: #DDD !important; }
body.res-nightmode #header .tabmenu li:not(.selected):hover a { background-color: #CCC; color: #444; }
#header-img { margin:8px 20px 0; }
.pagename { margin-right:25px; font-weight:bold; font-variant:normal; font-size:18px; }
body.res-nightmode .pagename a { font-size: 18px !important; }
#sr-header-area .dropdown.srdrop, #sr-header-area#srLeftContainer { padding-left:21px; }
#sr-more-link, #header #sr-header-area #RESShortcutsEditContainer, #header #sr-header-area #RESShortcutsRight, #header #sr-header-area #RESShortcutsLeft,
#header #sr-header-area #RESShortcutsAdd, #header #sr-header-area #RESShortcutsTrash { background-color:#c6daed; }
body.res-nightmode #sr-header-area, body.res-nightmode #sr-more-link { background-color: #c6daed !important; }
#sr-header-area #RESShortcutsEditContainer, #sr-more-link { border-right:20px solid #c6daed; font-weight:bolder; }

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
.side .titlebox &gt; h1 { font-size:34px; letter-spacing: -1px;}
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
.sidebox.submit { width:300px; }
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
.disabled .morelink .nub,.disabled .morelink:hover .nub { background:url(%%sprites-05%%) 0 0 no-repeat transparent; border-color:#f5f5f5; }

/* CONTENT */

/* main content */
.sitetable { font-family:verdana, arial, helvetica, sans-serif; clear:left;}
.infobar { overflow:hidden; margin:0 0 10px; }
.content { margin:20px 0 0 20px; }

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
.link.self .usertext-body .md p,.comment .usertext-body .md p { line-height:1.3em; }
.link .usertext .md { padding:5px 10px; }
.panestack-title { border:none; margin:0; padding:0; }
.panestack-title .title { float:left; font-size:11px; color:#888; margin:0; }
.commentarea .menuarea { font-size:11px; margin:0; }
.panestack-title:after { content:'-'; padding:0 5px; float:left; }
.commentarea &gt; .usertext { clear:left; margin:0; }
.usertext-edit { width:auto; }
.usertext-edit textarea { width:430px; padding:10px; }
.usertext .bottom-area { width:450px; }
.comment .usertext .bottom-area { width:100%; }
.usertext button { margin:5px 5px 10px 0; border:none; min-width:70px; }
body.res-nightmode .usertext .help-toggle { background-color:#DDD; }
.usertext .help-toggle a { color:#FFF; }
body.res-nightmode .usertext .help-toggle a { color:#444 !important; }
.usertext table.markhelp { width:450px; font-size:11px; }
.link .usertext .md { background-color:#FFF; border:1px solid #EAEAEA; }
.entry .buttons li a { font-family:verdana, arial, sans-serif; }

.usertext .help-toggle, .res-nightmode button.RESBigEditorPop, .usertext .bottom-area .reddiquette {
    background-color:#999;
    border:none;
    color:#FFF;
    padding:6px;
    margin:5px 3px;
    font-size:13px;
    -moz-border-radius:0px;
    -webkit-border-radius:0px;
    -o-border-radius:0px;
    -ms-border-radius:0px;
    -khtml-border-radius:0px;
    border-radius: 0;
}

#RESShortcutsSort { background-color:transparent !important; }
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
.side a[href*='#icon-'] { color:#000; cursor:default; }
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















/* Adds a hover box over the report button */
.linklisting .report-button:hover:before {
    content: "This is checked regularly by both human and robot mods";
    position: absolute;
    display: block;
    z-index: 1000;
    padding: 5px;
    border: 1px solid Red;
    border-radius: 5px;
    background-color: white;
    color: red;
    text-align: center;
    font-size: 11px;
    font-weight: normal;
    margin-left: -15px;
    margin-top: -50px;
    box-shadow: 2px 2px 5px #888888
    }
/* ###### R.B. Message ###### [5.2] */
/* Makes the report button show a more verbose note. */
    .report-button &gt; span.option.error:before {
    content: "This isn't a super down-vote. Only report spam or rule violations!"
    }





/* ###### Submission Warning ###### [8.2] */
/* Submission page warning text*/
#link-desc:after, #text-desc:after {
    display: block;
    margin-top: 1em;
    font-weight: bold;
    font-size:100%;
    color: blue;
    content: "Please read the rules in the sidebar before submitting!"
    }



/* EXTREMELY EXPERIMENTAL TEST!!!!!!!!! */

/*SIDEBAR RULES HOVER BOX!*/
/*************************/
.side table {
  display: block;
  margin-left: 0;
}
.side table td { width:280px; }
.side table thead {
  display: none;
}

.side table tbody tr td {
  display: block;
  border: none;
}
.side table tbody tr td:first-child {
  background: #cee3f8;
  color: #000000;
  padding: 3px;
  cursor: pointer;
  border: 1px solid #000022;
  border-spacing: 1px;
  border-color: white;
}

.side table tbody tr td:first-child a{
  color: #336699;
font-weight: bold;
}

.side table tbody tr td:first-child:hover, .side table tbody tr:hover td:first-child {
background: #cee3f8;
color: black;
}

.side table tbody tr td:first-child:hover a, .side table tbody tr:hover td:first-child a{
color: #ff4500;
}


.side table tbody tr td:last-child {
  display: none;
  color: black; 
  border-top: 0;
  padding: 0px 0px 0px;
}
.side table tbody tr:hover td:last-child {
  display: block;
}
.side h6:nth-of-type(1) {
  position: absolute;
  top: 70px;
  left: 53px;
  background: #222299;
  color: black;
  border: 1px solid #000066;
  border-left: 0;
  border-right: 0;
  height: 24px;
  line-height: 24px;
  text-shadow: 0px 1px 0px #222299;
}
.side h6:nth-of-type(1) a, .side h6:nth-of-type(1) a:visited {
  color: inherit;
}

/******************************/
/*END SIDEBAR RULES HOVER BOX*/


/* ###### Link Flair ###### [2.1] */
.linkflairlabel {
    color:green 
    !important; 
    font-weight:900; 
    background:white 
    !important; 
    border:1px solid green;
}