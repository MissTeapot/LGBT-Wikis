---
revision_id: 3894805a-d6b3-11e5-b4bc-0e6bc3308ce5
revision_date: 1455850094
---

/*------------------------------------------------------------------------------------------------------
        SimplePlus v0.9.8:
            ~ Developed by /u/Blisschen
            ~ Theme last modified 24 December 2015
       
        "It doesn’t matter whether little curly brackets live on the same lines or on new lines.
        It’s your code, you decide. Just be consistent. :)"
            @BobRossGameDev
           
        Control/Command-F Navagation:
            ~ BODY                          (used for fonts and other subreddit-wide changes)
            ~ HEADER                        (handles subreddit background, and tileable vs full-sized header)
            ~ SIDEBAR AND SUBMIT            (search, submit, and formatting)
            ~ CONTENT AND POSTS             (sticky post, nsfw post, and other fixes)
            ~ USER FLAIRS                   (user flairs, must be enabled on flair page)
            ~ LINK FLAIRS                   (link/post flairs, must also be enabled on flair page)
            ~ SNIPPETS                      (place your own code, or code from the wiki here)
------------------------------------------------------------------------------------------------------*/
 
 
 
/* BODY */
body {font-family: -apple-system, San Francisco Display, Helvetica Neue, Helvetica, Segoe UI, Verdana, Arial, sans-serif;}
 
 
 
/* HEADER */
#header{
    background-image: linear-gradient(
      rgba(255, 255, 255, 0.2),
      rgba(255, 255, 255, 0.2)
    ),url(%%bck1%%);
    background-position: left center;
    height:200px;
    border:none;
    box-shadow: 0 1.5px 4px rgba(0,0,0,0.24),0 1.5px 6px rgba(0,0,0,0.12);
    /* IF YOU ARE USING A FULL-SIZED (1000px) BACKGROUND, YOU MUST ENABLE BELOW THIS LINE
    background-repeat:no-repeat;
    background-size: 100%;*/
}
 
#header:after {
    position: absolute;
    top: 165px;
    width: 100%;
    height: 40px;
    background: rgba(255,255,255,0.8);
    content: " ";
    z-index: -1;
}
 
#header-bottom-left {
    bottom: 0;
    height: 20px;
    left: 90px;
    position: absolute;
    font-weight: 700;
    color: #369;
}
 
#header-bottom-left a{color: #369;font-variant:normal;}
#header-img {position: absolute;bottom: -5px;left: -80px;}
#header-bottom-left ul.tabmenu li a[href$="/ads/"]{display:none!important;}
.tabmenu #viewImagesButton {display: none!important;}
.tabmenu li.selected a{color: orangered!important;}
 
.tabmenu.formtab .selected a {
    color: white!important;
    font-size: 130%;
    background-color: #5f99cf;
    border: 2px solid #5F99CF!important;
}
 
#header-bottom-right {
    background:none;
    top: 175px !important;
    right: 20px;
    padding: 0px !important;
    font-weight: 700;
    font-size: 11px;
}
 
.pagename{
    position: relative;
    top: -8px;
    margin-right: 80px;
    margin-left: -13px;
}
 
.pagename a {color: #369; font-size: 16px;}
 
#sr-header-area {
    background-color: #000;
    background-color: rgba(255,255,255,0.8)!important;
    border: none;
    color: #fff;
    font-weight: 400;
    width: 100%;
    z-index: 9999;
}
 
