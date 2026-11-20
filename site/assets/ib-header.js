/* Instrumentation Blog: header menu behaviour for static sections (/assets/ib-header.js) */
(function(){var h=document.querySelector('.ibhd');if(!h)return;
var b=h.querySelector('.ibhd-burger');if(b)b.addEventListener('click',function(){var o=h.classList.toggle('menu-open');b.setAttribute('aria-expanded',o?'true':'false');});
h.querySelectorAll('.ibhd-sub').forEach(function(s){s.addEventListener('click',function(e){e.preventDefault();var li=s.parentNode,o=li.classList.toggle('open');s.setAttribute('aria-expanded',o?'true':'false');});});
h.querySelectorAll('.ibhd-lbl').forEach(function(l){l.addEventListener('click',function(){var li=l.parentNode,o=li.classList.toggle('open');var s=li.querySelector('.ibhd-sub');if(s)s.setAttribute('aria-expanded',o?'true':'false');});});
var f=h.querySelector('.ibhd-search');if(f){f.querySelector('button').addEventListener('click',function(e){var i=f.querySelector('input');if(!f.classList.contains('open')&&!i.value){e.preventDefault();f.classList.add('open');i.focus();}});}
document.addEventListener('click',function(e){if(!h.contains(e.target)){h.querySelectorAll('li.open').forEach(function(li){li.classList.remove('open');});}});
})();
