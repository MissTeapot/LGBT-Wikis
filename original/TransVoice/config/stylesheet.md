---
revision_id: 2c6a6052-6af0-11eb-80f4-0e06f0578723
revision_date: 1612886533
---

/* ==Edurne Reddit CSS Theme v5.6 - (http://www.reddit.com/r/edurne/)== */
/* POST FLAIR */
.linkflair-discussion .linkflairlabel { background-color: #add5ab; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-question .linkflairlabel { background-color: #b5bbde; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-av .linkflairlabel { background-color: #b266ff; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-resource .linkflairlabel { background-color: #ffe5cc; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-event .linkflairlabel { background-color: #ffff33; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-criticism .linkflairlabel { background-color: #ff3333; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-masc .linkflairlabel { background-color: #ccffff; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}
.linkflair-fem .linkflairlabel { background-color: #ffccff; font-size: 11px; font-weight: bold; color:#000000; border-color: #000000; border-width: 1px; border-radius: 3px;}

/* SIDEBAR FLAIR REDIRECTION */
html:lang(di) .link:not(.linkflair-discussion) { display: none }
html:lang(qu) .link:not(.linkflair-question) { display: none }
html:lang(av) .link:not(.linkflair-av) { display: none }
html:lang(re) .link:not(.linkflair-resource) { display: none }
html:lang(ev) .link:not(.linkflair-event) { display: none }
html:lang(cr) .link:not(.linkflair-criticism) { display: none }
html:lang(tm) .link:not(.linkflair-masc) { display: none }
html:lang(tf) .link:not(.linkflair-fem) { display: none }


/* SIDEBAR FLAIR CSS */
.side a[href*='#di'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #add5ab;}
.side a[href*='#qu'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #b5bbde;}
.side a[href*='#av'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #b266ff;}
.side a[href*='#re'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #ffe5cc;}
.side a[href*='#ev'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #ffff33;}
.side a[href*='#cr'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #ff3333;}
.side a[href*='#tm'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #ccffff;}
.side a[href*='#tf'] { display: inline-block; position: relative; margin-top:0px; border: 2px solid black; font-size: 100%; padding: 3px; color: black; font-weight: bold; background: #ffccff;}

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

/* No Participation CSS credit to /r/noparticipation, slightly modified */
body:lang(np):not(.subscriber) .arrow { 
    visibility: hidden !important;
}

body:lang(np):not(.subscriber) .usertext-edit,
body:lang(np):not(.subscriber) .sidebox.submit,
body:lang(np):not(.subscriber) .commentingAs,
body:lang(np):not(.subscriber) .markdownEditor, 
body:lang(np):not(.subscriber) .report-button,
body:lang(np):not(.subscriber) a[onclick*="return reply(this)"],
body:lang(np):not(.subscriber) .subButtons,
body:lang(np):not(.subscriber) .helplink,
body:lang(np):not(.subscriber) .titlebox .fancy-toggle-button.toggle &gt; .option.add {
    display: none !important;
}

body:lang(np):not(.subscriber) &gt; .content:before {
    content: "You have been linked to a read-only version of this subreddit. Please respect the community by not voting.";
    display: block;
    max-width: 800px;
    background-color: #F6E69F;
    padding: 5px 10px;
    margin: 5px 2px;
    border: 1px solid orange;
    font-size: small;
    text-align: center;
}

body:lang(np):not(.subscriber) .entry.likes:not(.reddit-entry):before,
body:lang(np):not(.subscriber) .entry.dislikes:not(.reddit-entry):before {
    content: "Please do not vote or comment when you come from external subreddits.";
    color: red;
    font-size: large;
    font-weight: bold;
}

/* Wiki protection */
body.wiki-page:lang(np):not(.subscriber) span.pageactions a.wikiaction-edit:not(.wikiaction-current),
body.wiki-page:lang(np):not(.subscriber) div.wiki-page-content form#editform label[for='reason'],
body.wiki-page:lang(np):not(.subscriber) div.wiki-page-content form#editform input#wiki_revision_reason,
body.wiki-page:lang(np):not(.subscriber) div.wiki-page-content form#editform input[type='submit'] {
    display: none !important;
}

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
ol li p, ul li p { display: inline; }

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