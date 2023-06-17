---
revision_id: d02f99fa-073a-11e7-a9a3-0e93c866da84
revision_date: 1489333484
---

/* ==Edurne Reddit CSS Theme v5.1.5 - (http://www.reddit.com/r/edurne/)== */

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
.tabmenu { font-size:11px; }
#header .tabmenu { border: 1px solid #5F99CF; border-bottom: 0; }
body.res-nightmode #header .tabmenu { border-color: #DDF; }
#header .tabmenu li { margin: 0; }
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
.side .titlebox &gt; h1 { font-size:34px; }
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
.sidebox.submit { position:absolute; top:95px; width:300px; }
body.res-nightmode .sidebox { padding-left: 0 !important; }
body.res-nightmode .sidebox.submit { background-image: none !important; }

body.res-nightmode .sidebox.submit .nub {
    height: 3px;
    width: 2px;
    border-left: 14px solid #393939;
    border-top: 14px solid #222;
    border-bottom: 14px solid #222;
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
    border-color:#449EF8;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

.morelink a,.morelink a:hover { color:#FFF; font-family:Verdana, Arial, sans-serif; font-size:16px; }
.morelink .nub,.morelink:hover .nub { background:url(%%sprites-05%%) 0 0 no-repeat transparent; }
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
.md &gt; ul, .md &gt; ol { /*border-left: 2px solid #ccc;*/ }
body.res-nightmode .md &gt; ul, body.res-nightmode .md &gt; ol { border-color: #666; }

.md ol {
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

.md ul {
    margin: 10px 0px;
    padding: 6px 6px 6px 27px;
    background-color: #fff;
    -moz-border-radius:2px;
    -webkit-border-radius:2px;
    -o-border-radius:2px;
    -ms-border-radius:2px;
    -khtml-border-radius:2px;
    border-radius:2px;
}

body.res-nightmode .md ul, body.res-nightmode .md ol { background-color: #444; }
.md ul { list-style: disc; }
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

.side a[href='#icon-exclamation']::before {background-position: -16px -32px;}
.side a[href='#icon-information']::before {background-position: -54px -51px;}
.side a[href='#icon-lightbulb']::before {background-position: -16px -51px;}
.side a[href='#icon-comments']::before {background-position: -35px -89px;}
.side a[href='#icon-unhappy']::before {background-position: -73px -89px;}
.side a[href='#icon-check']::before {background-position: -73px -51px;}
.side a[href='#icon-clock']::before {background-position: -35px -51px;}
.side a[href='#icon-cross']::before {background-position: -35px -70px;}
.side a[href='#icon-smile']::before {background-position: -54px -89px;}
.side a[href='#icon-error']::before {background-position: -54px -32px;}
.side a[href='#icon-note']::before {background-position: -54px -70px;}
.side a[href='#icon-star']::before {background-position: -73px -32px;}
.side a[href='#icon-help']::before {background-position: -16px -70px;}
.side a[href='#icon-time']::before {background-position: -73px -70px;}
.side a[href='#icon-bell']::before {background-position: -35px -32px;}
.side a[href='#icon-eye']::before {background-position: -16px -89px;}

/* SUBREDDIT-SPECIFIC STYLES - add you own styles below without modifying the code above.*/

/* Trigger Warnings */
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
div.collapsed &gt; a.expand:first-child + em + time + a.expand, div.collapsed &gt; a.expand:first-child + em + time + em + a.expand {
    display: none
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


/* hover text for the report button */
.report-button .option:not(.error):hover:before {
    color: black;
    background-color: #CCF;
    border: 1px solid #333;
    border-radius: 4px;
    content: "Please message the moderators if you click report, otherwise we won't know why it was reported. Direct links and specific descriptions of the situation you are reporting in your message will assist moderators in quickly resolving your issue.";
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

a[href="/trigger"] {color:black!important;background-color:black!important;}
a[href="/trigger"]:hover {color:black!important;background-color:white!important;}
div.md table{margin:2px;padding:0;text-align:center;}
/* div.md * tr th{margin:0; padding: 0;border-style:none;width:100%;} */ /* Commented to fix table bug */

/* ------------------------- */
/* BEGIN COPY */


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

body:lang(np):not(.subscriber) .usertext-edit,
body:lang(np):not(.subscriber) .sidebox.submit,
body:lang(np):not(.subscriber) .commentingAs,
body:lang(np):not(.subscriber) .markdownEditor, 
body:lang(np):not(.subscriber) .report-button,
body:lang(np):not(.subscriber) a[onclick*="return reply(this)"],
body:lang(np):not(.subscriber) .subButtons,
body:lang(np):not(.subscriber) .helplink,
body:lang(np):not(.subscriber) .titlebox .fancy-toggle-button.toggle &gt; .option.add
{
display: none !important;
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

body:lang(np):not(.subscriber) .entry.likes:not(.reddit-entry):before,
body:lang(np):not(.subscriber) .entry.dislikes:not(.reddit-entry):before
{
content: "Please do not vote or comment when you come from external subreddits.";
color: red;
font-size: large;
font-weight: bold;
}

/* Attempts to disrupt RES form hiding CSS styles */
body.res:lang(np):not(.subscriber) div.titlebox &gt; div[style*='display: block !important'] input:before,
body.res:lang(np):not(.subscriber) div.titlebox &gt; div[style*='display: block !important'] label:before,
body.res:lang(np):not(.subscriber) &gt; div#keyCommandLineWidget &gt; form:before
{
content: 'Removed by NoParticipation' !important;
margin-left: -10000px !important;
}

/* END COPY */


/*** Begin common styles for all flair. ***/
/* If you want to add a new flag, add its flair class to this list. Refer 
 * to "flair images" section below for naming requirements.
 *//*

span.flair-robot,
span.flair-trans, 
span.flair-ally, 
span.flair-genderqueer,
span.flair-gq-questioning,
span.flair-trans-questioning
{
visibility: visible;
width: 18px;
height: 12px;
padding: 0;
margin: 0;
}
/*** End common styles for all flair ***/

/*** Begin common styles for inline images. ***/
/* Same deal, add URL selector here for additional flags. Refer to 
 * inline images section below for URL usage. */
a[href="/ally"]:after, 
a[href="/trans"]:after, 
a[href="/genderqueer"]:after,
a[href="/gq-questioning"]:after,
a[href="/trans-questioning"]:after
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

span.flair-robot { background:#F5F5F5 url(%%robot%%) no-repeat left top !important; }
span.flair-ally { background:#F5F5F5 url(%%ally%%) no-repeat left top !important; }
span.flair-trans { background:#F5F5F5 url(%%trans%%) no-repeat left top !important; }
span.flair-genderqueer { background:#F5F5F5 url(%%gq%%) no-repeat left top !important; }
span.flair-gq-questioning { background:#F5F5F5 url(%%gq-questioning%%) no-repeat left top !important; }
span.flair-trans-questioning { background:#F5F5F5 url(%%trans-questioning%%) no-repeat left top !important; }

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
a[href="/trans"]:after { background-image: url(%%trans%%); }
a[href="/genderqueer"]:after { background-image: url(%%gq%%); }
a[href="/trans-questioning"]:after { background-image: url(%%trans-questioning%%); }
a[href="/gq-questioning"]:after { background-image: url(%%trans-questioning%%); }

/* End inline images */

/* /u/mspenguinette flair */



.flair {
   background-image: url(%%longflairislongnew%%);
   background-repeat: no-repeat;
   width: auto;
   height: 12px;
   min-width: 14px;
   text-indent: 20px;
   background-color: transparent;
   border: none;
   background-color: whiteSmoke;
   border: 1px solid #ddd;
    padding: 0;
}

.flair:hover {
   border: 1px solid #CBD5DD;
}

.flair-plain {
   background-image: none;
   height: 12px;
}

.flair-grayt {
   background-image: none;
   background-color: #cf0000;
   color: white;
   height: 12px;
}

.flair-ainbow-questioning{background-position: 0px -12px;}
.flair-ainbow{background-position: 0px -24px;}
.flair-ainbow-bi{background-position: 0px -36px;}
.flair-ainbow-pan{background-position: 0px -48px;}
.flair-ainbow-ace{background-position: 0px -60px;}
.flair-ainbow-straight{background-position: 0px -72px;}
.flair-ainbow-queer{background-position: 0px -84px;}
.flair-ainbow-trans{background-position: 0px -96px;}
.flair-ainbow-gq{background-position: 0px -108px;}
.flair-ainbow-genderfluid{background-position: 0px -120px;}
.flair-ainbow-polysexual{background-position: 0px -132px;}
.flair-bi-questioning{background-position: 0px -144px;}
.flair-bi-ainbow{background-position: 0px -156px;}
.flair-bi{background-position: 0px -168px;}
.flair-bi-pan{background-position: 0px -180px;}
.flair-bi-ace{background-position: 0px -192px;}
.flair-bi-straight{background-position: 0px -204px;}
.flair-bi-queer{background-position: 0px -216px;}
.flair-bi-trans{background-position: 0px -228px;}
.flair-bi-gq{background-position: 0px -240px;}
.flair-bi-genderfluid{background-position: 0px -252px;}
.flair-bi-polysexual{background-position: 0px -264px;}
.flair-pan-questioning{background-position: 0px -276px;}
.flair-pan-ainbow{background-position: 0px -288px;}
.flair-pan-bi{background-position: 0px -300px;}
.flair-pan{background-position: 0px -312px;}
.flair-pan-ace{background-position: 0px -324px;}
.flair-pan-straight{background-position: 0px -336px;}
.flair-pan-queer{background-position: 0px -348px;}
.flair-pan-trans{background-position: 0px -360px;}
.flair-pan-gq{background-position: 0px -372px;}
.flair-pan-genderfluid{background-position: 0px -384px;}
.flair-pan-polysexual{background-position: 0px -396px;}
.flair-ace-questioning{background-position: 0px -408px;}
.flair-ace-ainbow{background-position: 0px -420px;}
.flair-ace-bi{background-position: 0px -432px;}
.flair-ace-pan{background-position: 0px -444px;}
.flair-ace{background-position: 0px -456px;}
.flair-ace-straight{background-position: 0px -468px;}
.flair-ace-queer{background-position: 0px -480px;}
.flair-ace-trans{background-position: 0px -492px;}
.flair-ace-gq{background-position: 0px -504px;}
.flair-ace-genderfluid{background-position: 0px -516px;}
.flair-ace-polysexual{background-position: 0px -528px;}
.flair-straight-questioning{background-position: 0px -540px;}
.flair-straight-ainbow{background-position: 0px -552px;}
.flair-straight-bi{background-position: 0px -564px;}
.flair-straight-pan{background-position: 0px -576px;}
.flair-straight-ace{background-position: 0px -588px;}
.flair-straight{background-position: 0px -600px;}
.flair-straight-queer{background-position: 0px -612px;}
.flair-straight-trans{background-position: 0px -624px;}
.flair-straight-gq{background-position: 0px -636px;}
.flair-straight-genderfluid{background-position: 0px -648px;}
.flair-straight-polysexual{background-position: 0px -660px;}
.flair-queer-questioning{background-position: 0px -672px;}
.flair-queer-ainbow{background-position: 0px -684px;}
.flair-queer-bi{background-position: 0px -696px;}
.flair-queer-pan{background-position: 0px -708px;}
.flair-queer-ace{background-position: 0px -720px;}
.flair-queer-straight{background-position: 0px -732px;}
.flair-queer{background-position: 0px -744px;}
.flair-queer-trans{background-position: 0px -756px;}
.flair-queer-gq{background-position: 0px -768px;}
.flair-queer-genderfluid{background-position: 0px -780px;}
.flair-queer-polysexual{background-position: 0px -792px;}
.flair-trans-questioning{background-position: 0px -804px;}
.flair-trans-ainbow{background-position: 0px -816px;}
.flair-trans-bi{background-position: 0px -828px;}
.flair-trans-pan{background-position: 0px -840px;}
.flair-trans-ace{background-position: 0px -852px;}
.flair-trans-straight{background-position: 0px -864px;}
.flair-trans-queer{background-position: 0px -876px;}
.flair-trans{background-position: 0px -888px;}
.flair-trans-gq{background-position: 0px -900px;}
.flair-trans-genderfluid{background-position: 0px -912px;}
.flair-trans-polysexual{background-position: 0px -924px;}
.flair-gq-questioning{background-position: 0px -936px;}
.flair-gq-ainbow{background-position: 0px -948px;}
.flair-gq-bi{background-position: 0px -960px;}
.flair-gq-pan{background-position: 0px -972px;}
.flair-gq-ace{background-position: 0px -984px;}
.flair-gq-straight{background-position: 0px -996px;}
.flair-gq-queer{background-position: 0px -1008px;}
.flair-gq-trans{background-position: 0px -1020px;}
.flair-gq{background-position: 0px -1032px;}
.flair-gq-genderfluid{background-position: 0px -1044px;}
.flair-gq-polysexual{background-position: 0px -1056px;}
.flair-genderfluid-questioning{background-position: 0px -1068px;}
.flair-genderfluid-ainbow{background-position: 0px -1080px;}
.flair-genderfluid-bi{background-position: 0px -1092px;}
.flair-genderfluid-pan{background-position: 0px -1104px;}
.flair-genderfluid-ace{background-position: 0px -1116px;}
.flair-genderfluid-straight{background-position: 0px -1128px;}
.flair-genderfluid-queer{background-position: 0px -1140px;}
.flair-genderfluid-trans{background-position: 0px -1152px;}
.flair-genderfluid-gq{background-position: 0px -1164px;}
.flair-genderfluid{background-position: 0px -1176px;}
.flair-genderfluid-polysexual{background-position: 0px -1188px;}
.flair-polysexual-questioning{background-position: 0px -1200px;}
.flair-polysexual-ainbow{background-position: 0px -1212px;}
.flair-polysexual-bi{background-position: 0px -1224px;}
.flair-polysexual-pan{background-position: 0px -1236px;}
.flair-polysexual-ace{background-position: 0px -1248px;}
.flair-polysexual-straight{background-position: 0px -1260px;}
.flair-polysexual-queer{background-position: 0px -1272px;}
.flair-polysexual-trans{background-position: 0px -1284px;}
.flair-polysexual-gq{background-position: 0px -1296px;}
.flair-polysexual-genderfluid{background-position: 0px -1308px;}
.flair-polysexual{background-position: 0px -1320px;}
.flair-questioning{background-position: 0px -1332px;}
.flair-blank{background-position: 0px -1344px;}
.flair-ally{background-position: 0px -1356px;}
.flair-intersex{background-position: 0px -1368px;}
.flair-lipstick{background-position: 0px -1380px;}
.flair-bear{background-position: 0px -1392px;}
.flair-male{background-position: 0px -1404px;}
.flair-female{background-position: 0px -1416px;}
.flair-third{background-position: 0px -1428px;}
.flair-partner{background-position: 0px -1440px;}
.flair-scholar{background-position: 0px -1452px;}
.flair-gynoromantic{background-position: 0px -1464px;}
.flair-androgynoromantic{background-position: 0px -1476px;}
.flair-androromantic{background-position: 0px -1488px;}
.flair-neutroisromantic{background-position: 0px -1500px;}
.flair-transromantic{background-position: 0px -1512px;}
.flair-heteromantic{background-position: 0px -1524px;}
.flair-homoromantic{background-position: 0px -1536px;}
.flair-panromantic{background-position: 0px -1548px;}
.flair-biromantic{background-position: 0px -1560px;}
.flair-polyromantic{background-position: 0px -1572px;}
.flair-monoromantic{background-position: 0px -1584px;}
.flair-lithromantic{background-position: 0px -1596px;}
.flair-demiromantic{background-position: 0px -1608px;}
.flair-aromantic{background-position: 0px -1620px;}
.flair-agender{background-position: 0px -1632px;}
.flair-demiboy{background-position: 0px -1644px;}
.flair-demigirl{background-position: 0px -1656px;}
.flair-nonbinary{background-position: 0px -1668px;}	


.flairselector{
border-radius: 8px;
-moz-border-radius: 8px;
padding-top: 1px;
}

.flairselector ul li:nth-of-type(3n+1),.flairselector ul li:nth-of-type(6),.flairselector ul li:nth-of-type(10),.flairselector ul li:nth-of-type(41), flairselector ul li:last-of-type {
border-bottom: 1px solid black;
padding-bottom: 5px;
margin-bottom: 5px;
}

.flairselector ul li:nth-of-type(1),.flairselector ul li:nth-of-type(4),.flairselector ul li:nth-of-type(7){
border-bottom: none !important;
margin-bottom: 0px !important;
padding-bottom: 0px !important;
}

.flairoptionpane ul li a{
display: none;
}

/* Fancy sidebar rules table */
.side .md &gt; p{
    font-size: 75%;
    float: right;
    margin-top: -3em;
}
.side .md table{
width: 99%;
}
.side thead{
display:none;
}
.side table tbody tr td {
display: block;
cursor: pointer;
border: 0;
}
.side table tbody tr td:first-child {
color: #000000;
cursor: pointer;
border-spacing: 1px;
border-color: white;
font-weight: bold;
}
.side table tbody tr:nth-child(odd) {
background: #f6f6f6;
}
.side table tbody tr:nth-child(even) {
background: #ffffff;
}
.side table tbody tr td:last-child {
display: none;
color: black;
}
.side table tbody tr:hover td:last-child {
display: block;
}