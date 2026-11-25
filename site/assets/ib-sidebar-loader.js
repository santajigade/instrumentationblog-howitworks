/* Loads the shared sidebar; the hourly key lets sidebar changes go live within an hour despite long CDN caching. */
(function(){if(window.__ibsxl)return;window.__ibsxl=1;var d=new Date(),k=''+d.getUTCFullYear()+(d.getUTCMonth()+1)+d.getUTCDate()+d.getUTCHours();var s=document.createElement('script');s.src='/assets/ib-sidebar.js?h='+k;document.head.appendChild(s);})();
