(window.webpackJsonp=window.webpackJsonp||[]).push([[285],{1385:function(e,t,r){"use strict";r.d(t,"a",(function(){return c}));var n=r(1),o=(r(19),r(21)),c=function(){var e=Object(n.a)(regeneratorRuntime.mark((function e(data){return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:o.a.debug("Pushing dataLayer event:",data),window.dataLayer.push(data);case 2:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()},2064:function(e,t,r){"use strict";r.r(t);r(16),r(15),r(13),r(17),r(18);var n=r(3),o=(r(33),r(43),r(82)),c=r(139),d=r(178),f=r(1385),l=r(21),m=r(22),O=r.n(m),v=r(42);function w(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function h(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?w(Object(source),!0).forEach((function(t){Object(n.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):w(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}d.a.$on(c.a.PurchaseCompleted,(function(e){var t=e.order,r=t.total/100;window.tap("conversion",t.id,r,{customer_id:t.user}),l.a.debug("Tapfiliate conversion tracked"),O.a.remove("ref")})),d.a.$on(c.a.PurchaseCompleted,(function(e){var t=e.order,r=e.logo,n=Object(o.a)(t);if(0!==t.total){var f=n.reduce((function(e,t){return e+t.price}),0),l=Object(v.b)(t.total,t.items);n=n.map((function(e){return h(h({},e),{},{price:e.price.toFixed()})}));var m=f-l;d.a.$emit(c.a.EcommercePurchase,{coupon:t.coupon?t.coupon.id:void 0,value:m.toFixed(2),transaction_id:t.id,affiliation:null==r?void 0:r.eid,shipping:"0.00",currency:"USD",tax:"0.00",items:n})}})),d.a.$on(c.a.PurchaseCompleted,(function(e){var t=e.order,r={coupon:t.coupon&&0!==Object(v.b)(t.total,t.items)?t.coupon.id:"",items:t.items,discount:Object(v.b)(t.total,t.items),order_id:t.id,total:t.total};0===t.total&&l.a.debug("Skipping analytics.  Reason: Order is free. Data:",r),Object(f.a)(h({event:"purchase_completed"},r))})),d.a.$on(c.a.PurchaseCompleted,(function(e){e.order.items.find((function(e){return"site"===e.package.type}))&&window.$nuxt.$store.dispatch("dashboard/markStepAsComplete","website")}))}}]);
//# sourceMappingURL=449fedf.js.map