.sr-bar a, .dropdown.srdrop .selected,.drop-choices a.choice {color:#369;font-weight: bold;text-transform:none;}
.drop-choices{background-color: rgba(255,255,255,0.9)!important;}
.tabmenu li a {padding: 2px 6px 0 6px;background-color: rgba(255,255,255,0.6);}
   
.tabmenu li.selected a {
    color: orangered;
    background-color: white;
    border-bottom: 5px solid white!important;
    z-index: 100;
    border:none;
}
 
 
 
/* SIDEBAR AND SUBMIT */
 
#search input[type=text]{border: 1px solid #369;}
.infobar{background: #fff;border: 1px solid #369;}
.titlebox h1 a {width: 100%;color: #369!important;text-align: center;font-size: 25px;}
.titlebox .fancy-toggle-button{margin-top: 2px;}
.formtabs-content {border-top: 4px solid #336699;}
.infobar {background-color: #f6e69f!important;border-color: #ffa500!important;}
.tabmenu{font-size: 13px;}
 
.tabmenu.formtab .selected a {
    color: white!important;
    background-color: #369;
    border: 2px solid #369!important;
}
 
.roundfield {
    width: 500px;
    background-color: #ECF3F9;
    border: 1px solid #369;
    border-radius: 0;
    padding: 5px 10px 10px 10px;
    font-size: large;
    color: #369;
    font-weight: 500;
}
 
.titlebox .fancy-toggle-button .remove {
    background-color: #ef5350!important;
    padding: 4px 5px 4px 5px;
    border: none;
    background-image: none;
}
 
.titlebox .fancy-toggle-button .add{
    background-color: #66BB6A!important;
    padding: 4px 5px 4px 5px;
    border: none;
    background-image: none;
}
 
.titlebox .RESDashboardToggle, .titlebox .RESshortcut, .titlebox .RESshortcutside{
    background-color: #66BB6A!important;
    padding: 4px 5px 4px 5px;
    border: none;
    background-image: none;
}
 
.morelink {
    display: block;
    text-align: center;
    position: relative;
    border: 1px solid #369;
    background: #ecf3f9;
    font-weight: bold;
    letter-spacing: -.4px;
}
 
.morelink:hover{color:#fff;background: #369;border: 1px solid #ecf3f9;}
.morelink .nub{display:none;}
.sidecontentbox .content{border: 1px solid #369;}
.sidecontentbox .title h1 {color: #369;}
.md hr{background:#369;height:2px;}
.subscribers{font-weight: bold;font-size: 12px;text-align:center;}
.users-online:before {display:none;}
.side .md h1, .side .md h2 {color: #369;}
 
.sidecontentbox .content {
    margin: 0!important;
    padding: 5px!important;
    font-size: larger;
    list-style: none;
}
 
.flairselector h2 {background: none;}
.flairselector form{border-top: solid 1px #369;}
.flairselector.drop-choices.active {border: solid 1px #369;}
 
 
 
/* CONTENT AND POSTS */
 
.stickied {background: #C8E6C9;border:none!important;padding: 7px;margin-right: 300px}
body:not(.comments-page) .stickied .tagline {color: #2B8B27!important; font-weight: bold;}
div.content {font-size: 12px;padding: 5px;}
.thumbnail.self{display:none;}
.link .title {font-size: medium;font-weight: normal;margin-bottom: 1px;}
.link.last-clicked {border: none; border-bottom: 1px solid #dde9f3!important;}
.thing{border-bottom: 1px solid #dde9f3; padding: 6px;}
 
.thing .title {
    color: #369;
    outline: none;
    margin-right: .4em;
    padding: 0px;
    overflow: hidden;
}
 
.entry .buttons li a {color: #888;font-weight: bold;padding: 0 1px;}
.tagline{padding-top: 2px;}
.linefield {background-color:#FFF;}
.linefield textarea, .linefield input[type=text], .linefield input[type=password]{border: 1px solid #369;}
.linefield .title {color:#369;}
 
.arrow.up{background: url(%%up%%) 0 0;}
.arrow.upmod {background: url(%%upm%%) 0 0;}
.arrow.down{background: url(%%down%%) 0 0;}
.arrow.downmod {background: url(%%downm%%) 0 0;}
 
.over18 a.title:link, .over18 a.title:visited, body:not(.comments-page) .over18 .link .tagline, body:not(.comments-page) .over18 .tagline, body:not(.comments-page) .over18 .entry .buttons li a, body:not(.comments-page) .over18 .entry .buttons li + li {color: #D10023!important;padding-bottom: 0!important;}
 
 
 
/* USER FLAIRS */
 
.flair {
    min-width: 14px;
    max-width: 14px;
    position: relative;
    height: 14px;
    line-height: 14px;
    border: none;
    border-radius: 10px;
    overflow: hidden;
    padding: 1px;
    vertical-align: middle;
    font-size: 10px!important;
    text-indent: 3px;
    transition: all 0.5s;
}
 
.flair:hover{max-width:500px;padding-right:6px;padding-left:4px;color:#fff}
 
/* Add custom flairs below this line, athough some have already been provided. */
 
.flair-red {background: #e57373;color: #e57373;}
.flair-orange {background: #FF9800;color: #FF9800;}
.flair-yellow {background: #FFCA28;color: #FFCA28;}
.flair-green {background: #81C784;color: #81C784;}
.flair-blue {background: #81D4FA;color: #81D4FA;}
.flair-purple {background: #9575CD;color: #9575CD;}
.flair-grey {background: #9E9E9E;color: #9E9E9E;}
 
.flair-mod {background: #228822;color: #228822;}
 
 
 
/* LINK FLAIRS */
 
.linkflair .linkflairlabel
{
    text-align:center;
    border-radius:3px;
    padding: 2px 5px 2px 5px;
    border:none;
    overflow: visible;
    font-size: 10px!important;
}
 
/* Add custom flairs below this line, athough some have already been provided. */
 
.linkflair-magenta .linkflairlabel{border:1px solid #E91E63;color:#E91E63;background-color:inherit;}
.linkflair-orange .linkflairlabel{border:1px solid #FF9800;color:#FF9800;background-color:inherit;}
.linkflair-blue .linkflairlabel{border:1px solid #03A9F4;color:#03A9F4;background-color:inherit;}
.linkflair-dblue .linkflairlabel{border:1px solid #007aff;color:#007aff;background-color:inherit;}
.linkflair-navy .linkflairlabel{border:1px solid #546E7A;color:#546E7A;background-color:inherit;}
.linkflair-lgrey .linkflairlabel{border:1px solid #ADADAD;color:#ADADAD;background-color:inherit;}
.linkflair-dgrey .linkflairlabel{border:1px solid #424242;color:#424242;background-color:inherit;}
.linkflair-purple .linkflairlabel{border:1px solid #673AB7;color:#673AB7;background-color:inherit;}
.linkflair-black .linkflairlabel{border:1px solid #212121;color:#212121;background-color:inherit;}
 
.linkflair-sticky .linkflairlabel{border: 1px solid #4CAF50; color:#4CAF50; background-color:#FFF;}
.linkflair-nsfw .linkflairlabel{border:1px solid #D10023;color:#D10023;background-color:inherit;}
 
 

    /* SNIPPETS */

/* removes reddit from banner */
#header-img.default-header { width: 35px; }